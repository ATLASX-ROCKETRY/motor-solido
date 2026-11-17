# Ejemplo 1 — Grano BATES y carcasa de acero AISI 304

Este ejemplo toma los resultados de la misión común y diseña la geometría de un motor con grano BATES y carcasa de acero inoxidable AISI 304. Aplica las ecuaciones de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md) y [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md).

Cálculo: `python3 scripts/ejemplo1_bates.py`. Todas las cuentas son fórmulas escritas en cada paso; el script solo las evalúa para que los números se puedan reproducir. **En este ejemplo no hay valores simulados.**

**Versión web:** https://atlasx-rocketry.github.io/motor-solido/ejemplos/ejemplo_1.html

## Cómo leer este documento

Cada paso es una hoja dividida en dos columnas:

- **Resolución** (izquierda): qué se calcula, con qué ecuación, qué significa cada término y el resultado.
- **Suposición y análisis** (derecha): qué se supone en esa fila, por qué se acepta y cuánto cambia el resultado si no se cumple. Solo usa lo calculado hasta ese paso.

Al final de cada paso se indica el **resultado** y qué permite calcular en el **paso siguiente**.

**Secuencia:** Datos de entrada → Paso 6 (presupuesto con acero) → Paso 8 (geometría BATES) → Paso 9 (neutralidad) → Paso 10 (alma requerida) → Paso 11 (núcleo y segmentos) → Paso 12 (tubo del motor) → Resumen del ejemplo

---

## Datos de entrada — De la misión común y del material

**Pregunta:** ¿con qué datos empieza este ejemplo y de dónde sale cada uno?

**Qué se obtiene:** la lista de valores heredados de la misión común y las propiedades del acero que se usarán más adelante.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### Valores que llegan de la misión común

Estos números ya se calcularon y justificaron en [`00_mision_comun.md`](00_mision_comun.md). Aquí solo se reúnen, con el paso donde se obtuvo cada uno.

| Símbolo | Nombre | Valor | Paso de origen |
|---|---|---|---|
| $m_0$ | Masa al despegue, con el motor cargado | 10 kg | 1 |
| $\bar F$ | Empuje medio del motor | 1600 N | 3 |
| $I_{dis}$ | Impulso de diseño | 2172 N·s | 5 |
| $t_{b,dis}$ | Tiempo de combustión de diseño | 1.36 s | 5 |
| $m_p$ | Masa de propelente | 2.129 kg | 5 |
| $m_{resto}$ | Masa del resto del cohete | 4.95 kg | 6 |
| $\zeta_{min}$ | Fracción de propelente mínima | 0.422 | 6 |
| $\rho_p$ | Densidad del grano de KNSB | 1749 kg/m³ | Propelente |
| $V_p$ | Volumen de propelente | 1217 cm³ | 7 |

</td>
<td valign="top">

#### SD.1 · Los valores se heredan, no se recalculan

**Qué se supone.** Que los resultados de la misión común son correctos.

**Por qué se acepta.** Cada uno tiene sus propias suposiciones analizadas en ese documento.

**Qué pasa si cambia alguno.** Hay que rehacer este ejemplo desde el paso donde se use.

> El dato que más condiciona este ejemplo es $t_{b,dis}$ = 1.36 s: obliga a un motor que queme rápido (paso 10).

</td>
</tr>
<tr>
<td valign="top">

#### Material de la carcasa: acero inoxidable AISI 304

| Propiedad | Símbolo | Valor |
|---|---|---|
| Límite elástico (recocido) | $\sigma_y$ | ~205 MPa |
| Resistencia última | $\sigma_u$ | ~515 MPa |
| Densidad | $\rho_{acero}$ | ~8000 kg/m³ |
| Resistencia específica | $\sigma_y/\rho$ | ~26 kN·m/kg |

**Dónde se usa cada propiedad:**

- **En este ejemplo**, el material solo entra en el presupuesto de masa (paso 6).
- **Más adelante**, el límite elástico servirá para calcular el espesor de la pared de la carcasa.

</td>
<td valign="top">

#### SD.2 · Propiedades de catálogo

**Qué se supone.** Valores típicos de catálogo para acero 304 recocido.

**Por qué se acepta.** Son suficientes para una primera estimación.

