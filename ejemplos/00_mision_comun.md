# Misión común — pasos 1 a 7 (parte común)

Estos pasos **no dependen ni del grano ni del material de la carcasa**: el impulso lo
exigen la masa, el apogeo y el arrastre. Se calculan una vez y los usan los tres
ejemplos.

Ecuaciones: [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).
Cálculo: `python3 scripts/comun.py`.

## Cómo leer este documento

Cada paso es una hoja dividida en dos columnas:

- **Resolución** (izquierda): qué se calcula, con qué ecuación, qué significa cada término y el resultado.
- **Suposición y análisis** (derecha): cada simplificación o dato supuesto en esa fila, por qué se acepta y cuánto cambia el resultado si no se cumple. Solo usa lo calculado hasta ese paso.

Al final de cada paso se indica el **resultado** y qué permite calcular en el **paso siguiente**.

**Secuencia:** Paso 1 (requisitos) → Propelente → Paso 2 (velocidad) → Paso 3 (impulso a mano) → Paso 4 (impulso simulado) → Paso 5 (margen y propelente) → Paso 6 (presupuesto de masa común) → Paso 7 (volumen de propelente)

---

## Paso 1 — Requisitos de la misión

**Pregunta:** ¿qué tiene que cumplir el cohete? Todo lo demás se deriva de estos números.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Valor | Origen |
|---|---|---|---|
| $m_0$ | Masa total al despegue, **incluye el motor cargado** | 10 kg | Equipo |
| $h_{ap}$ | Apogeo objetivo: altura máxima que debe alcanzar | 1000 m | Equipo |
| $D_{cohete}$ | Diámetro exterior del fuselaje | 150 mm | Equipo |
| $(F/W)_{min}$ | Relación empuje/peso mínima al despegue | 5 | Regla práctica |
| $L_{riel}$ | Largo del riel de lanzamiento | 4 m | LASC, regla FLT 4.4.1 |
| $v_{riel,min}$ | Velocidad mínima al salir del riel | 30 m/s | LASC, regla FLT 4.3.4 |

</td>
<td valign="top">

**S1.1 · Requisitos fijos**

Estos valores no se calculan: los fija el equipo o la competencia.

- **Equipo:** $m_0$, $h_{ap}$ y $D_{cohete}$. Si cambian, se rehace toda la cadena.
- **LASC, riel:** para apogeos de 1500 m o menos, la competencia entrega un riel de **4 m** de aluminio con sección de 40 × 40 mm (reglas FLT 4.4.1 y 4.4.3).
- **LASC, velocidad de salida:** sin análisis detallado, el cohete debe salir del riel a **30 m/s** o más (regla FLT 4.3.4). Con simulación o vuelos de prueba se puede justificar un valor menor, pero nunca por debajo de 15 m/s.

> Se adopta 30 m/s, el valor que LASC acepta sin análisis adicional.

</td>
</tr>
<tr>
<td valign="top">

**Qué implica cada requisito**

- $m_0$ = 10 kg **con el motor incluido**: el motor compite por masa con el resto del cohete. Un motor más pesado deja menos masa para fuselaje, recuperación y aviónica.
- $h_{ap}$ = 1000 m: fija la energía que hay que darle al cohete.
- $D_{cohete}$ = 150 mm: fija el **área frontal** y, con ella, el arrastre. También limita el diámetro máximo del motor.
- $L_{riel}$ = 4 m: es la distancia disponible para que el cohete gane velocidad antes de quedar libre.

**Relación empuje/peso mínima**

$$\bar F \ge (F/W)_{min}\; m_0\, g = 5 \times 10 \times 9.81 = 490\ \text{N}$$

- $\bar F$: empuje medio del motor.
- $m_0 g$: peso del cohete al despegue, 98.1 N.
- $F/W$: cuántas veces el empuje supera al peso. Con $F/W$ = 1 el cohete flota; con 5 acelera a $(5-1)\,g = 4g$.

</td>
<td valign="top">

**S1.2 · La regla de $F/W \ge 5$**

Es una regla práctica de cohetería amateur, no una ley física. Lo que realmente importa es que el cohete **salga del riel con velocidad suficiente** para que las aletas lo estabilicen.

- Ese criterio usa el largo del riel (4 m) y la velocidad mínima de LASC (30 m/s).
- Se aplica en el paso 3, cuando se elige el empuje, y resulta más exigente que $F/W \ge 5$.

**S1.3 · Por qué el diámetro de 150 mm importa**

El aire frena al cohete en proporción al área que empuja de frente: $A = \pi D^2/4$.

| Diámetro | Área frontal |
|---|---|
| 100 mm | 0.0079 m² (79 cm²) |
| **150 mm** | **0.0177 m² (177 cm²)** |

> 177 / 79 = 2.25: a la misma velocidad, un cohete de 150 mm tiene 2.25 veces más arrastre que uno de 100 mm.

</td>
</tr>
</table>

> **Resultado del paso 1:** $m_0$ = 10 kg, $h_{ap}$ = 1000 m, $D_{cohete}$ = 150 mm, riel de 4 m, salida del riel a 30 m/s o más.
>
> **Con este resultado →** sabemos **qué** hay que lograr. Antes de calcular cuánto impulso hace falta, se fija **con qué** propelente se va a lograr, porque su $I_{sp}$ entra en los cálculos siguientes.

---

## Propelente — KNSB (65 % KNO₃ / 35 % sorbitol)

**Pregunta:** ¿qué propiedades del propelente entran en la cadena de cálculo, y de dónde salen?

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Valor | Origen |
|---|---|---|---|
| $I_{sp}$ | Impulso específico | 104 s | Modelo termoquímico previo |
| $\rho_{ideal}$ | Densidad teórica: mezcla sin burbujas | 1841 kg/m³ | Cálculo teórico |
| $\rho_p$ | Densidad real del grano colado | 1749 kg/m³ | 95 % del ideal |
| $r$ | Velocidad de regresión: cuántos mm por segundo retrocede la superficie que quema | — | Ley de Vieille |
| $a$, $n$ | Coeficiente y exponente de presión de la ley de Vieille | tabla | R. Nakka |
| $P$ | Presión de la cámara de combustión | — | — |

</td>
<td valign="top">

*Fila de definiciones; las suposiciones de cada valor están en las filas siguientes.*

</td>
</tr>
<tr>
<td valign="top">

**Impulso específico**

$$I_{sp} = \frac{F}{\dot m\, g_0}$$

