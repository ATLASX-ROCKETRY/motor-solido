"""Ejemplo 1: grano BATES + carcasa de acero AISI 304 (pasos 6 y 8 a 12).

Todas las cuentas son fórmulas cerradas (cálculo a mano); este script solo
las evalúa para que los números del documento se puedan reproducir.
No hay simulación en este ejemplo.

Uso:  python3 scripts/ejemplo1_bates.py
"""
import math
from comun import r_knsb, RHO_P, M0, MASAS_RESTO, ISP, G0, MARGEN

# --- De la misión común ---
I_REQ = 1809.6                    # paso 4 (simulado, caso 1) [N·s]
I_DIS = (1 + MARGEN) * I_REQ      # paso 5 [N·s]
F_MEDIO = 1600.0                  # paso 3 [N]
MP = I_DIS / (ISP * G0)           # paso 5 [kg]
VP = MP / RHO_P                   # paso 7 [m3]
TB = I_DIS / F_MEDIO              # paso 5 [s]
M_RESTO = sum(MASAS_RESTO.values())

# --- Decisiones del ejemplo ---
ZETA = 0.40                       # fracción de propelente supuesta, acero 304
P_DISENO = 2.5                    # presión supuesta dentro de la meseta [MPa]
E_LINER = 1.0e-3                  # espesor de liner [m]
DELTA = 0.25e-3                   # holgura radial [m]
S_SEP = 2.0e-3                    # separación entre segmentos [m]
G_MAX = 1400.0                    # flujo másico máximo [kg/m2 s]


def geometria(k, w):
    """D, d0, L0 y volumen de un segmento para un alma w y una fracción de núcleo k."""
    D = 2 * w / (1 - k)
    d0 = k * D
    L0 = (3 * D + d0) / 2
    V = math.pi / 4 * (D**2 - d0**2) * L0
    return D, d0, L0, V


def area_quemado(D, d0, L0, N, x):
    d, L = d0 + 2 * x, L0 - 2 * x
    return N * (math.pi * d * L + math.pi / 2 * (D**2 - d**2))


def k_para_N(N, w):
    """Fracción de núcleo k con la que N segmentos suman exactamente V_p (bisección)."""
    lo, hi = 0.3, 0.9
    for _ in range(60):
        k = 0.5 * (lo + hi)
        if N * geometria(k, w)[3] < VP:
            lo = k        # volumen corto: núcleo más grande (D crece)
        else:
            hi = k
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    print(f"Misión común: I_dis={I_DIS:.0f} N·s  m_p={MP:.3f} kg  V_p={VP*1e6:.0f} cm3  t_b={TB:.3f} s")

    # Paso 6
    m_motor = MP / ZETA
    print(f"\nPaso 6: m_motor={m_motor:.2f}  estructura={m_motor-MP:.2f}  disponible resto={M0-m_motor:.2f}  "
          f"necesario={M_RESTO:.2f}  margen={M0-m_motor-M_RESTO:+.2f} kg")
    for z in (0.35, 0.40, 0.45, 0.50):
        print(f"   zeta={z:.2f}: margen {M0 - MP/z - M_RESTO:+.2f} kg")
    print(f"   zeta_min={MP/(M0-M_RESTO):.3f}  estructura max={M0-M_RESTO-MP:.2f} kg")

    # Paso 10: alma
    r = r_knsb(P_DISENO)
    w = r * TB
    print(f"\nPaso 10: r={r*1e3:.3f} mm/s  w=r*t_b={w*1e3:.2f} mm")
    for P in (1.5, 2.5, 3.79):
        print(f"   P={P} MPa: r={r_knsb(P)*1e3:.3f} mm/s  w={r_knsb(P)*TB*1e3:.2f} mm")

    # Paso 11: tabla de k
    print("\nPaso 11: k, D, d0, L0, Vseg, N=Vp/Vseg, largo")
    for k in (0.50, 0.60, 0.65, 0.70, 0.75):
        D, d0, L0, V = geometria(k, w)
        N = VP / V
        Nc = math.ceil(N)
        print(f"   k={k:.2f} D={D*1e3:.1f} d0={d0*1e3:.1f} L0={L0*1e3:.1f} Vseg={V*1e6:.0f} N={N:.2f} -> {Nc}  "
              f"largo={(Nc*L0+(Nc-1)*S_SEP)*1e3:.0f} mm  exceso={(Nc*V/VP-1)*100:.0f} %")

    N = 5
    k = k_para_N(N, w)
    D, d0, L0, V = geometria(k, w)
    print(f"\nElegido N={N}: k={k:.4f}  D={D*1e3:.2f}  d0={d0*1e3:.2f}  L0={L0*1e3:.2f} mm  "
          f"Vtot={N*V*1e6:.1f} cm3  w=(D-d0)/2={(D-d0)/2*1e3:.2f} mm  t_b=w/r={(D-d0)/2/r:.3f} s")

    # Paso 9: curva de área
    xs = [w * i / 6 for i in range(7)]
    Ab = [area_quemado(D, d0, L0, N, x) for x in xs]
    xx = [w * i / 400 for i in range(401)]
    AA = [area_quemado(D, d0, L0, N, x) for x in xx]
    print("   A_b(x):", ", ".join(f"x={x*1e3:.2f}:{a*1e6:.0f}" for x, a in zip(xs, Ab)))
    print(f"   A_b min={min(AA)*1e6:.0f} max={max(AA)*1e6:.0f} mm2  variación={(max(AA)/min(AA)-1)*100:.1f} %")

    # Verificación de flujo (preliminar, meseta)
    A_port = math.pi / 4 * d0**2
    G = RHO_P * r * max(AA) / A_port
    print(f"   A_port={A_port*1e6:.0f} mm2  G_final={G:.0f} kg/m2s (límite {G_MAX:.0f})")
    print(f"   gasto másico medio = m_p/t_b = {MP/TB:.3f} kg/s ; rho*r*Ab_medio = {RHO_P*r*sum(AA)/len(AA):.3f} kg/s")

    # Paso 12
    D_int = D + 2 * E_LINER + 2 * DELTA
    L_gr = N * L0 + (N - 1) * S_SEP
    print(f"\nPaso 12: D_int={D_int*1e3:.1f} mm  largo granos={L_gr*1e3:.0f} mm  carga volumétrica="
          f"{N*V/(math.pi/4*D**2*L_gr)*100:.0f} %")