**Qué pasa si no se cumple.** El límite elástico real depende del proveedor y del estado del material (recocido o trabajado en frío). Hay que usar el certificado del material que se compre.

> **Resistencia específica:** dice cuánta resistencia se obtiene por cada kilo. El acero 304 tiene unas 4 veces menos que el aluminio 6061 (~102 kN·m/kg). Por eso, a igual presión, una carcasa de acero pesa más.

</td>
</tr>
</table>

> **Resultado:** valores de la misión común y propiedades del acero 304.
>
> **Con este resultado →** el paso 6 revisa si un motor con carcasa de acero cabe en el presupuesto de 10 kg.

---

## Paso 6 — Presupuesto de masa con carcasa de acero

**Pregunta:** si la carcasa es de acero, ¿el cohete completo pesa 10 kg o menos?

**Viene de:** $m_p$ = 2.129 kg, $m_{resto}$ = 4.95 kg y $\zeta_{min}$ = 0.422 (misión común, pasos 5 y 6).

**Qué se obtiene:** el margen de masa con acero y la masa máxima que puede tener la estructura del motor.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### Variables

| Símbolo | Nombre | Unidad |
|---|---|---|
| $\zeta$ | Fracción de propelente: qué parte del motor completo es propelente | — |
| $m_{motor}$ | Masa del motor completo, cargado | kg |
| $m_{estr}$ | Masa de la estructura del motor: carcasa, tapas, tobera y liner | kg |
| $m_{resto,disp}$ | Masa que queda disponible para el resto del cohete | kg |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

#### 1. Masa del motor completo

La fracción de propelente se define como $\zeta = m_p / m_{motor}$. Si se conoce $\zeta$, se despeja la masa del motor.

##### Ecuación

$$m_{motor} = \frac{m_p}{\zeta}$$

##### Cálculo

$$m_{motor} = \frac{2.129\ \text{kg}}{0.40} = 5.32\ \text{kg}$$

La estructura es lo que no es propelente:

$$m_{estr} = m_{motor} - m_p = 5.32 - 2.129 = 3.19\ \text{kg}$$

#### 2. Masa que queda para el resto del cohete

$$m_{resto,disp} = m_0 - m_{motor} = 10 - 5.32 = 4.68\ \text{kg}$$

#### 3. Comparación con lo necesario

$$\text{margen} = m_{resto,disp} - m_{resto} = 4.68 - 4.95 = -0.27\ \text{kg}$$

</td>
<td valign="top">

#### S6.1 · $\zeta$ = 0.40 para un motor de acero

**Qué se supone.** Una fracción de propelente de 0.40: de cada 10 kg de motor, 4 kg son propelente y 6 kg son estructura.

**Por qué se acepta.** El espesor de la carcasa todavía no se conoce. Los motores amateur de acero suelen tener $\zeta$ entre 0.35 y 0.45, y 0.40 está en el medio.

**Cuándo se verifica.** En la etapa de carcasa, cuando se calcule el espesor de pared con la presión máxima.

##### Sensibilidad

Se repite el cálculo del margen con otros valores de $\zeta$: el rango típico del acero (0.35 a 0.45) y 0.50, que sería un motor de acero muy optimizado.

| $\zeta$ | Masa del motor | Margen |
|---|---|---|
| 0.35 | 6.08 kg | −1.03 kg |
| **0.40** | **5.32 kg** | **−0.27 kg** |
| 0.45 | 4.73 kg | +0.32 kg |
| 0.50 | 4.26 kg | +0.79 kg |

</td>
</tr>
<tr>
<td valign="top">

#### 4. Qué significa el resultado

El margen es **negativo**: con $\zeta$ = 0.40 el cohete pesaría 10.27 kg y **no cabe en el presupuesto**.

Para que quepa, el motor debe tener al menos la fracción mínima de la misión común, $\zeta_{min}$ = 0.422. Expresado como masa, la estructura no puede superar:

$$m_{estr,max} = m_0 - m_{resto} - m_p = 10 - 4.95 - 2.129 = 2.92\ \text{kg}$$

| | Estimado con $\zeta$ = 0.40 | Máximo permitido |
|---|---|---|
| Estructura del motor | 3.19 kg | **2.92 kg** |
| Diferencia | | 0.27 kg de más |