- $F$: empuje.
- $\dot m$: kg de propelente quemados por segundo.
- $g_0$ = 9.80665 m/s²: gravedad estándar. Se usa por definición, para que $I_{sp}$ quede en segundos.

Es la "eficiencia" del propelente: a mayor $I_{sp}$, menos masa para el mismo impulso.

</td>
<td valign="top">

**SP.1 · $I_{sp}$ = 104 s**

Sale del modelo termoquímico del motor de 38 mm de los apuntes, que trabajaba a baja presión y con una tobera pequeña.

- **Por qué se acepta:** es un valor bajo, así que si el motor real rinde más, sobra propelente. Es el lado seguro para llegar al apogeo.
- **Qué significa en números:** cada kg de propelente entrega $I_{sp}\,g_0$ de impulso.

| $I_{sp}$ | Impulso por kg |
|---|---|
| 95 s | 932 N·s |
| **104 s** | **1020 N·s** |
| 120 s | 1177 N·s |

</td>
</tr>
<tr>
<td valign="top">

**Densidad**

$$\rho_p = 0.95\,\rho_{ideal} = 0.95 \times 1841 = 1749\ \text{kg/m}^3$$

Al colar el propelente fundido quedan burbujas de aire atrapadas. Por eso el grano real es menos denso que la mezcla teórica.

</td>
<td valign="top">

**SP.2 · Densidad del 95 %**

El 95 % es un valor supuesto. La densidad real depende de cómo se cuele el propelente: temperatura, uso de vacío, vibración.

- **Cómo obtener el valor real:** pesar y medir granos de prueba.
- **Efecto si es menor:** con 90 % ($\rho_p$ = 1657 kg/m³), la misma masa ocupa un 5.6 % más de volumen y el motor resulta más largo.

</td>
</tr>
<tr>
<td valign="top">

**Velocidad de regresión: ley de Vieille**

$$r = a\,P^{\,n}$$

- $r$: velocidad a la que retrocede la superficie que quema [mm/s].
- $P$: presión de cámara [MPa]. A más presión, la llama se acerca a la superficie y la calienta más.
- $a$, $n$: constantes que se miden para cada propelente. Cambian según el rango de presión.

| P [MPa] | a [mm/s·MPaⁿ] | n |
|---|---|---|
| 0.10–0.81 | 10.708 | 0.625 |
| 0.81–1.50 | 8.763 | −0.314 |
| **1.50–3.79** | **7.852** | **−0.013** |
| 3.79–7.03 | 3.907 | 0.535 |
| 7.03–10.67 | 9.653 | 0.064 |

**Ejemplo de uso** a 2.5 MPa (dentro del tramo resaltado):

$$r = 7.852 \times 2.5^{-0.013} = 7.852 \times 0.988 = 7.76\ \text{mm/s}$$

</td>
<td valign="top">

**SP.3 · De dónde salen estos valores**

La tabla reproduce los coeficientes publicados por **Richard Nakka** para KNSB, obtenidos con mediciones experimentales ("Values of a and n for various pressure regimes, KNSB", sitio nakka-rocketry.net, página de *burn rate*).

- **Pendiente de verificar:** los valores los escribí de memoria. Desde esta sesión no pude abrir esa página. Hay que cotejarlos antes de usarlos.
- **El cálculo de 7.76 mm/s** es propio: es aplicar la fórmula con los valores del tramo.

**SP.4 · La "meseta" y por qué conviene**

En el tramo de 1.5 a 3.8 MPa el exponente es $n \approx 0$, así que $P^n \approx 1$: la velocidad casi **no depende de la presión**. A eso se le llama meseta.

- **Ventaja:** si la presión sube por algún motivo, la combustión no se acelera. El motor es más estable.
- **Supuesto:** el motor va a trabajar dentro de ese tramo. Todavía no se puede comprobar, porque la presión depende del diseño del motor.
- **Límite:** los datos son de un propelente de laboratorio. El del equipo puede diferir por pureza, tamaño de partícula o humedad. Lo correcto es medir $r$ con el propelente propio.

</td>
</tr>
</table>

> **Resultado:** $I_{sp}$ = 104 s, $\rho_p$ = 1749 kg/m³, $r \approx$ 7.76 mm/s en la meseta.
>
> **Con este resultado →** ya tenemos todos los datos de entrada. El paso 2 empieza a responder **cuánto impulso** necesita la misión, comenzando por la velocidad.

---

## Paso 2 — Velocidad necesaria al apagarse el motor

**Pregunta:** ¿a qué velocidad debe ir el cohete en el instante en que se apaga el motor para que, subiendo solo por inercia, llegue a 1000 m?

**Viene del paso 1:** el apogeo $h_{ap} = 1000$ m.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $v_b$ | Velocidad de apagado (*burnout*): velocidad cuando el motor deja de empujar | m/s |
| $h_b$ | Altura de apagado: altura alcanzada mientras el motor funcionaba | m |
| $h_{ap}$ | Apogeo: altura máxima, donde la velocidad vertical es cero | m |
| $g$ | Aceleración de la gravedad, 9.81 | m/s² |
| $m$ | Masa del cohete después del apagado | kg |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Idea física: conservación de la energía**

Después del apagado, la única fuerza sobre el cohete es su peso. El peso es una fuerza **conservativa**: la energía que el cohete pierde en velocidad la gana en altura, sin pérdidas. Igualamos la energía en el apagado con la energía en el apogeo:

$$\underbrace{\tfrac{1}{2}\,m\,v_b^2}_{\text{cinética}} + \underbrace{m\,g\,h_b}_{\text{potencial}} = \underbrace{m\,g\,h_{ap}}_{\text{en el apogeo}}$$

- $\tfrac{1}{2} m v_b^2$: energía de movimiento en el apagado. Crece con el cuadrado de la velocidad: ir al doble de rápido da cuatro veces más energía.
- $m g h_b$: energía por la altura ya ganada durante la combustión.
- $m g h_{ap}$: energía en el apogeo. Allí la velocidad es cero, así que toda la energía es de altura.

La masa $m$ aparece en los tres términos y se cancela. Despejando:

$$v_b = \sqrt{2\,g\,(h_{ap} - h_b)}$$

</td>
<td valign="top">

**S2.1 · Sin aire**

Para que la energía se conserve, el peso tiene que ser la única fuerza. Por eso se supone que no hay aire.

- **Efecto:** con aire, parte de la energía se pierde al frenar contra el aire. El cohete real debe apagarse **más rápido** que lo calculado: este resultado es una **cota inferior**.
- **¿Se puede despreciar el aire?** Estimación rápida del arrastre a 140 m/s, con un coeficiente típico $C_d \approx 0.5$, aire a nivel del mar (1.225 kg/m³) y el área del paso 1:

$$F_D \approx \tfrac12 \rho v^2 C_d A = \tfrac12 (1.225)(140)^2(0.5)(0.0177) \approx 106\ \text{N}$$

> 106 N es del mismo orden que el peso del cohete (98 N): el aire **no** se puede despreciar.

**S2.2 · La masa se cancela**

Sin aire, un cohete de 1 kg y uno de 100 kg necesitan la misma velocidad. Con aire ya no: el arrastre es una fuerza, y frena más a un cohete liviano que a uno pesado.

</td>
</tr>
<tr>
<td valign="top">

**Sustitución numérica**

Con $h_b \approx 0$ (ver S2.3):

$$v_b = \sqrt{2 \times 9.81 \times 1000} = \sqrt{19\,620} \approx 140\ \text{m/s}$$

Unidades: $\sqrt{(\text{m/s}^2)\cdot\text{m}} = \sqrt{\text{m}^2/\text{s}^2} = \text{m/s}$. La ecuación es dimensionalmente coherente.

</td>
<td valign="top">

**S2.3 · Apagado a ras del suelo ($h_b \approx 0$)**

La altura que gana el cohete mientras quema depende del motor, que todavía no conocemos. Por eso se toma como cero.

- **Efecto:** en realidad el cohete sube mientras quema, así que necesita **menos** velocidad. Este supuesto **sobrestima** $v_b$.
- **Sensibilidad:**

| $h_b$ | $v_b$ |
|---|---|
| 0 m | 140 m/s |
| 100 m | 133 m/s |
| 200 m | 125 m/s |

Los supuestos S2.1 y S2.3 empujan el resultado en sentidos opuestos.

**S2.4 · Gravedad constante**

La gravedad disminuye con la altura: $g(h) = g_0\,[R/(R+h)]^2$, con $R$ = 6371 km.

> A 1000 m, $g$ = 0.9997 $g_0$: el efecto es despreciable (0.03 %).

</td>
</tr>
</table>

> **Resultado del paso 2:** $v_b \approx$ **140 m/s** (cota inferior, sin aire).
>
> **Con este resultado →** ya sabemos qué velocidad hay que alcanzar. El paso 3 usa $v_b$ para calcular **cuánto impulso** necesita el motor para darle esa velocidad a 10 kg mientras vence la gravedad.

---

## Paso 3 — Impulso estimado a mano

**Pregunta:** ¿qué impulso total debe entregar el motor para llevar 10 kg hasta 140 m/s, sabiendo que mientras empuja la gravedad tira hacia abajo?

**Viene de:** $v_b$ = 140 m/s (paso 2); $m_0$ = 10 kg, riel de 4 m y salida a 30 m/s (paso 1).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $p$ | Cantidad de movimiento: masa × velocidad | kg·m/s |
| $I$ | Impulso total: el "empujón" acumulado del motor | N·s |
| $F(t)$ | Empuje del motor en cada instante $t$ | N |
| $\bar F$ | Empuje medio durante la combustión | N |
| $t_b$ | Tiempo de combustión (*burn time*) | s |
| $m_0$ | Masa al despegue | kg |
| $v_b$ | Velocidad de apagado (del paso 2) | m/s |
| $L_{riel}$ | Largo del riel de lanzamiento | m |
| $L_{ef}$ | Recorrido guiado efectivo: distancia que el cohete avanza hasta soltarse del riel | m |
| $v_{riel}$ | Velocidad del cohete al salir del riel | m/s |
| $F_{riel}$ | Empuje del motor mientras el cohete está en el riel | N |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Qué es el impulso y de dónde sale la integral**

La 2ª ley de Newton, escrita en su forma general, dice que una fuerza cambia la cantidad de movimiento $p = m\,v$:

$$F = \frac{dp}{dt}$$

Si se multiplican ambos lados por un intervalo de tiempo muy pequeño $dt$:

$$dp = F\,dt$$

Esto se lee así: **durante un instante $dt$, una fuerza $F$ cambia la cantidad de movimiento en $F\,dt$.**

El empuje de un motor no es constante: sube al encender, se mantiene y baja al final. Para saber el efecto total se suman todos esos pequeños aportes $F\,dt$, desde el encendido ($t$ = 0) hasta el apagado ($t = t_b$). Esa suma es una integral, y su resultado se llama **impulso**:

$$I = \int_0^{t_b} F(t)\,dt$$

- **Gráficamente:** si se dibuja el empuje contra el tiempo, $F\,dt$ es un rectángulo muy delgado de altura $F$ y ancho $dt$. La integral suma todos los rectángulos, es decir, es el **área bajo la curva de empuje**.
- **Unidades:** N·s, que equivale a kg·m/s, las mismas unidades que la cantidad de movimiento.

**Ejemplo:** un motor que empuja 1000 N durante el primer segundo y 600 N durante el segundo siguiente entrega

$$I = 1000 \times 1 + 600 \times 1 = 1600\ \text{N·s}$$

</td>
<td valign="top">

*Definición exacta: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Empuje medio: qué es y por qué $t_b = I/\bar F$**

El **empuje medio** $\bar F$ es el empuje **constante** que, actuando durante el mismo tiempo $t_b$, daría el mismo impulso que el empuje real.

En el ejemplo anterior, el motor da 1600 N·s en 2 s. Un motor que empujara **siempre** 800 N durante 2 s daría lo mismo: $800 \times 2 = 1600$ N·s. Entonces su empuje medio es 800 N:

$$\bar F = \frac{I}{t_b} = \frac{1600\ \text{N·s}}{2\ \text{s}} = 800\ \text{N}$$

En general, por definición:

$$\bar F = \frac{I}{t_b} \quad\Longleftrightarrow\quad I = \bar F\,t_b \quad\Longleftrightarrow\quad t_b = \frac{I}{\bar F}$$

Las tres formas dicen lo mismo. La última responde: **si sé cuánto impulso necesito y con qué empuje medio lo entrego, ¿cuánto tiempo tiene que quemar el motor?**

Es la misma idea que un viaje en carro: para recorrer 160 km a una velocidad media de 80 km/h se tardan 160 / 80 = 2 h.

</td>
<td valign="top">

*Definición exacta: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Idea física: el impulso contra la gravedad**

Mientras el motor funciona, sobre el cohete actúan dos fuerzas: el empuje $F(t)$ hacia arriba y el peso $m_0 g$ hacia abajo. La fuerza neta es la que cambia la cantidad de movimiento:

$$F(t) - m_0\,g = \frac{d(m_0\,v)}{dt}$$

Se integran los dos lados desde el despegue ($t$ = 0, $v$ = 0) hasta el apagado ($t = t_b$, $v = v_b$):

$$\int_0^{t_b} F\,dt \;-\; m_0\,g\,t_b \;=\; m_0\,v_b - 0$$

La primera integral es el impulso $I$. La segunda es sencilla porque el peso es constante: $m_0 g$ por el tiempo $t_b$. Queda:

$$\underbrace{I}_{\text{impulso del motor}} - \underbrace{m_0\,g\,t_b}_{\text{lo que quita la gravedad}} = \underbrace{m_0\,v_b}_{\text{cantidad de movimiento final}}$$

- $I$: todo lo que empuja el motor.
- $m_0 g t_b$: **pérdida por gravedad**. Mientras quema, parte del empuje solo sirve para sostener el peso del cohete. Cuanto más dura la combustión, más impulso se gasta en eso.
- $m_0 v_b$: lo que realmente queda como movimiento: el cohete sale a $v_b$.

</td>
<td valign="top">

**S3.1 · La masa se toma constante (10 kg)**

Mientras el motor quema, el propelente sale por la tobera y **el cohete se aliviana**. Para poder hacer la integral a mano se supone que la masa vale siempre $m_0$ = 10 kg.

- **Efecto:** con 10 kg todo el tiempo, el cohete parece más pesado de lo que es en promedio. La ecuación pide **más impulso del necesario**: sobrestima.
- **Cuánto:** se calcula al final de este paso (S3.5).

**S3.2 · Hereda dos supuestos del paso 2**

Este paso usa $v_b$ = 140 m/s, que se calculó sin aire y con $h_b \approx 0$.

- **Sin aire:** falta la fuerza que frena al cohete. La ecuación pide **menos impulso del real**: subestima.
- **$h_b \approx 0$:** la velocidad de 140 m/s es algo mayor que la realmente necesaria. La ecuación pide **más impulso**: sobrestima.

</td>
</tr>
<tr>
<td valign="top">

**Despeje del impulso**

La ecuación tiene dos incógnitas, $I$ y $t_b$. Con la relación del empuje medio, $t_b = I/\bar F$, queda una sola si se elige $\bar F$. Se reemplaza $t_b$:

$$I - m_0 g\,\frac{I}{\bar F} = m_0 v_b$$

Se saca $I$ como factor común:

$$I\left(1 - \frac{m_0 g}{\bar F}\right) = m_0 v_b$$

Y se divide entre el paréntesis:

$$\boxed{I = \frac{m_0\,v_b}{1 - \dfrac{m_0\,g}{\bar F}}}$$

- $m_0 g/\bar F$: fracción del empuje que se gasta en sostener el peso. Es el inverso de la relación empuje/peso.
- $1 - m_0 g/\bar F$: fracción del empuje que **sí acelera** al cohete.

**Lectura física:** si el empuje apenas iguala al peso ($\bar F \to m_0 g$), el denominador tiende a cero y el impulso necesario a infinito. Un motor así gasta todo en sostener el cohete y nunca lo acelera.

</td>
<td valign="top">

**S3.3 · Para qué sirve este cálculo a mano**

Da un **orden de magnitud** con cuentas sencillas.

- Sirve de referencia: cualquier cálculo más detallado que se haga después tiene que dar un valor parecido. Si no, hay un error.
- Muestra la física del problema: el impulso tiene una parte que acelera y otra que se pierde contra la gravedad.

</td>
</tr>
<tr>
<td valign="top">

**Elección del empuje medio: criterio del riel**

Mientras el cohete está en el riel, el riel lo guía. Al salir, lo estabilizan las **aletas**, y las aletas solo funcionan si el aire pasa con suficiente velocidad. Por eso se exige una velocidad mínima al salir del riel.

**Cuándo se considera que sale del riel.** Según LASC, en el instante en que se suelta la última guía (*rail button*) que está **delante del centro de gravedad**. Como esa guía va a cierta altura sobre la cola del cohete, el recorrido guiado $L_{ef}$ es menor que el largo del riel.

Con aceleración constante $a$ a lo largo del recorrido (cinemática):

$$v_{riel}^2 = 2\,a\,L_{ef}$$

La aceleración neta es el empuje menos el peso, dividido por la masa:

$$a = \frac{F_{riel}}{m_0} - g$$

Juntando y despejando el empuje:

$$F_{riel,min} = m_0\left(\frac{v_{riel}^2}{2\,L_{ef}} + g\right)$$

- $v_{riel}^2/(2L_{ef})$: aceleración necesaria para llegar a $v_{riel}$ en el recorrido guiado.
- $+\,g$: aceleración extra para vencer el peso.

Con $v_{riel}$ = 30 m/s (LASC):

| Recorrido guiado $L_{ef}$ | $F_{riel,min}$ |
|---|---|
| 4.0 m (todo el riel) | 1223 N |
| 3.5 m | 1384 N |
| **3.2 m** | **1504 N** |
| 3.0 m | 1598 N |

Se toma $L_{ef}$ = 3.2 m (guía delantera a ≈0.8 m de la cola) y se elige $F_{riel}$ = **1600 N**. Con ese empuje:

$$v_{riel} = \sqrt{2 \times 3.2 \times \left(\frac{1600}{10} - 9.81\right)} = \sqrt{961} \approx 31.0\ \text{m/s} \;\ge 30\ \text{m/s}$$

El cohete tarda $t = 2L_{ef}/v_{riel} = 6.4/31.0 \approx 0.21$ s en recorrer el riel.

Suponiendo empuje constante, el empuje medio es el mismo: $\bar F = F_{riel}$ = 1600 N ($F/W \approx 16$).

</td>
<td valign="top">

**S3.4 · El empuje de 1600 N y el recorrido de 3.2 m**

Son dos supuestos ligados.

- **Recorrido guiado de 3.2 m:** depende de dónde quede el centro de gravedad y de dónde se ponga la guía delantera, que todavía no están definidos. Si la guía va más arriba, el recorrido es menor y hace falta más empuje (ver la tabla).
- **Lo que exige LASC es el empuje en el riel**, durante los primeros ≈0.2 s. Un motor con un empuje inicial alto podría cumplir con un empuje medio menor. Aquí, al suponer empuje constante, ambos coinciden.
- **El empuje real no se elige libremente:** sale de la geometría del grano y de la presión, que todavía no están diseñadas. El motor final tendrá que cumplir $F_{riel} \ge F_{riel,min}$.

