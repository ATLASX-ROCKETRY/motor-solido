"""Paso 4 de la misión común: todas las simulaciones de vuelo, caso por caso.

Qué hace
--------
Simula el vuelo vertical del cohete con las ecuaciones del paso 4
(docs/... y ejemplos/00_mision_comun.md):

    dh/dt = v
    m dv/dt = F - 1/2 rho(h) Cd A v|v| - m g
    dm/dt = -F / (Isp g0)      mientras quema

con el método de Euler (pasos de tiempo dt) y busca por bisección el
impulso total I_req que lleva el cohete exactamente a 1000 m.

Las funciones de integración y bisección están en scripts/comun.py.
Los valores base (masa, diámetro, Cd, empuje, Isp, densidad del aire)
también están al inicio de scripts/comun.py.

Cada caso cambia UNA sola variable respecto del caso base. La tabla que
imprime este script es la fuente de todos los valores marcados como
"simulado" en ejemplos/00_mision_comun.md.

Uso:  python3 scripts/paso4_simulacion.py
"""
import math
import comun

BASE = dict(cd=comun.CD, F=comun.F_MEDIO, rho0=comun.RHO0, isp=comun.ISP, dt=1e-3)

CASOS = [
    # (número, descripción, cambios respecto del caso base)
    (1, "Caso base", {}),
    (2, "Sin aire (Cd = 0)", {"cd": 0.0}),
    (3, "Cd = 0.4 (-20 %)", {"cd": 0.4}),
    (4, "Cd = 0.6 (+20 %)", {"cd": 0.6}),
    (5, "Empuje 1200 N", {"F": 1200.0}),
    (6, "Empuje 2400 N", {"F": 2400.0}),
    (7, "Isp = 120 s", {"isp": 120.0}),
    (8, "Aire de sitio alto (rho0 = 1.0)", {"rho0": 1.0}),
    (9, "Paso de tiempo 0.2 ms", {"dt": 2e-4}),
]


def con_parametros(p, funcion, *args, **kw):
    """Ejecuta una función de comun.py con los parámetros p y restaura los originales."""
    guardado = (comun.ISP, comun.RHO0)
    comun.ISP, comun.RHO0 = p["isp"], p["rho0"]
    try:
        return funcion(*args, **kw)
    finally:
        comun.ISP, comun.RHO0 = guardado


def estado_apagado(I, p):
    """Altura y velocidad en el instante en que se apaga el motor."""
    A = math.pi / 4 * comun.D_COHETE**2
    mp = I / (p["isp"] * comun.G0)
    tb = I / p["F"]
    mdot = mp / tb
    h = v = t = 0.0
    m = comun.M0
    dt = p["dt"]
    while t < tb:
        m -= mdot * dt
        rho = p["rho0"] * math.exp(-h / comun.H_ESC)
        a = (p["F"] - 0.5 * rho * p["cd"] * A * v * abs(v)) / m - comun.G
        v += a * dt
        h += v * dt
        t += dt
    return h, v


def correr(cambios):
    p = dict(BASE, **cambios)
    kw = dict(F=p["F"], cd=p["cd"], dt=p["dt"])
    I = con_parametros(p, comun.impulso_requerido, **kw)
    h_ap, vmax, mp, tb = con_parametros(p, comun.apogeo, I, **kw)
    h_b, _ = estado_apagado(I, p)
    return I, vmax, mp, tb, h_b


if __name__ == "__main__":
    print("Valores base (scripts/comun.py):", BASE)
    print()
    print(f"{'Caso':<5}{'Descripción':<34}{'I_req [N·s]':>12}{'v_max [m/s]':>13}{'m_p [kg]':>10}{'t_b [s]':>9}{'h_b [m]':>9}")
    for n, desc, cambios in CASOS:
        I, vmax, mp, tb, h_b = correr(cambios)
        print(f"{n:<5}{desc:<34}{I:>12.1f}{vmax:>13.0f}{mp:>10.2f}{tb:>9.2f}{h_b:>9.0f}")

    # Paso 5: apogeo con el impulso de diseño
    I_req = correr({})[0]
    I_dis = (1 + comun.MARGEN) * I_req
    h = comun.apogeo(I_dis, F=BASE["F"], cd=BASE["cd"])[0]
    print()
    print(f"Caso 10  Paso 5: apogeo con I_dis = {I_dis:.0f} N·s  ->  {h:.0f} m")
