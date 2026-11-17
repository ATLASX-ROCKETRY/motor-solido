# Atlas X — Propulsión

Diseño de un motor cohete de propelente sólido para el cohete Atlas X.

## 🌐 Página web

- **Portada:** https://atlasx-rocketry.github.io/motor-solido/
- **Misión común (con animación interactiva):** https://atlasx-rocketry.github.io/motor-solido/ejemplos/mision_comun.html

Publicada con GitHub Pages desde la rama `main`.

## Contenido

### Ecuaciones (solo símbolos)

| Archivo | Qué contiene |
|---|---|
| [`docs/01_mision_a_geometria.md`](docs/01_mision_a_geometria.md) | Cadena de ecuaciones: de la misión a las longitudes del grano BATES (pasos 1–12) |
| [`docs/02_numero_de_granos.md`](docs/02_numero_de_granos.md) | Cómo se define el número de segmentos N: mínimo por volumen, máximo por flujo másico, espacio |
| [`docs/03_geometria_finocyl.md`](docs/03_geometria_finocyl.md) | Ecuaciones del grano Finocyl (reemplazan a los pasos 8–11) |

### Ejemplos aplicados (hasta el paso 12)

Misión: 10 kg al despegue (con motor), 1000 m de apogeo, fuselaje de 150 mm, propelente KNSB.

| Archivo | Qué contiene |
|---|---|
| [`ejemplos/00_mision_comun.md`](ejemplos/00_mision_comun.md) | Pasos 1–7, iguales para los tres ejemplos (versión página: `ejemplos/mision_comun.html`) |
| [`ejemplos/ejemplo_1_bates_acero304.md`](ejemplos/ejemplo_1_bates_acero304.md) | BATES + acero AISI 304 |
| [`ejemplos/ejemplo_2_bates_al6061.md`](ejemplos/ejemplo_2_bates_al6061.md) | BATES + aluminio 6061-T6 |
| [`ejemplos/ejemplo_3_finocyl_acero304.md`](ejemplos/ejemplo_3_finocyl_acero304.md) | Finocyl + acero AISI 304 |

### Scripts (Python 3 + numpy)

```bash
python3 scripts/comun.py                    # misión común
python3 scripts/paso4_simulacion.py         # valores simulados del paso 4 (10 casos)
python3 scripts/ejemplo_bates.py acero304   # ejemplo 1
python3 scripts/ejemplo_bates.py al6061     # ejemplo 2
python3 scripts/ejemplo_finocyl.py          # ejemplo 3 (~25 s, búsqueda de geometría)
```

Para regenerar la página HTML después de editar el `.md` (requiere `pip install markdown`):

```bash
python3 scripts/md_a_html.py ejemplos/00_mision_comun.md ejemplos/mision_comun.html ejemplos/mision_comun_animacion.html
```

## Resumen de resultados

Común: impulso de diseño 2172 N·s (clase K), empuje de 1600 N (salida del riel a 30 m/s), 2.129 kg de propelente, 1217 cm³.

> ⚠️ Los ejemplos 1–3 todavía usan la versión anterior de la misión común (2191 N·s, 2.148 kg) y deben revisarse. En particular, el BATES quema en 2.15 s y su empuje no alcanza para salir del riel a 30 m/s.

| | Ej. 1: BATES + 304 | Ej. 2: BATES + 6061 | Ej. 3: Finocyl + 304 |
|---|---|---|---|
| Grano | 4 × (D 66.8, d₀ 33.4, L₀ 116.9 mm) | igual al ej. 1 | 1 × (D 66.8, r_c 20, 10 aletas 4×4 mm) |
| Tubo: diámetro interior | 69.3 mm | 69.3 mm | 69.3 mm |
| Largo de grano | 473 mm | 473 mm | 589 mm |
| Neutralidad | 7.5 % | 7.5 % | 3.5 % |
| ζ supuesto | 0.40 | 0.55 | 0.40 |
| Margen de masa | **−0.32 kg ❌** | **+1.14 kg ✅** | **−0.32 kg ❌** (≈ −0.8 por el largo extra) |

Para que el cohete no supere 10 kg, el motor debe lograr **ζ ≥ 0.422**
(estructura ≤ 2.92 kg).

> ⚠️ ζ es un supuesto. Se verifica en la etapa siguiente (modelo de cámara →
> P_max → espesor de pared con SF 1.5–2 → masa real de la carcasa).

## Estado

- [x] Ecuaciones: misión → geometría (BATES y Finocyl)
- [x] Ejemplos 1–3 hasta el paso 12
- [ ] Modelo de cámara: P(t), Kn, garganta
- [ ] Carcasa: espesor de pared, tapas, ζ real
- [ ] Tobera

## Seguridad

Un motor de alta potencia requiere, antes de cualquier vuelo: pruebas estáticas en
banco con distancia de seguridad, prueba hidrostática de la carcasa y los permisos
que exija la normativa local.
