# Ejemplo 1 — Grano BATES y carcasa de acero AISI 304

Aplica las ecuaciones de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md) y [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md) a la misión común: presupuesto de masa con acero y geometría del grano BATES.

Cálculo: `python3 scripts/ejemplo1_bates.py`. Todas las cuentas de este ejemplo son fórmulas escritas en cada paso; el script solo las evalúa. **No hay valores simulados en este ejemplo.**

**Versión web:** https://atlasx-rocketry.github.io/motor-solido/ejemplos/ejemplo_1.html

## Cómo leer este documento

Cada paso es una hoja dividida en dos columnas:

- **Resolución** (izquierda): qué se calcula, con qué ecuación, qué significa cada término y el resultado.
- **Suposición y análisis** (derecha): cada simplificación o dato supuesto en esa fila, por qué se acepta y cuánto cambia el resultado si no se cumple. Solo usa lo calculado hasta ese paso.

Al final de cada paso se indica el **resultado** y qué permite calcular en el **paso siguiente**.

**Secuencia:** Datos de entrada → Paso 6 (presupuesto con acero) → Paso 8 (geometría BATES) → Paso 9 (neutralidad) → Paso 10 (alma requerida) → Paso 11 (núcleo y segmentos) → Paso 12 (tubo del motor) → Resumen del ejemplo

---

## Datos de entrada — De la misión común y del material

**Pregunta:** ¿con qué datos empieza este ejemplo?

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**De la misión común** ([`00_mision_comun.md`](00_mision_comun.md))

| Símbolo | Nombre | Valor | Paso de origen |
|---|---|---|---|
| $m_0$ | Masa al despegue | 10 kg | 1 |
| $I_{dis}$ | Impulso de diseño | 2172 N·s | 5 |
| $\bar F$ | Empuje medio | 1600 N | 3 |
| $t_{b,dis}$ | Tiempo de combustión de diseño | 1.36 s | 5 |
| $m_p$ | Masa de propelente | 2.129 kg | 5 |
| $\rho_p$ | Densidad del grano (KNSB) | 1749 kg/m³ | Propelente |
| $V_p$ | Volumen de propelente | 1217 cm³ | 7 |
| $m_{resto}$ | Masa del resto del cohete | 4.95 kg | 6 |
| $\zeta_{min}$ | Fracción de propelente mínima | 0.422 | 6 |

</td>
<td valign="top">

**SD.1 · Se heredan, no se recalculan**

Estos valores ya tienen sus suposiciones analizadas en la misión común. Si cambia alguno, hay que rehacer este ejemplo.

- El más importante para este ejemplo es $t_{b,dis}$ = 1.36 s: obliga a un motor de combustión corta (paso 10).

</td>
</tr>
<tr>
<td valign="top">

**Material de la carcasa: acero inoxidable AISI 304**

| Propiedad | Valor |
|---|---|
| Límite elástico $\sigma_y$ (recocido) | ~205 MPa |
| Resistencia última $\sigma_u$ | ~515 MPa |
| Densidad | ~8000 kg/m³ |
| Resistencia específica $\sigma_y/\rho$ | ~26 kN·m/kg |

En este ejemplo el material solo entra en el **presupuesto de masa** (paso 6). Su resistencia se usa más adelante, para calcular el espesor de pared.

</td>
<td valign="top">

**SD.2 · Propiedades típicas**

Son valores de catálogo para acero 304 recocido. El límite elástico real depende del proveedor y del estado del material (recocido o trabajado en frío).

- **Qué hacer:** usar el certificado del material que se compre.
- **Resistencia específica:** dice cuánta resistencia se obtiene por cada kilo. El acero 304 tiene unas 4 veces menos que el aluminio 6061 (~102 kN·m/kg). Por eso, a igual presión, una carcasa de acero pesa más.

</td>
</tr>
</table>