</td>
<td valign="top">

#### S6.2 · Requisito para la etapa de carcasa

Este resultado **no descarta el acero**. Deja un objetivo concreto:

> La estructura del motor debe pesar **2.92 kg o menos**.

**Si no se logra, hay tres salidas:**

1. Aligerar el resto del cohete (fuselaje, aletas, recuperación).
2. Aceptar un apogeo menor que 1000 m.
3. Cambiar a un material más liviano (ejemplo 2: aluminio).

</td>
</tr>
</table>

> **Resultado del paso 6:** con $\zeta$ = 0.40 el presupuesto **no cierra** (sobran 0.27 kg). La estructura del motor debe pesar **2.92 kg o menos**.
>
> **Con este resultado →** el material ya dejó su requisito. Los pasos 8 a 12 diseñan la geometría del grano, que no depende del material.

---

## Paso 8 — Geometría de un segmento BATES

**Pregunta:** ¿cómo se describe un segmento BATES y cómo cambia su forma mientras quema?

**Viene de:** las ecuaciones del paso 8 de [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).

**Qué se obtiene:** las ecuaciones del área que quema, del volumen y del alma, en función de las medidas del grano.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### Variables

| Símbolo | Nombre | Unidad |
|---|---|---|
| $D$ | Diámetro exterior del grano | mm |
| $d_0$ | Diámetro inicial del núcleo (el hueco central) | mm |
| $L_0$ | Largo inicial de un segmento | mm |
| $N$ | Número de segmentos | — |
| $k$ | Fracción del núcleo: $d_0/D$ | — |
| $x$ | Espesor ya quemado desde el encendido | mm |
| $w$ | Alma (*web*): espesor total que hay que quemar | mm |
| $A_b$ | Área de quemado: superficie que está ardiendo | mm² |
| $V_{seg}$ | Volumen de propelente de un segmento | cm³ |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

#### 1. Cómo quema un segmento

Cada segmento es un cilindro con un hueco en el centro. Quema por tres superficies:

- **El núcleo:** la cara interior del hueco.
- **Las dos caras planas:** los anillos de cada extremo.

La superficie exterior **no quema**, porque está cubierta por el liner.

Cuando se ha quemado un espesor $x$, el núcleo se agrandó y el segmento se acortó:

$$d(x) = d_0 + 2x \qquad L(x) = L_0 - 2x$$

- $d_0 + 2x$: el núcleo crece $x$ por cada lado del diámetro.
- $L_0 - 2x$: cada cara retrocede $x$, y son dos caras.

#### 2. Área de quemado

Es la suma de la superficie del núcleo y de las dos caras, multiplicada por el número de segmentos:

$$A_b(x) = N\left[\underbrace{\pi\,d\,L}_{\text{núcleo}} + \underbrace{2 \cdot \frac{\pi}{4}\left(D^2 - d^2\right)}_{\text{dos caras}}\right]$$

- **Núcleo:** es un cilindro, así que su área es perímetro ($\pi d$) por largo ($L$).
- **Cada cara:** es un anillo, así que su área es el círculo exterior menos el hueco.

</td>
<td valign="top">

#### S8.1 · Toda la superficie retrocede igual

**Qué se supone.** Que todas las superficies retroceden a la misma velocidad $r$.

**Por qué se acepta.** La presión es casi la misma en toda la cámara y el propelente es homogéneo.

**Qué pasa si no se cumple.** Si el gas que pasa por el núcleo va muy rápido, acelera la combustión en la parte de atrás del motor (**combustión erosiva**). Se controla con el flujo másico $G$, que se revisa en el paso 11.

#### S8.2 · Las caras queman libremente

**Qué se supone.** Que las dos caras de cada segmento están descubiertas y queman.

**Por qué se acepta.** Es lo que define a un grano BATES y lo que permite que su área sea pareja (paso 9).

</td>
</tr>
<tr>
<td valign="top">

#### 3. Volumen de un segmento

Es el área del anillo multiplicada por el largo:

$$V_{seg} = \frac{\pi}{4}\left(D^2 - d_0^2\right) L_0$$

#### 4. Alma