> Consecuencia: con 1600 N, el impulso de ≈1500 N·s se entrega en menos de 1 s. La salida a 30 m/s obliga a un motor de **empuje alto y combustión corta**.

**Cuánto cambia el impulso según el empuje**

| $\bar F$ | $I$ | $t_b$ | Pérdida por gravedad $m_0 g\,t_b$ |
|---|---|---|---|
| 1200 N | 1525 N·s | 1.27 s | 125 N·s |
| 1600 N | 1491 N·s | 0.93 s | 91 N·s |
| 2400 N | 1460 N·s | 0.61 s | 60 N·s |

Pasar de 1200 a 2400 N reduce el impulso necesario en:

$$\frac{1525 - 1460}{1525} = \frac{65}{1525} = 0.043 \approx 4\ \%$$

**Por qué pasa:** el impulso que se gasta en sostener el peso es $m_0 g\,t_b$. Un motor más fuerte entrega su impulso **en menos tiempo**: con 2400 N quema 0.61 s en vez de 1.27 s, así que pasa menos tiempo "peleando" contra la gravedad y pierde 60 N·s en vez de 125 N·s. La parte útil, $m_0 v_b$ = 1400 N·s, es la misma en los tres casos.

</td>
</tr>
<tr>
<td valign="top">

**Sustitución numérica**

$$I = \frac{10 \times 140}{1 - \dfrac{10 \times 9.81}{1600}} = \frac{1400}{1 - 0.061} = \frac{1400}{0.939} \approx 1491\ \text{N·s}$$

$$t_b = \frac{I}{\bar F} = \frac{1491}{1600} \approx 0.93\ \text{s}$$

Unidades: kg·m/s = N·s, porque 1 N = 1 kg·m/s².

</td>
<td valign="top">

**S3.5 · Corrección por la masa que disminuye**

El resultado de 1491 N·s supone que el cohete pesa 10 kg todo el tiempo (S3.1). Con ese mismo resultado se puede estimar cuánto se aliviana.

**1. Propelente quemado.** Como $I_{sp} = F/(\dot m\, g_0)$, integrando en el tiempo queda $I = m_p\,I_{sp}\,g_0$. Entonces:

$$m_p \approx \frac{1491}{104 \times 9.81} = 1.46\ \text{kg}$$

**2. Masa media.** El cohete pasa de 10 kg a 10 − 1.46 = 8.54 kg. La masa media es (10 + 8.54)/2 = 9.27 kg.

**3. Nuevo impulso** con la masa media:

> $I = 9.27 \times 140 \,/\, (1 - 9.27 \times 9.81/1600)$ = 1376 N·s

**Por qué baja:** con 10 kg se suponía un cohete más pesado que el real. Hacía falta más impulso para acelerarlo y también más para sostener su peso. Con la masa media, las dos partes bajan y el impulso cae un 8 %.

Por eso el resultado de este paso se da como un **rango**: 1491 N·s con masa constante y 1376 N·s con masa media.

</td>
</tr>
</table>

> **Resultado del paso 3:** $I \approx$ **1376 a 1491 N·s** (unos 1400 N·s), con $\bar F$ = 1600 N y $t_b \approx$ **0.9 s**. Es un orden de magnitud: no incluye el aire.
>
> **Con este resultado →** sabemos en qué rango está el impulso. El paso 4 agrega lo que aquí se simplificó (aire, masa que disminuye continuamente, altura ganada al quemar) para obtener el **valor de diseño**, y usa este rango para comprobar que el cálculo es coherente.

---

## Paso 4 — Impulso requerido con vuelo simulado

**Pregunta:** ¿qué impulso lleva al cohete **exactamente** a 1000 m, teniendo en cuenta el aire, la masa que disminuye y la altura ganada durante la combustión?

**Viene de:** $m_0$ y $D_{cohete}$ (paso 1), $\bar F$ = 1600 N y el rango de 1376 a 1491 N·s (paso 3), $I_{sp}$ = 104 s (propelente).

Cálculo: `python3 scripts/comun.py`

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $h(t)$ | Altura en el instante $t$ | m |
| $v(t)$ | Velocidad vertical | m/s |
| $m(t)$ | Masa del cohete, que baja al quemar | kg |
| $F_D$ | Fuerza de arrastre aerodinámico (*drag*) | N |
| $\rho(h)$ | Densidad del aire a la altura $h$ | kg/m³ |
| $\rho_0$ | Densidad del aire en el sitio de lanzamiento | kg/m³ |
| $H$ | Altura de escala de la atmósfera, 8500 | m |
| $C_d$ | Coeficiente de arrastre del cohete | — |
| $A_{ref}$ | Área frontal de referencia | m² |
| $I_{sp}$ | Impulso específico del propelente | s |
| $g_0$ | Gravedad estándar, 9.80665 (definición de $I_{sp}$) | m/s² |
| $\dot m$ | Gasto másico: kg de propelente quemados por segundo | kg/s |
| $m_p$ | Masa de propelente | kg |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Ecuación 1: cinemática**

$$\frac{dh}{dt} = v$$

La altura cambia según la velocidad. Es la definición de velocidad.

**Ecuación 2: 2ª ley de Newton con tres fuerzas**

$$m(t)\,\frac{dv}{dt} = \underbrace{F}_{\text{empuje}} - \underbrace{F_D}_{\text{arrastre}} - \underbrace{m(t)\,g}_{\text{peso}}$$

- $m\,dv/dt$: masa por aceleración, es decir, cómo cambia la velocidad en cada instante.
- $F$: empuje del motor. Vale $\bar F$ mientras quema y 0 después.
- $F_D$: arrastre. Siempre se opone al movimiento.
- $m\,g$: peso. Disminuye a medida que se quema el propelente.

</td>
<td valign="top">

**S4.1 · Vuelo vertical**

Se supone que el cohete sube en línea recta.

- **En la práctica:** el riel se inclina unos grados por seguridad y el viento desvía la trayectoria. El apogeo real es algo menor.
- **Cómo se maneja:** no se cuantifica aquí. Es una de las razones para agregar un margen al impulso.

**S4.2 · Empuje constante**

Se supone que el motor empuja siempre $\bar F$ = 1600 N.

- **En la práctica:** el empuje real tiene un arranque, una zona casi constante y una cola.
- **Por qué se acepta:** para el apogeo importa el impulso total, no su forma. Se comprobó variando el empuje:

> $\bar F$ = 1200 / 1600 / 2400 N → $I_{req}$ = 1813 / 1810 / 1805 N·s (menos de 0.5 %).

</td>
</tr>
<tr>
<td valign="top">

**Ecuación 3: la masa disminuye**

$$\frac{dm}{dt} = -\dot m = -\frac{F}{I_{sp}\,g_0} \;\; (t < t_b), \qquad 0 \;\; (t \ge t_b)$$

**De dónde sale:** de la definición de impulso específico, $I_{sp} = F/(\dot m\,g_0)$, despejando $\dot m$. Un propelente con más $I_{sp}$ quema menos masa para el mismo empuje.

Integrando durante toda la combustión:

$$m_p = \frac{I}{I_{sp}\,g_0}$$

</td>
<td valign="top">

**S4.3 · $I_{sp}$ = 104 s**

En este paso, el $I_{sp}$ solo decide qué tan rápido se aliviana el cohete.

> Con $I_{sp}$ = 120 s, $I_{req}$ = 1818 N·s (+0.5 %): efecto pequeño.

Donde sí influye mucho es en la masa de propelente, $m_p = I/(I_{sp}\,g_0)$.

</td>
</tr>
<tr>
<td valign="top">

**El arrastre y la atmósfera**

$$F_D = \tfrac{1}{2}\,\rho(h)\,v^2 \cdot C_d \cdot A_{ref}$$

- $\tfrac{1}{2}\rho v^2$: **presión dinámica**, la "presión" del aire que choca contra el cohete. Crece con el cuadrado de la velocidad.
- $A_{ref}$: área frontal, $\pi D_{cohete}^2/4 = \pi (0.15)^2/4$ = 0.0177 m².
- $C_d$: qué tan aerodinámica es la forma: cono, aletas, acabado superficial.

En el código se escribe $v\,|v|$ en lugar de $v^2$ para que el arrastre cambie de sentido si el cohete baja.

$$\rho(h) = \rho_0\,e^{-h/H}$$

El aire es menos denso con la altura. La forma exponencial sale del equilibrio hidrostático con temperatura constante.

**Orden de magnitud:** a 181 m/s, $F_D = \tfrac12 (1.225)(181)^2(0.5)(0.0177) \approx$ 177 N, que sobre unos 8 kg frena con ≈2.2 g adicionales.

</td>
<td valign="top">

**S4.4 · $C_d$ = 0.5**

Es un valor típico de cohetes amateur, que suelen estar entre 0.4 y 0.75. Sin túnel de viento ni CFD no se conoce mejor.

- **Cómo se maneja:** se prueban tres valores (tabla de resultados).

> ±20 % en $C_d$ → −6 % / +7 % en $I_{req}$.

**S4.5 · Aire a nivel del mar**

Se usa $\rho_0$ = 1.225 kg/m³, el aire más denso posible: es el caso conservador.

> Desde un sitio alto (~1700 m, $\rho_0 \approx$ 1.0 kg/m³): $I_{req}$ = 1706 N·s (−6 %).

**S4.6 · Atmósfera exponencial**

Es una aproximación de la atmósfera real.

> A 1000 m da 1.089 kg/m³ contra 1.112 de la atmósfera estándar (−2 %): efecto menor.

</td>
</tr>
<tr>
<td valign="top">

**Método de solución**

Las tres ecuaciones están acopladas (la masa cambia la aceleración, la altura cambia el arrastre) y no tienen solución a mano. Se resuelven por pasos de tiempo:

1. **Integración:** desde $h$ = 0, $v$ = 0, $m = m_0$, se avanza en pasos de $\Delta t$ = 1 ms con el método de Euler: con las fuerzas actuales se calcula la aceleración, con ella la nueva velocidad y con esta la nueva altura.
2. **Apogeo:** la simulación se detiene cuando, ya apagado el motor, la velocidad se vuelve negativa. Esa altura es el apogeo.
3. **Bisección:** se busca el $I$ que da 1000 m. Se prueba un valor; si el apogeo queda corto, se aumenta; si se pasa, se reduce. Cada vez se parte el intervalo a la mitad, hasta converger.

Con cada $I$: $t_b = I/\bar F$ y $\dot m = m_p/t_b$.

</td>
<td valign="top">

**S4.7 · ¿Es suficientemente fino el paso de tiempo?**

Un método numérico solo vale si el resultado no depende del paso de tiempo. Se repitió con un paso 5 veces más chico.

> $\Delta t$ = 1 ms → 1809.6 N·s; $\Delta t$ = 0.2 ms → 1809.9 N·s. El resultado no cambia.

**Comprobación con el paso 3**

Se simuló también **sin aire** ($C_d$ = 0) y dio 1346 N·s.

- El paso 3 daba 1376 N·s con masa media. Queda solo un 2 % arriba, porque aún suponía $h_b \approx 0$ (S2.3).
- La simulación y el cálculo a mano coinciden en el orden de magnitud: el código es coherente.

</td>
</tr>
<tr>
<td valign="top">

**Resultados**

| $C_d$ | $I_{req}$ [N·s] | $v_{max}$ [m/s] | $m_p$ [kg] | $t_b$ [s] |
|---|---|---|---|---|
| 0 (sin aire) | 1346 | 136 | 1.32 | 0.84 |
| 0.4 | 1698 | 170 | 1.66 | 1.06 |
| **0.5** | **1810** | **181** | **1.77** | **1.13** |
| 0.6 | 1933 | 192 | 1.90 | 1.21 |

- $I_{req}$: impulso con el que el cohete llega justo a 1000 m (salida de la bisección).
- $v_{max}$: velocidad máxima; ocurre al apagarse el motor.
- $m_p = I_{req}/(I_{sp}\,g_0)$. Ejemplo: 1810 / (104 × 9.80665) = 1.77 kg.
- $t_b = I_{req}/\bar F$. Ejemplo: 1810 / 1600 = 1.13 s.

</td>
<td valign="top">

**Qué enseña la tabla**

- **El aire cuesta +34 %:** sin aire bastan 1346 N·s; con aire hacen falta 1810.
- **Con aire, $v_{max}$ = 181 m/s y no 140:** el aire frena al cohete en la subida libre, así que debe apagarse más rápido. Confirma S2.1.
- **Sin aire, $v_{max}$ = 136 m/s y no 140:** el cohete sube ≈100 m mientras quema y necesita menos velocidad. Confirma S2.3.
- **El supuesto más incierto ($C_d$) mueve poco el resultado:** un error razonable en $C_d$ no compromete el diseño.

</td>
</tr>
</table>