> **Resultado:** datos de la misión común y propiedades del acero 304.
>
> **Con este resultado →** el paso 6 revisa si un motor de acero cabe en el presupuesto de 10 kg.

---

## Paso 6 — Presupuesto de masa con carcasa de acero

**Pregunta:** si el motor es de acero, ¿cabe el cohete completo en 10 kg?

**Viene de:** $m_p$ = 2.129 kg, $m_{resto}$ = 4.95 kg y $\zeta_{min}$ = 0.422 (misión común, pasos 5 y 6).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $\zeta$ | Fracción de propelente: $m_p/m_{motor}$ | — |
| $m_{motor}$ | Masa del motor completo | kg |
| $m_{estr}$ | Masa de la estructura del motor: carcasa, tapas, tobera y liner | kg |
| $m_{resto,disp}$ | Masa que queda disponible para el resto del cohete | kg |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Masa del motor**

Por definición de fracción de propelente:

$$m_{motor} = \frac{m_p}{\zeta} = \frac{2.129}{0.40} = 5.32\ \text{kg}$$

$$m_{estr} = m_{motor} - m_p = 5.32 - 2.129 = 3.19\ \text{kg}$$

**Masa disponible para el resto del cohete**

$$m_{resto,disp} = m_0 - m_{motor} = 10 - 5.32 = 4.68\ \text{kg}$$

**Comparación con lo necesario**

$$\text{margen} = m_{resto,disp} - m_{resto} = 4.68 - 4.95 = -0.27\ \text{kg}$$

</td>
<td valign="top">

**S6.1 · $\zeta$ = 0.40 para acero**

Todavía no se conoce el espesor de la carcasa, así que se supone una fracción de propelente típica de motores amateur de acero, que suele estar entre 0.35 y 0.45.

- **Por qué se acepta:** permite estimar la masa antes de diseñar la carcasa.
- **Cuándo se verifica:** en la etapa de carcasa, cuando se calcule el espesor de pared con la presión máxima.

**Por qué estos valores en la tabla:** el rango típico del acero (0.35 a 0.45) y 0.50, que sería un motor de acero muy bien optimizado.

| $\zeta$ | Margen de masa |
|---|---|
| 0.35 | −1.03 kg |
| **0.40** | **−0.27 kg** |
| 0.45 | +0.32 kg |
| 0.50 | +0.79 kg |

</td>
</tr>
<tr>
<td valign="top">

**Qué significa el resultado**

El margen es **negativo**: con $\zeta$ = 0.40, el cohete pesaría 10.27 kg y **no cabe en el presupuesto**.

Para que quepa, el motor debe lograr $\zeta \ge \zeta_{min}$ = 0.422 (misión común, paso 6). Es decir, la estructura del motor no puede pesar más de:

$$m_{estr,max} = m_0 - m_{resto} - m_p = 10 - 4.95 - 2.129 = 2.92\ \text{kg}$$

Con $\zeta$ = 0.40 se estimaron 3.19 kg: sobran unos 0.27 kg de acero.

</td>
<td valign="top">

**S6.2 · Requisito derivado para la carcasa**

Este paso no descarta el acero: deja un **objetivo** para la etapa de carcasa.

> La estructura del motor debe pesar **2.92 kg o menos**.

Si no se logra, las salidas son tres: aligerar el resto del cohete, aceptar un apogeo menor o cambiar de material (ejemplo 2).

</td>
</tr>
</table>

> **Resultado del paso 6:** con $\zeta$ = 0.40 el presupuesto **no cierra** (−0.27 kg). La estructura del motor debe pesar **≤ 2.92 kg**.
>
> **Con este resultado →** el material ya dejó su requisito. Los pasos 8 a 12 diseñan la geometría del grano, que no depende del material.

---

## Paso 8 — Geometría de un segmento BATES

**Pregunta:** ¿cómo se describe un segmento BATES y cómo cambia mientras quema?