El fuego empieza en el núcleo y avanza hacia la pared exterior. **El alma es la distancia que tiene que recorrer:**

$$w = \frac{D - d_0}{2}$$

Cuando el espesor quemado llega a $x = w$, el núcleo alcanzó la pared y el propelente se acabó.

</td>
<td valign="top">

#### S8.3 · El segmento termina por el alma, no por el largo

**Qué se supone.** Que el propelente se acaba cuando el fuego llega a la pared, y no antes por el lado de las caras.

**Condición para que se cumpla.** El segmento se acorta $2x$, así que debe ser $L_0/2 > w$.

> Se verifica en el paso 11, con las medidas finales.

</td>
</tr>
</table>

> **Resultado del paso 8:** ecuaciones de $A_b(x)$, $V_{seg}$ y $w$ en función de $D$, $d_0$, $L_0$ y $N$.
>
> **Con este resultado →** el paso 9 usa $A_b(x)$ para elegir el largo $L_0$ que hace que el empuje sea parejo.

---

## Paso 9 — Neutralidad: el largo de cada segmento

**Pregunta:** ¿qué largo debe tener cada segmento para que el área que quema, y con ella el empuje, se mantenga pareja?

**Viene de:** la ecuación de $A_b(x)$ del paso 8.

**Qué se obtiene:** una relación entre $L_0$, $D$ y $d_0$.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### 1. Por qué importa que el área sea pareja

El gas que produce el motor es proporcional al área que quema:

$$\dot m = \rho_p\,r\,A_b$$

Si el área sube y baja, la presión y el empuje también lo hacen. Un motor con área pareja se llama **neutro**: tiene presión casi constante, y su carcasa no necesita resistir picos.

#### 2. Los dos efectos que compiten

| Superficie | Qué le pasa al quemar | Efecto en el área |
|---|---|---|
| Núcleo | Se agranda | Aumenta |
| Caras | El anillo se achica y el segmento se acorta | Disminuye |

#### 3. Condición de neutralidad

Se pide que el área al inicio ($x$ = 0) sea igual al área al final ($x = w$). Al final, el núcleo llegó a la pared ($d = D$) y las caras desaparecieron:

$$\underbrace{\pi d_0 L_0 + \frac{\pi}{2}\left(D^2 - d_0^2\right)}_{\text{área al inicio}} = \underbrace{\pi D\left(L_0 - D + d_0\right)}_{\text{área al final}}$$

Despejando $L_0$:

$$\boxed{L_0 = \frac{3D + d_0}{2}}$$

</td>
<td valign="top">

#### S9.1 · Igualar el inicio y el final

**Qué se supone.** Que basta con igualar el área al inicio y al final para que el empuje sea parejo.

**Por qué se acepta.** Es la forma estándar de diseñar un BATES, con una regla sencilla.

**Qué pasa en realidad.** El área no queda perfectamente constante: sube un poco en el medio de la combustión y vuelve a bajar.

> Cuánto varía se calcula en el paso 11, con las medidas finales.

</td>
</tr>
</table>

> **Resultado del paso 9:** $L_0 = (3D + d_0)/2$.
>
> **Con este resultado →** solo faltan $D$ y $d_0$. El paso 10 obtiene la primera condición sobre ellos: el alma que exige el tiempo de combustión.

---

## Paso 10 — Alma requerida por el tiempo de combustión

**Pregunta:** ¿qué espesor de propelente debe tener el grano para quemarse justo en el tiempo que exige la misión?

**Viene de:** $t_{b,dis}$ = 1.36 s (misión común, paso 5) y la ley de Vieille del KNSB (misión común, propelente).

**Qué se obtiene:** el alma $w$ que deben cumplir todas las opciones de geometría.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### Variables

| Símbolo | Nombre | Unidad |
|---|---|---|
| $r$ | Velocidad de regresión: cuánto retrocede la superficie por segundo | mm/s |
| $P$ | Presión de cámara | MPa |
| $a$, $n$ | Coeficiente y exponente de la ley de Vieille | — |
| $t_{b,dis}$ | Tiempo de combustión de diseño | s |
| $w$ | Alma necesaria | mm |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

#### 1. Idea física