> **Resultado del paso 4:** $I_{req}$ = **1810 N·s** ($C_d$ = 0.5; $v_{max}$ = 181 m/s; $t_b$ = 1.13 s).
>
> **Con este resultado →** tenemos el impulso que la misión **exige**. El paso 5 le suma un **margen de diseño** para cubrir los supuestos de este paso y, con $I_{sp}$, obtiene la **masa de propelente** que debe cargar el motor.

---

## Paso 5 — Margen de diseño y masa de propelente

**Pregunta:** ¿cuánto impulso debe tener realmente el motor, considerando que los supuestos de los pasos anteriores pueden fallar, y cuánto propelente hace falta para darlo?

**Viene de:** $I_{req}$ = 1810 N·s (paso 4) e $I_{sp}$ = 104 s (propelente).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $I_{req}$ | Impulso requerido: el justo para llegar a 1000 m (paso 4) | N·s |
| $\mu$ | Margen de diseño: fracción extra de impulso | — |
| $I_{dis}$ | Impulso de diseño: el que debe entregar el motor | N·s |
| $m_p$ | Masa de propelente | kg |
| $I_{sp}$ | Impulso específico | s |
| $g_0$ | Gravedad estándar, 9.80665 | m/s² |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Margen de diseño**

$$I_{dis} = (1 + \mu)\, I_{req}$$

- $I_{req}$: lo que la misión exige si todos los supuestos se cumplen.
- $(1+\mu)$: factor que agrega impulso para cubrir lo que salga peor de lo previsto.

**Por qué hace falta:** el paso 4 calculó $I_{req}$ con supuestos ($C_d$, vuelo vertical, sin viento, empuje constante). Si el motor se diseñara con exactamente 1810 N·s, cualquier desviación desfavorable dejaría el cohete por debajo de 1000 m.

$$I_{dis} = 1.20 \times 1810 = 2172\ \text{N·s}$$

</td>
<td valign="top">

**S5.1 · Margen del 20 %**

Es una decisión de ingeniería: cuánta incertidumbre se quiere cubrir.

- **Qué cubre:** un $C_d$ peor ($C_d$ = 0.6 exige 1933 N·s, +7 %), la inclinación del riel, el viento y un cohete más pesado de lo previsto.
- **Con qué holgura:** aun en el peor caso calculado, quedan 2172/1933 − 1 = 12 % de margen.
- **Su costo:** más margen exige más propelente y un motor más pesado, lo que aprieta el presupuesto de masa.

</td>
</tr>
<tr>
<td valign="top">

**Masa de propelente**

De la definición de $I_{sp}$, integrada durante toda la combustión:

$$m_p = \frac{I_{dis}}{I_{sp}\, g_0}$$

- $I_{dis}$: impulso total a entregar.
- $I_{sp}\,g_0$: impulso que entrega cada kg de propelente (N·s/kg = m/s). Se llama **velocidad efectiva de escape**: 104 × 9.81 = 1020 m/s.

$$m_p = \frac{2172}{104 \times 9.80665} = \frac{2172}{1020} = 2.129\ \text{kg}$$

Unidades: N·s / (m/s) = (kg·m/s) / (m/s) = kg.

</td>
<td valign="top">

**S5.2 · Qué tanto depende de $I_{sp}$**

La masa de propelente es inversamente proporcional al $I_{sp}$.

| $I_{sp}$ | $m_p$ |
|---|---|
| 95 s | 2.33 kg |
| **104 s** | **2.13 kg** |
| 120 s | 1.85 kg |

> Un error de ±10 % en $I_{sp}$ cambia la masa de propelente ±10 %. Es la incertidumbre más importante de este paso.

</td>
</tr>
<tr>
<td valign="top">

**Clase del motor**

Los motores se clasifican por impulso total. Cada letra duplica el rango de la anterior:

| Clase | Impulso total |
|---|---|
| J | 640–1280 N·s |
| **K** | **1280–2560 N·s** |
| L | 2560–5120 N·s |

Con 2172 N·s el motor es **clase K**.

**Apogeo con el margen:** simulando el vuelo del paso 4 con $I_{dis}$, el cohete llega a **1242 m**. Los 242 m de exceso son el margen expresado en altura.

</td>
<td valign="top">

**S5.3 · Qué implica un motor clase K**

Es un motor de cohetería de **alta potencia**. Antes de volarlo hacen falta:

- pruebas estáticas en banco con distancia de seguridad,
- prueba hidrostática de la carcasa,
- los permisos que exija la normativa local.

</td>
</tr>
</table>

> **Resultado del paso 5:** $I_{dis}$ = **2172 N·s** (clase K), $m_p$ = **2.129 kg** de propelente.
>
> **Con este resultado →** sabemos cuánto propelente lleva el motor. El paso 6 verifica si **cabe en el presupuesto de 10 kg** junto con la estructura del motor y el resto del cohete.

---

## Paso 6 — Presupuesto de masa (parte común)

**Pregunta:** si el propelente pesa 2.129 kg, ¿cuánto puede pesar como máximo la estructura del motor para que el cohete completo no supere los 10 kg?

**Viene de:** $m_0$ = 10 kg (paso 1) y $m_p$ = 2.129 kg (paso 5).

La parte que depende del material de la carcasa ($\zeta$ supuesto y margen final) está en cada ejemplo. Aquí se calcula lo común a los tres.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $m_{resto}$ | Masa de todo lo que no es el motor | kg |
| $m_{motor}$ | Masa del motor completo: propelente + carcasa + tapas + tobera + liner | kg |
| $\zeta$ | Fracción de propelente: $m_p/m_{motor}$ | — |
| $m_{desc}$ | Masa en el descenso (sin propelente) | kg |
| $v_{desc}$ | Velocidad de descenso con paracaídas | m/s |
| $C_{D,par}$ | Coeficiente de arrastre del paracaídas | — |
| $A_{par}$ | Área del paracaídas | m² |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Masa del resto del cohete**

| Componente | Masa |
|---|---|
| Tubo de fuselaje (~1.3 m, fibra de vidrio) | 1.75 kg |
| Cono de nariz | 0.70 kg |
| Aletas | 0.60 kg |
| Soporte del motor | 0.50 kg |
| Recuperación | 0.90 kg |
| Aviónica | 0.50 kg |
| **$m_{resto}$** | **4.95 kg** |

</td>
<td valign="top">

**S6.1 · Masas estimadas, no medidas**

Son valores típicos para un cohete de 150 mm de unos 1.7 m de largo (relación largo/diámetro ≈ 11).