**Viene de:** las ecuaciones de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md), paso 8.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $D$ | Diámetro exterior del grano | mm |
| $d_0$ | Diámetro inicial del núcleo (el hueco central) | mm |
| $L_0$ | Largo inicial de un segmento | mm |
| $N$ | Número de segmentos | — |
| $x$ | Espesor ya quemado desde el encendido | mm |
| $w$ | Alma (*web*): espesor total que hay que quemar | mm |
| $A_b$ | Área de quemado: superficie que está ardiendo | mm² |
| $V_{seg}$ | Volumen de propelente de un segmento | cm³ |
| $k$ | Fracción del núcleo: $d_0/D$ | — |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Cómo quema un segmento**

Cada segmento es un cilindro con un hueco central. Quema por la superficie del núcleo y por sus dos caras planas. La superficie exterior no quema, porque está protegida por el liner.

Cuando se ha quemado un espesor $x$, el núcleo creció y el segmento se acortó:

$$d(x) = d_0 + 2x \qquad L(x) = L_0 - 2x$$

- $d_0 + 2x$: el núcleo crece $x$ por cada lado.
- $L_0 - 2x$: cada cara retrocede $x$, y son dos.

**Área de quemado** de $N$ segmentos:

$$A_b(x) = N\left[\underbrace{\pi\,d\,L}_{\text{núcleo}} + \underbrace{2 \cdot \frac{\pi}{4}\left(D^2 - d^2\right)}_{\text{dos caras}}\right]$$

- El núcleo es un cilindro: perímetro × largo.
- Cada cara es un anillo: área del círculo exterior menos la del hueco.

</td>
<td valign="top">

**S8.1 · Regresión uniforme**

Toda la superficie retrocede a la misma velocidad $r$.

- **Por qué se acepta:** la presión es casi uniforme en la cámara y el propelente es homogéneo.
- **Cuándo falla:** si el gas que pasa por el núcleo va muy rápido, acelera la combustión en la parte de atrás (combustión erosiva). Se controla con el flujo másico $G$ (paso 11).

**S8.2 · Caras sin inhibir**

Se supone que las dos caras de cada segmento queman libremente, que es lo que define un grano BATES.

</td>
</tr>
<tr>
<td valign="top">

**Volumen de un segmento y alma**

$$V_{seg} = \frac{\pi}{4}\left(D^2 - d_0^2\right) L_0$$

Es el área del anillo multiplicada por el largo.

$$w = \frac{D - d_0}{2}$$

El fuego empieza en el núcleo y avanza hacia la pared. **El alma es la distancia que debe recorrer**: desde la superficie del núcleo hasta la pared. Cuando $x = w$, el propelente se acabó.

</td>
<td valign="top">

**S8.3 · Las caras no se acaban antes**

El segmento también se acorta desde las caras. Para que el grano termine por el alma radial y no por el largo, debe cumplirse $L_0/2 > w$.

> Se verifica en el paso 11 con las medidas finales.

</td>
</tr>
</table>

> **Resultado del paso 8:** ecuaciones de $A_b(x)$, $V_{seg}$ y $w$ en función de $D$, $d_0$, $L_0$ y $N$.
>
> **Con este resultado →** el paso 9 usa $A_b(x)$ para elegir el largo $L_0$ que hace que el empuje sea parejo.

---

## Paso 9 — Neutralidad: el largo de cada segmento

**Pregunta:** ¿qué largo debe tener cada segmento para que el área de quemado, y con ella el empuje, se mantenga lo más pareja posible?

**Viene de:** $A_b(x)$ del paso 8.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Por qué importa que el área sea pareja**

El gas que produce el motor es proporcional al área que quema: $\dot m = \rho_p\,r\,A_b$. Si el área sube y baja, la presión y el empuje también. Un motor con área pareja (**neutro**) tiene presión casi constante, y su carcasa no necesita aguantar picos.

**Los dos efectos que compiten**

- El **núcleo crece** al quemar, así que su área aumenta.
- Las **caras se achican**: el anillo pierde área por dentro y el segmento se acorta.