La superficie retrocede a una velocidad $r$ y tiene que recorrer el alma $w$. El tiempo que tarda es distancia entre velocidad:

$$t_b = \frac{w}{r}$$

Es como una vela: cuanto más gruesa, más tiempo dura encendida.

#### 2. Por qué aquí se despeja el alma

El tiempo **ya está decidido**. La cadena es:

1. Para salir del riel a 30 m/s hace falta un empuje de 1600 N (misión común, paso 3).
2. Con ese empuje, el impulso de 2172 N·s se entrega en 1.36 s (misión común, paso 5).
3. Entonces el grano debe quemarse en 1.36 s, y lo que queda por decidir es su espesor:

$$\boxed{w = r \cdot t_{b,dis}}$$

#### 3. Velocidad de regresión

Con la ley de Vieille del KNSB a 2.5 MPa, dentro de la meseta:

$$r = a\,P^{\,n} = 7.852 \times 2.5^{-0.013} = 7.76\ \text{mm/s}$$

#### 4. Cálculo

$$w = 7.76\ \tfrac{\text{mm}}{\text{s}} \times 1.36\ \text{s} = 10.53\ \text{mm}$$

Unidades: (mm/s) × s = mm.

</td>
<td valign="top">

#### S10.1 · El motor trabaja dentro de la meseta

**Qué se supone.** Una presión de cámara de 2.5 MPa, dentro de la meseta del KNSB (1.5 a 3.8 MPa).

**Por qué se acepta.** La presión real todavía no se conoce: depende del área de quemado y de la garganta de la tobera. En la meseta, la velocidad de regresión casi no cambia con la presión.

##### Sensibilidad

Se repite el cálculo en los dos extremos de la meseta y en el valor supuesto:

| Presión | $r$ | Alma $w$ |
|---|---|---|
| 1.5 MPa | 7.72 mm/s | 10.47 mm |
| **2.5 MPa** | **7.76 mm/s** | **10.53 mm** |
| 3.79 MPa | 7.72 mm/s | 10.47 mm |

> En toda la meseta el alma cambia **menos de 0.1 mm**: el resultado casi no depende de la presión.

A 1.5 MPa se usa el tramo anterior de la tabla de Vieille ($a$ = 8.763, $n$ = −0.314), que da casi lo mismo.

**Qué pasa si no se cumple.** Si la presión sale de la meseta, $r$ cambia mucho y el tiempo de combustión también. El modelo de cámara debe comprobarlo.

</td>
</tr>
<tr>
<td valign="top">

#### 5. Consecuencia para la forma del grano

Hay que acomodar **1217 cm³** de propelente con solo **10.5 mm** de espesor. Es como envolver mucho volumen en una capa delgada.

Por eso el grano tiene que ser:

- un **tubo de pared delgada**, con un núcleo grande,
- repartido en **varios segmentos**.

</td>
<td valign="top">

#### S10.2 · Por qué el diseño anterior ya no sirve

En la versión anterior de este ejemplo, el BATES tenía 16.7 mm de alma.

| | Diseño anterior | Requisito actual |
|---|---|---|
| Alma | 16.7 mm | 10.5 mm |
| Tiempo de combustión | 16.7 / 7.76 = 2.15 s | 1.36 s |
| Empuje medio aproximado | ≈ 1000 N | 1600 N |

Con ≈ 1000 N el cohete no sale del riel a 30 m/s.

</td>
</tr>
</table>

> **Resultado del paso 10:** el grano debe tener un alma de **w = 10.5 mm**.
>
> **Con este resultado →** el paso 11 combina el alma con el volumen de propelente para elegir el núcleo, el diámetro y el número de segmentos.

---

## Paso 11 — Núcleo, diámetro y número de segmentos

**Pregunta:** ¿qué combinación de diámetro, núcleo y número de segmentos tiene un alma de 10.5 mm y suma 1217 cm³ de propelente?

**Viene de:** $w$ = 10.53 mm (paso 10), $L_0 = (3D + d_0)/2$ (paso 9), la ecuación de $V_{seg}$ (paso 8) y $V_p$ = 1217 cm³ (misión común, paso 7).

**Qué se obtiene:** las medidas finales del grano y sus comprobaciones.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### 1. Del tamaño del núcleo al diámetro