- **Ejemplo de cómo se estimó:** el tubo de fibra de vidrio con 1.5 mm de pared pesa ≈1.33 kg/m.
- **Qué falta:** no incluye carga útil. Se reemplazan por masas reales cuando el equipo de estructuras defina materiales.

</td>
</tr>
<tr>
<td valign="top">

**Verificación del paracaídas**

En el descenso, a velocidad constante, el arrastre del paracaídas iguala al peso:

$$\tfrac{1}{2}\,\rho_0\, v_{desc}^2\, C_{D,par}\, A_{par} = m_{desc}\, g \;\Longrightarrow\; A_{par} = \frac{2\, m_{desc}\, g}{\rho_0\, C_{D,par}\, v_{desc}^2}$$

- Lado izquierdo: arrastre (misma forma que en el paso 4).
- Lado derecho: peso del cohete vacío, $m_{desc} = 10 - 2.129 = 7.87$ kg.

$$A_{par} = \frac{2 \times 7.87 \times 9.81}{1.225 \times 1.5 \times 5.5^2} = 2.78\ \text{m}^2 \;\Rightarrow\; \varnothing = \sqrt{\frac{4 A_{par}}{\pi}} = 1.88\ \text{m}$$

</td>
<td valign="top">

**S6.2 · Descenso a 5.5 m/s**

Es una velocidad de aterrizaje segura habitual. Equivale a dejar caer el cohete desde ≈1.5 m.

| $v_{desc}$ | Diámetro del paracaídas |
|---|---|
| 4.5 m/s | 2.30 m |
| **5.5 m/s** | **1.88 m** |
| 6.5 m/s | 1.59 m |

**S6.3 · $C_{D,par}$ = 1.5 y masa del paracaídas**

- El coeficiente depende del tipo de paracaídas y del área que se tome como referencia. Debe salir del fabricante o de pruebas.
- Se estima que un paracaídas de 1.9 m pesa ≈0.4 kg, así que cabe en los 0.90 kg de recuperación.

</td>
</tr>
<tr>
<td valign="top">

**Fracción de propelente mínima**

La masa total es la suma del motor y del resto. El motor pesa $m_p/\zeta$:

$$m_0 = \frac{m_p}{\zeta} + m_{resto} \quad\Longrightarrow\quad \boxed{\zeta_{min} = \frac{m_p}{m_0 - m_{resto}}}$$

- $m_0 - m_{resto}$: masa máxima disponible para el motor completo.
- $\zeta_{min}$: la menor fracción de propelente que aún cabe en 10 kg.

$$\zeta_{min} = \frac{2.129}{10 - 4.95} = \frac{2.129}{5.05} = 0.422$$

Masa máxima de la estructura del motor: $5.05 - 2.129 = 2.92$ kg.

</td>
<td valign="top">

**S6.4 · Qué tanto depende de $m_{resto}$**

Si el resto del cohete pesa más, queda menos masa para el motor y este tiene que ser más eficiente.

| $m_{resto}$ | $\zeta_{min}$ |
|---|---|
| 4.75 kg | 0.406 |
| **4.95 kg** | **0.422** |
| 5.15 kg | 0.439 |
| 5.45 kg | 0.468 |

> Cada 100 g extra en el resto del cohete suben $\zeta_{min}$ unos 0.008: el motor tiene que ser un 2 % más eficiente en masa.

</td>
</tr>
</table>

> **Resultado del paso 6:** $\zeta_{min}$ = **0.422**. La estructura del motor (carcasa + tapas + tobera + liner) no puede pesar más de **2.92 kg**.
>
> **Con este resultado →** tenemos el límite de masa que cada ejemplo debe respetar según su material. El paso 7 calcula **cuánto espacio** ocupa el propelente, que es el dato con el que empieza la geometría del grano.

---

## Paso 7 — Volumen de propelente

**Pregunta:** ¿cuánto espacio ocupan los 2.129 kg de propelente?

**Viene de:** $m_p$ = 2.129 kg (paso 5) y $\rho_p$ = 1749 kg/m³ (propelente).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $V_p$ | Volumen de propelente | m³ (o cm³) |
| $m_p$ | Masa de propelente | kg |
| $\rho_p$ | Densidad real del grano | kg/m³ |

**Ecuación**

$$V_p = \frac{m_p}{\rho_p} = \frac{2.129\ \text{kg}}{1749\ \text{kg/m}^3} = 1.217 \times 10^{-3}\ \text{m}^3 = 1217\ \text{cm}^3$$

Es la definición de densidad: masa por unidad de volumen. 1217 cm³ es casi lo que cabe en una botella de 1.25 L.

</td>
<td valign="top">

**S7.1 · Hereda la densidad del 95 %**

El volumen depende directamente de la densidad supuesta (SP.2).

> Con 90 %: 1285 cm³ (+5.6 %). Con 98 %: 1180 cm³ (−3 %).

**S7.2 · Es solo el propelente**

El motor ocupa más espacio que esto, porque el grano tiene un núcleo hueco por donde salen los gases. La relación entre ambos (carga volumétrica) depende de la geometría del grano y se calcula en cada ejemplo.

</td>
</tr>
</table>

> **Resultado del paso 7:** $V_p$ = **1217 cm³**.
>
> **Con este resultado →** termina la parte común. Cada ejemplo toma $V_p$ y lo convierte en medidas reales: diámetro del grano, núcleo, largo y número de segmentos (pasos 8 a 12), con su propio material y geometría.

---

## Resumen de la cadena común

| Paso | Resultado | Pasa a |
|---|---|---|
| 1 · Requisitos | $m_0$ = 10 kg, $h_{ap}$ = 1000 m, $D$ = 150 mm, riel de 4 m, salida a 30 m/s | todos |
| Propelente | $I_{sp}$ = 104 s, $\rho_p$ = 1749 kg/m³ | 4, 5, 7 |
| 2 · Velocidad | $v_b \approx$ 140 m/s (cota inferior) | 3 |
| 3 · Impulso a mano | $\bar F$ = 1600 N; $I \approx$ 1376–1491 N·s (orden de magnitud) | 4 |
| 4 · Impulso simulado | $I_{req}$ = 1810 N·s | 5 |
| 5 · Margen | $I_{dis}$ = 2172 N·s, $m_p$ = 2.129 kg | 6, 7 |
| 6 · Masa | $\zeta_{min}$ = 0.422 (estructura ≤ 2.92 kg) | cada ejemplo |
| 7 · Volumen | $V_p$ = 1217 cm³ | cada ejemplo |