**Condición:** se pide que el área al inicio ($x$ = 0) sea igual al área al final ($x = w$, cuando $d = D$ y las caras desaparecen):

$$\pi d_0 L_0 + \frac{\pi}{2}\left(D^2 - d_0^2\right) = \pi D\left(L_0 - D + d_0\right)$$

Despejando $L_0$:

$$\boxed{L_0 = \frac{3D + d_0}{2}}$$

</td>
<td valign="top">

**S9.1 · Igualar inicio y final**

Es la forma estándar de diseñar un BATES. No hace el área perfectamente constante: sube un poco en el medio y vuelve a bajar.

- **Cuánto varía:** se calcula en el paso 11 con las medidas reales.
- **Por qué se acepta:** con una regla sencilla se logra una variación pequeña, de pocos por ciento.

</td>
</tr>
</table>

> **Resultado del paso 9:** $L_0 = (3D + d_0)/2$.
>
> **Con este resultado →** solo faltan $D$ y $d_0$. El paso 10 obtiene la primera restricción sobre ellos: el alma que exige el tiempo de combustión.

---

## Paso 10 — Alma requerida por el tiempo de combustión

**Pregunta:** ¿qué espesor de propelente debe tener el grano para quemarse justo en el tiempo que exige la misión?

**Viene de:** $t_{b,dis}$ = 1.36 s (misión común, paso 5) y la ley de Vieille del KNSB (misión común, propelente).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $r$ | Velocidad de regresión: cuánto retrocede la superficie por segundo | mm/s |
| $P$ | Presión de cámara | MPa |
| $t_{b,dis}$ | Tiempo de combustión de diseño | s |
| $w$ | Alma necesaria | mm |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Idea física**

La superficie retrocede a una velocidad $r$ y tiene que recorrer el alma $w$. El tiempo que tarda es:

$$t_b = \frac{w}{r}$$

Es como una vela: cuanto más gruesa, más dura encendida.

Aquí el tiempo **ya está decidido**: la misión común pidió 1.36 s, porque el empuje de 1600 N lo fija la salida del riel. Entonces se despeja el alma:

$$\boxed{w = r \cdot t_{b,dis}}$$

**Velocidad de regresión** con la ley de Vieille, a 2.5 MPa (dentro de la meseta):

$$r = a\,P^{\,n} = 7.852 \times 2.5^{-0.013} = 7.76\ \text{mm/s}$$

**Sustitución**

$$w = 7.76\ \tfrac{\text{mm}}{\text{s}} \times 1.36\ \text{s} = 10.53\ \text{mm}$$

Unidades: (mm/s) × s = mm.

</td>
<td valign="top">

**S10.1 · El motor trabaja en la meseta**

La presión de cámara todavía no se conoce: depende del área de quemado y de la garganta de la tobera. Se supone 2.5 MPa, dentro de la meseta del KNSB (1.5 a 3.8 MPa).

**Por qué estos valores en la tabla:** los dos extremos de la meseta y el valor supuesto.

| Presión | $r$ | Alma $w$ |
|---|---|---|
| 1.5 MPa | 7.72 mm/s | 10.47 mm |
| **2.5 MPa** | **7.76 mm/s** | **10.53 mm** |
| 3.79 MPa | 7.72 mm/s | 10.47 mm |

> En toda la meseta el alma cambia menos de 0.1 mm: el resultado casi no depende de la presión.

A 1.5 MPa se usa el tramo anterior de la tabla de Vieille ($a$ = 8.763, $n$ = −0.314), que da casi lo mismo.

**Cuándo falla:** si la presión real sale de la meseta, $r$ cambia mucho. El modelo de cámara debe comprobar que no sale.

</td>
</tr>
<tr>
<td valign="top">

**Consecuencia para la forma del grano**