Si el núcleo es una fracción $k$ del diámetro, $d_0 = k\,D$, el alma queda:

$$w = \frac{D - k\,D}{2} = \frac{D\,(1 - k)}{2}$$

Despejando el diámetro:

$$\boxed{D = \frac{2\,w}{1 - k}}$$

- Con un núcleo más grande ($k$ alto), $1 - k$ es pequeño y el diámetro crece, aunque el alma sea la misma.

Con $D$ se calculan en cadena $d_0 = kD$, $L_0 = (3D + d_0)/2$ y $V_{seg}$.

#### 2. Número de segmentos

Es el volumen total dividido entre el volumen de cada segmento (ruta B de [`docs/02_numero_de_granos.md`](../docs/02_numero_de_granos.md)):

$$N = \frac{V_p}{V_{seg}}$$

</td>
<td valign="top">

#### S11.1 · Cambia el orden del cálculo respecto de docs/01

**Qué cambia.** En `docs/01` se elegían $k$ y $N$, y el diámetro salía de la fórmula de raíz cúbica.

**Por qué.** Aquí el alma ya está fijada por el tiempo de combustión (paso 10). Entonces se elige $k$, el diámetro sale del alma y el número de segmentos sale del volumen.

</td>
</tr>
<tr>
<td valign="top">

#### 3. Tabla de opciones

Se evalúan las ecuaciones anteriores para varios valores de $k$, siempre con $w$ = 10.53 mm.

**Ejemplo de una fila** ($k$ = 0.70):

- $D = 2 \times 10.53 / (1 - 0.70) = 70.2$ mm
- $d_0 = 0.70 \times 70.2 = 49.1$ mm
- $L_0 = (3 \times 70.2 + 49.1)/2 = 129.9$ mm
- $V_{seg} = \frac{\pi}{4}(70.2^2 - 49.1^2)(129.9) = 256$ cm³
- $N = 1217 / 256 = 4.75$, que se redondea a 5

| $k$ | $D$ | $d_0$ | $L_0$ | $V_{seg}$ | $N$ | Largo total |
|---|---|---|---|---|---|---|
| 0.50 | 42.1 mm | 21.1 mm | 73.7 mm | 77 cm³ | 15.8 → 16 | 1209 mm |
| 0.60 | 52.7 mm | 31.6 mm | 94.8 mm | 132 cm³ | 9.2 → 10 | 966 mm |
| 0.65 | 60.2 mm | 39.1 mm | 109.8 mm | 180 cm³ | 6.8 → 7 | 781 mm |
| **0.70** | **70.2 mm** | **49.1 mm** | **129.9 mm** | **256 cm³** | **4.8 → 5** | **657 mm** |
| 0.75 | 84.2 mm | 63.2 mm | 158.0 mm | 385 cm³ | 3.2 → 4 | 638 mm |

</td>
<td valign="top">

#### S11.2 · Cómo se elige $k$

**Por qué estos valores.** Se recorre el rango en que un BATES es práctico, de 0.50 a 0.75.

**Qué muestra la tabla:**

- **Núcleo chico ($k$ ≤ 0.60):** con un alma tan delgada salen de 10 a 16 segmentos y más de 1 m de grano. Es difícil de fabricar y de cargar.
- **Núcleo muy grande ($k$ = 0.75):** pocos segmentos, pero un diámetro de 84 mm. Además, con 4 segmentos enteros sobra un 27 % de propelente.
- **$k$ ≈ 0.70:** 5 segmentos de unos 70 mm.

> Se elige **$k$ ≈ 0.70**: es el mejor compromiso entre número de piezas, diámetro y largo.

</td>
</tr>
<tr>
<td valign="top">

#### 4. Ajuste fino a exactamente 5 segmentos

Con $k$ = 0.70 salen 4.75 segmentos. Si se usan 5 enteros sin cambiar nada, sobra un 5 % de propelente. Por eso se ajusta $k$ para que **5 segmentos sumen exactamente $V_p$**:

$$5 \cdot V_{seg}(k) = V_p$$

Esta ecuación no se despeja a mano: se resolvió por tanteo (bisección) con el script.