Hay que acomodar 1217 cm³ de propelente con solo 10.5 mm de espesor. Es como envolver mucho volumen en una capa delgada: el grano tiene que ser un **tubo de pared delgada y núcleo grande**, repartido en varios segmentos.

</td>
<td valign="top">

**S10.2 · Por qué el diseño anterior ya no sirve**

El BATES de la versión anterior tenía 16.7 mm de alma: quemaba en 16.7 / 7.76 = 2.15 s con un empuje de ≈1000 N, por debajo de lo necesario para salir del riel a 30 m/s.

</td>
</tr>
</table>

> **Resultado del paso 10:** el grano debe tener un alma de **w = 10.5 mm**.
>
> **Con este resultado →** el paso 11 combina el alma con el volumen de propelente para elegir el núcleo, el diámetro y el número de segmentos.

---

## Paso 11 — Núcleo, diámetro y número de segmentos

**Pregunta:** ¿qué combinación de diámetro, núcleo y número de segmentos tiene un alma de 10.5 mm y suma 1217 cm³ de propelente?

**Viene de:** $w$ = 10.53 mm (paso 10), $L_0 = (3D + d_0)/2$ (paso 9), $V_{seg}$ (paso 8) y $V_p$ = 1217 cm³ (misión común, paso 7).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**De la fracción de núcleo al diámetro**

Con $d_0 = k\,D$, el alma queda $w = (D - kD)/2 = D(1 - k)/2$. Despejando el diámetro:

$$D = \frac{2\,w}{1 - k}$$

- Si el núcleo es más grande ($k$ alto), $1 - k$ es pequeño y el diámetro crece, aunque el alma sea la misma.

Con $D$ se obtienen en cascada $d_0 = kD$, $L_0 = (3D + d_0)/2$ y $V_{seg}$.

**Número de segmentos** (ruta B de [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md)):

$$N = \frac{V_p}{V_{seg}}$$

</td>
<td valign="top">

**S11.1 · Cambio de ruta respecto de docs/01**

En `docs/01` se elegían $k$ y $N$, y el diámetro salía de la fórmula de raíz cúbica. Aquí el alma ya está fijada (paso 10), así que la ruta cambia: se elige $k$, sale $D$ del alma y $N$ del volumen.

</td>
</tr>
<tr>
<td valign="top">

**Tabla de opciones**

Se evalúan las ecuaciones anteriores para varios $k$, con $w$ = 10.53 mm. Ejemplo con $k$ = 0.70: $D = 2 \times 10.53 / 0.30 = 70.2$ mm, $d_0 = 49.1$ mm, $L_0 = (3 \times 70.2 + 49.1)/2 = 129.9$ mm.

| $k$ | $D$ | $d_0$ | $L_0$ | $V_{seg}$ | $N = V_p/V_{seg}$ | Largo total |
|---|---|---|---|---|---|---|
| 0.50 | 42.1 mm | 21.1 mm | 73.7 mm | 77 cm³ | 15.8 → 16 | 1209 mm |
| 0.60 | 52.7 mm | 31.6 mm | 94.8 mm | 132 cm³ | 9.2 → 10 | 966 mm |
| 0.65 | 60.2 mm | 39.1 mm | 109.8 mm | 180 cm³ | 6.8 → 7 | 781 mm |
| **0.70** | **70.2 mm** | **49.1 mm** | **129.9 mm** | **256 cm³** | **4.8 → 5** | **657 mm** |
| 0.75 | 84.2 mm | 63.2 mm | 158.0 mm | 385 cm³ | 3.2 → 4 | 638 mm |

</td>
<td valign="top">

**S11.2 · Por qué estos valores de $k$ y cómo se elige**

Se recorre el rango en que un BATES es práctico, de 0.50 a 0.75.