| Medida | Símbolo | Valor |
|---|---|---|
| Fracción de núcleo | $k$ | 0.693 |
| Diámetro del grano | $D$ | **68.6 mm** |
| Diámetro del núcleo | $d_0$ | **47.6 mm** |
| Largo de cada segmento | $L_0$ | **126.7 mm** |
| Número de segmentos | $N$ | **5** |
| Volumen total | $N \cdot V_{seg}$ | 1217 cm³ |

#### 5. Comprobaciones

| Qué se comprueba | Cálculo | Resultado |
|---|---|---|
| Alma | $(68.6 - 47.6)/2$ | 10.5 mm ✓ |
| Tiempo de combustión | $10.53 / 7.76$ | 1.36 s ✓ |
| Termina por el alma (S8.3) | $L_0/2 = 63.4$ mm $> w$ | ✓ |

</td>
<td valign="top">

#### S11.3 · El ajuste es numérico, no una simulación

**Qué se hizo.** La bisección solo busca el $k$ que cumple una ecuación escrita: prueba un valor, revisa si sobra o falta volumen y corrige.

**Cómo comprobarlo a mano.** Con $D$ = 68.62 mm, $d_0$ = 47.56 mm y $L_0$ = 126.70 mm:

$$V_{seg} = \frac{\pi}{4}\left(68.62^2 - 47.56^2\right)(126.70) = 243.5\ \text{cm}^3$$

> $5 \times 243.5 = 1217$ cm³ ✓

</td>
</tr>
<tr>
<td valign="top">

#### 6. Curva del área de quemado

Se evalúa la ecuación del paso 8 con las medidas finales, en 7 puntos desde el encendido hasta el final del alma:

| Espesor quemado $x$ | Área de quemado $A_b$ |
|---|---|
| 0 mm | 113 864 mm² |
| 1.76 mm | 115 316 mm² |
| 3.51 mm | 116 187 mm² |
| 5.27 mm | **116 477 mm²** (máxima) |
| 7.02 mm | 116 187 mm² |
| 8.78 mm | 115 316 mm² |
| 10.53 mm | 113 864 mm² |

**Qué muestra:**

- Empieza y termina con la misma área, como exige el paso 9.
- Variación máxima: $(116\,477 - 113\,864)/113\,864$ = **2.3 %**. El grano es casi neutro.

#### 7. Control cruzado del propelente quemado por segundo

Se calcula el gasto másico de dos maneras independientes:

| Camino | Cálculo | Resultado |
|---|---|---|
| Por la geometría | $\rho_p\,r\,\bar A_b = 1749 \times 0.00776 \times 0.1156$ | 1.569 kg/s |
| Por la misión | $m_p / t_b = 2.129 / 1.357$ | 1.569 kg/s |

> Los dos caminos coinciden: la geometría es coherente con la misión.

</td>
<td valign="top">

#### S11.4 · Flujo másico en el núcleo (preliminar)

**Qué se revisa.** Todo el gas de los 5 segmentos sale por el núcleo del último. Si va muy rápido, aparece combustión erosiva (S8.1). Se mide con el flujo másico: kilos de gas por segundo y por metro cuadrado de núcleo.

$$G = \frac{\rho_p\,r\,A_{b,max}}{\frac{\pi}{4}d_0^2} = \frac{1749 \times 0.00776 \times 0.1165}{0.001776} \approx 890\ \text{kg/m}^2\text{s}$$

> **890 < 1400 kg/m²s** (límite práctico): cumple con holgura, gracias al núcleo grande.

**Qué se supone.** La velocidad de regresión de la meseta. Por eso el resultado es preliminar y se confirma con el modelo de cámara.

</td>
</tr>
</table>

> **Resultado del paso 11:** **5 segmentos** de $D$ = **68.6 mm**, $d_0$ = **47.6 mm** y $L_0$ = **126.7 mm**. Alma de 10.5 mm, variación de área de 2.3 % y flujo másico de 890 kg/m²s.
>
> **Con este resultado →** el paso 12 calcula las medidas interiores del tubo que debe alojar los 5 segmentos.

---

## Paso 12 — Dimensiones del tubo del motor

**Pregunta:** ¿qué diámetro interior y qué largo debe tener el tubo de la carcasa?