- **Núcleo chico ($k$ ≤ 0.60):** con un alma tan delgada salen 10 a 16 segmentos y más de 1 m de grano. Es difícil de fabricar y de cargar.
- **Núcleo muy grande ($k$ = 0.75):** pocos segmentos, pero un diámetro de 84 mm, y con 4 segmentos sobra un 27 % de propelente.
- **$k$ ≈ 0.70:** 5 segmentos de 70 mm. Es el mejor compromiso entre número de piezas, diámetro y largo.

</td>
</tr>
<tr>
<td valign="top">

**Ajuste fino: exactamente 5 segmentos**

Con $k$ = 0.70 salen 4.75 segmentos. Con 5 enteros sobraría un 5 % de propelente. Se ajusta $k$ para que 5 segmentos sumen exactamente $V_p$:

$$5 \cdot V_{seg}(k) = V_p$$

Esta ecuación no se despeja a mano: se resolvió por tanteo (bisección) con el script. El resultado es:

| Medida | Valor |
|---|---|
| Fracción de núcleo $k$ | 0.693 |
| Diámetro del grano $D$ | **68.6 mm** |
| Diámetro del núcleo $d_0$ | **47.6 mm** |
| Largo de cada segmento $L_0$ | **126.7 mm** |
| Número de segmentos $N$ | **5** |
| Volumen total | 1217 cm³ |

**Comprobaciones**

- Alma: $w = (68.6 - 47.6)/2 = 10.5$ mm ✓
- Tiempo: $t_b = 10.53/7.76 = 1.36$ s ✓
- Caras (S8.3): $L_0/2 = 63.4$ mm, mayor que $w$ ✓

</td>
<td valign="top">

**S11.3 · El ajuste es numérico, no una simulación**

La bisección solo busca el $k$ que cumple una ecuación escrita. Se puede verificar a mano: con $D$ = 68.62 mm, $d_0$ = 47.56 mm y $L_0$ = 126.70 mm,

$$V_{seg} = \frac{\pi}{4}(68.62^2 - 47.56^2)(126.70) = 243.5\ \text{cm}^3$$

y $5 \times 243.5 = 1217$ cm³ ✓.

</td>
</tr>
<tr>
<td valign="top">

**Curva de área de quemado** (paso 8 con las medidas finales)

| $x$ | 0 | 1.76 | 3.51 | 5.27 | 7.02 | 8.78 | 10.53 mm |
|---|---|---|---|---|---|---|---|
| $A_b$ [mm²] | 113 864 | 115 316 | 116 187 | 116 477 | 116 187 | 115 316 | 113 864 |

- Empieza y termina con la misma área (condición del paso 9).
- Variación máxima: $(116\,477 - 113\,864)/113\,864$ = **2.3 %**. El grano es casi neutro.

**Control cruzado del gasto de propelente**

Con el área media, el propelente que se quema por segundo es $\dot m = \rho_p\,r\,\bar A_b$ = 1749 × 0.00776 × 0.1156 ≈ **1.569 kg/s**. Por otro camino, $m_p/t_b$ = 2.129/1.357 = **1.569 kg/s**. Coinciden: la geometría es coherente con la misión.

</td>
<td valign="top">

**S11.4 · Flujo másico en el núcleo (preliminar)**

Todo el gas de los 5 segmentos sale por el núcleo del último. Si va muy rápido, aparece combustión erosiva (S8.1). Se mide con el flujo másico:

$$G = \frac{\rho_p\,r\,A_{b,max}}{\frac{\pi}{4}d_0^2} = \frac{1749 \times 0.00776 \times 0.1165}{0.001776} \approx 890\ \text{kg/m}^2\text{s}$$

> 890 < 1400 kg/m²s (límite práctico): cumple con holgura, gracias al núcleo grande.

Es **preliminar**: supone $r$ de la meseta. Se confirma con el modelo de cámara.

</td>
</tr>
</table>

> **Resultado del paso 11:** **5 segmentos** de $D$ = **68.6 mm**, $d_0$ = **47.6 mm** y $L_0$ = **126.7 mm**. Alma de 10.5 mm, neutralidad de 2.3 % y $G$ = 890 kg/m²s.
>
> **Con este resultado →** el paso 12 calcula las medidas interiores del tubo que debe alojar los 5 segmentos.