**Viene de:** $D$, $L_0$ y $N$ (paso 11).

**Qué se obtiene:** las medidas interiores mínimas del tubo y la carga volumétrica.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

#### Variables

| Símbolo | Nombre | Unidad |
|---|---|---|
| $D_{int}$ | Diámetro interior del tubo | mm |
| $e_{liner}$ | Espesor del liner: tubo aislante entre el grano y la carcasa | mm |
| $\delta$ | Holgura radial para poder introducir los granos | mm |
| $s$ | Separación entre segmentos | mm |
| $L_{granos}$ | Largo que ocupan los granos dentro del tubo | mm |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

#### 1. Diámetro interior

Al diámetro del grano se suman el liner y la holgura, una vez por cada lado:

$$D_{int} = D + 2\,e_{liner} + 2\,\delta = 68.6 + 2(1.0) + 2(0.25) = 71.1\ \text{mm}$$

#### 2. Largo de los granos

Cinco segmentos con cuatro separaciones entre ellos:

$$L_{granos} = N\,L_0 + (N - 1)\,s = 5(126.7) + 4(2) = 642\ \text{mm}$$

A este largo se suman las tapas y la tobera, que se diseñan en la etapa de carcasa.

#### 3. Carga volumétrica

Indica qué parte del espacio interior ocupa el propelente:

$$\frac{V_p}{\frac{\pi}{4}D^2 L_{granos}} = \frac{1217\ \text{cm}^3}{\frac{\pi}{4}(6.86)^2(64.2)\ \text{cm}^3} \approx 51\ \%$$

</td>
<td valign="top">

#### S12.1 · Liner, holgura y separación

**Qué se supone.**

| Medida | Valor |
|---|---|
| Liner | 1.0 mm |
| Holgura radial | 0.25 mm |
| Separación entre segmentos | 2 mm |

**Por qué se acepta.** Son valores típicos de motores amateur de este tamaño. Se ajustan cuando se elijan el liner y el tubo comercial.

#### S12.2 · La carga volumétrica es baja

Un BATES suele tener entre 70 y 80 %. Este tiene **51 %**: es el precio del alma delgada, porque el núcleo grande deja mucho espacio vacío.

- **Desventaja:** el tubo es más largo y pesado. Con acero, eso aprieta aún más el presupuesto de masa del paso 6.
- **Ventaja:** el núcleo grande mantiene bajo el flujo másico (S11.4).

</td>
</tr>
</table>

> **Resultado del paso 12:** tubo de **71.1 mm** de diámetro interior como mínimo y **642 mm** de largo de granos, más tapas y tobera.
>
> **Con este resultado →** termina la geometría. El siguiente paso es el modelo de cámara: presión, garganta de la tobera y espesor de la carcasa.

---

## Resumen del ejemplo

Grano BATES y carcasa de acero AISI 304. Todos los valores salen de fórmulas escritas en los pasos; ninguno es simulado.

| Magnitud | Valor | Paso |
|---|---|---|
| Fracción de propelente supuesta | $\zeta$ = 0.40 | 6 |
| Margen de masa | **−0.27 kg: no cierra** | 6 |
| Estructura máxima del motor | 2.92 kg | 6 |
| Alma requerida | $w$ = 10.5 mm | 10 |
| Número de segmentos | 5 | 11 |
| Diámetro del grano y del núcleo | 68.6 mm y 47.6 mm | 11 |
| Largo de cada segmento | 126.7 mm | 11 |
| Variación del área de quemado | 2.3 % | 11 |
| Flujo másico (preliminar) | 890 kg/m²s | 11 |
| Diámetro interior del tubo | 71.1 mm como mínimo | 12 |
| Largo de granos | 642 mm | 12 |
| Carga volumétrica | 51 % | 12 |

**Pendiente para la etapa de carcasa:**

1. **Modelo de cámara:** calcular la presión y la garganta de la tobera. Debe confirmar que la presión queda dentro de la meseta (S10.1) y el flujo másico (S11.4).
2. **Espesor de pared:** con $\sigma_y$ = 205 MPa y un factor de seguridad de 1.5 a 2.
3. **Masa real de la estructura:** debe ser 2.92 kg o menos para que el cohete quepa en 10 kg.