---

## Paso 12 — Dimensiones del tubo del motor

**Pregunta:** ¿qué diámetro interior y qué largo debe tener el tubo de la carcasa?

**Viene de:** $D$, $L_0$ y $N$ (paso 11).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $D_{int}$ | Diámetro interior del tubo | mm |
| $e_{liner}$ | Espesor del liner (tubo aislante entre grano y carcasa) | mm |
| $\delta$ | Holgura radial para introducir los granos | mm |
| $s$ | Separación entre segmentos | mm |
| $L_{granos}$ | Largo ocupado por los granos | mm |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Diámetro interior**

$$D_{int} = D + 2\,e_{liner} + 2\,\delta = 68.6 + 2(1.0) + 2(0.25) = 71.1\ \text{mm}$$

**Largo de los granos**

$$L_{granos} = N\,L_0 + (N - 1)\,s = 5(126.7) + 4(2) = 642\ \text{mm}$$

A esto se suman las tapas y la tobera, que se diseñan en la etapa de carcasa.

**Carga volumétrica** (cuánto del espacio interior es propelente):

$$\frac{V_p}{\frac{\pi}{4}D^2 L_{granos}} = \frac{1217}{\frac{\pi}{4}(6.86)^2(64.2)} \approx 51\ \%$$

</td>
<td valign="top">

**S12.1 · Liner de 1 mm, holgura de 0.25 mm y separación de 2 mm**

Son valores típicos de motores amateur de este tamaño. Se ajustan cuando se elijan el liner y el tubo comercial.

**S12.2 · Carga volumétrica baja**

El 51 % es bajo para un BATES (suele ser 70–80 %). Es el precio del alma delgada: el núcleo grande deja mucho espacio vacío.

- **Consecuencia:** el tubo es más largo y pesado de lo que sería con alma gruesa. Con acero, eso aprieta aún más el presupuesto del paso 6.
- **Ventaja:** el núcleo grande da un flujo másico bajo (S11.4).

</td>
</tr>
</table>

> **Resultado del paso 12:** tubo de **≥ 71.1 mm** de diámetro interior y **642 mm** de largo de granos, más tapas.
>
> **Con este resultado →** termina la geometría. El siguiente paso es el modelo de cámara: presión, garganta de la tobera y espesor de la carcasa.

---

## Resumen del ejemplo

Ejemplo 1: grano BATES y carcasa de acero AISI 304. Todos los valores salen de fórmulas escritas en los pasos; ninguno es simulado.

| Magnitud | Valor | Paso |
|---|---|---|
| Fracción de propelente supuesta | $\zeta$ = 0.40 | 6 |
| Margen de masa | **−0.27 kg: no cierra** | 6 |
| Estructura máxima del motor | 2.92 kg | 6 |
| Alma requerida | $w$ = 10.5 mm | 10 |
| Segmentos | 5 | 11 |
| Diámetro del grano / núcleo | 68.6 mm / 47.6 mm | 11 |
| Largo de cada segmento | 126.7 mm | 11 |
| Neutralidad (variación de $A_b$) | 2.3 % | 11 |
| Flujo másico (preliminar) | 890 kg/m²s | 11 |
| Diámetro interior del tubo | ≥ 71.1 mm | 12 |
| Largo de granos | 642 mm | 12 |
| Carga volumétrica | 51 % | 12 |

**Pendiente para la etapa de carcasa**

1. **Modelo de cámara:** presión y garganta de la tobera. Debe confirmar que la presión queda en la meseta (S10.1) y el flujo másico (S11.4).
2. **Espesor de pared** con $\sigma_y$ = 205 MPa y factor de seguridad de 1.5–2.
3. **Masa real de la estructura:** debe ser ≤ 2.92 kg para que el cohete quepa en 10 kg.
