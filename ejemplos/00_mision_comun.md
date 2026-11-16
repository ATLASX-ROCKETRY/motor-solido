# Misión común — pasos 1 a 7 (parte común)

Estos pasos **no dependen ni del grano ni del material de la carcasa**: el impulso lo
exigen la masa, el apogeo y el arrastre. Se calculan una vez y los usan los tres
ejemplos.

Ecuaciones: [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).
Cálculo: `python3 scripts/comun.py`.

## Cómo leer este documento

Cada paso es una hoja dividida en dos columnas:

- **Resolución** (izquierda): qué se calcula, con qué ecuación, qué significa cada término y el resultado.
- **Suposición y análisis** (derecha): cada simplificación o dato supuesto en esa fila, por qué se acepta y cuánto cambia el resultado si no se cumple.

Al final de cada paso se indica el **resultado** y qué permite calcular en el **paso siguiente**.

**Secuencia:** Paso 1 (requisitos) → Propelente → Paso 2 (velocidad) → Paso 3 (impulso a mano) → Paso 4 (impulso simulado) → Paso 5 (margen y propelente) → Paso 6 (presupuesto de masa común) → Paso 7 (volumen de propelente) → cada ejemplo.

---

## Paso 1 — Requisitos de la misión

**Pregunta:** ¿qué tiene que cumplir el cohete? Todo lo demás se deriva de estos números.

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Valor | Unidad |
|---|---|---|---|
| $m_0$ | Masa total al despegue, **incluye el motor cargado** | 10 | kg |
| $h_{ap}$ | Apogeo objetivo: altura máxima que debe alcanzar | 1000 | m |
| $D_{cohete}$ | Diámetro exterior del fuselaje | 150 | mm |
| $(F/W)_{min}$ | Relación empuje/peso mínima al despegue | 5 | — |

</td>
<td valign="top">

**S1.1 · Son decisiones del equipo, no resultados**

$m_0$, $h_{ap}$ y $D_{cohete}$ los fijó el equipo como requisitos de la misión. No tienen una incertidumbre que analizar: si cambian, se rehace toda la cadena.

</td>
</tr>
<tr>
<td valign="top">

**Qué implica cada requisito**

- $m_0$ = 10 kg **con el motor incluido**: el motor compite por masa con el resto del cohete. Un motor más pesado deja menos masa para fuselaje, recuperación y aviónica (paso 6).
- $h_{ap}$ = 1000 m: fija la energía que hay que darle al cohete (paso 2).
- $D_{cohete}$ = 150 mm: fija el **área frontal** y por lo tanto el arrastre (paso 4). También limita el diámetro máximo del motor.

**Relación empuje/peso mínima**

$$\bar F \ge (F/W)_{min}\; m_0\, g = 5 \times 10 \times 9.81 = 490\ \text{N}$$

- $\bar F$: empuje medio del motor.
- $m_0 g$: peso del cohete al despegue, 98.1 N.
- El cociente $F/W$ dice cuántas veces el empuje supera al peso. Con $F/W$ = 1 el cohete flota; con 5 acelera a $(5-1)\,g = 4g$.

</td>
<td valign="top">

**S1.2 · $(F/W)_{min}$ = 5 es una regla práctica**

Es un valor usado en cohetería amateur para salir del riel con velocidad suficiente. El criterio físico más preciso es la **velocidad de salida del riel**, que depende del largo del riel (ver paso 3).

> Con un riel de 2 m y salida a 20 m/s, el mínimo sube a ≈1100 N ($F/W$ ≈ 11). El largo del riel es un dato pendiente.

**S1.3 · Por qué 150 mm importa tanto**

El arrastre crece con el área frontal, que crece con $D^2$. Pasar de 100 a 150 mm multiplica el área por 2.25.

> Con 100 mm el impulso necesario era 1558 N·s; con 150 mm es 1826 N·s (+17 %).

</td>
</tr>
</table>

> **Resultado del paso 1:** requisitos $m_0$ = 10 kg, $h_{ap}$ = 1000 m, $D_{cohete}$ = 150 mm, $\bar F \ge$ 490 N.
>
> **Con este resultado →** sabemos **qué** hay que lograr. Antes de calcular cuánto impulso hace falta, se fija **con qué** propelente se va a lograr, porque su $I_{sp}$ entra en los pasos 4 y 5.

---

## Propelente — KNSB (65 % KNO₃ / 35 % sorbitol)

**Pregunta:** ¿qué propiedades del propelente entran en la cadena de cálculo, y de dónde salen?

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Valor | Unidad | Origen |
|---|---|---|---|---|
| $I_{sp}$ | Impulso específico: segundos que 1 kg de propelente produce un empuje igual a su peso | 104 | s | Modelo termoquímico previo |
| $\rho_{ideal}$ | Densidad teórica: mezcla sin burbujas | 1841 | kg/m³ | Cálculo teórico |
| $\rho_p$ | Densidad real del grano colado | 1749 | kg/m³ | 95 % del ideal |
| $r$ | Velocidad de regresión: cuántos mm por segundo retrocede la superficie que quema | — | mm/s | Ley de Vieille |
| $a$, $n$ | Coeficiente y exponente de presión de la ley de Vieille | tabla | — | Datos experimentales de R. Nakka |
| $P$ | Presión de la cámara de combustión | — | MPa | — |

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

Es la "eficiencia" del propelente: a mayor $I_{sp}$, menos masa para el mismo impulso. Entra en el paso 4 (cuánto se aliviana el cohete) y en el paso 5 (cuánto propelente cargar).

</td>
<td valign="top">

**SP.1 · $I_{sp}$ = 104 s es conservador**

Sale del modelo termoquímico del motor de 38 mm, que trabajaba a baja presión y con una tobera pequeña. Un motor más grande con una tobera bien diseñada suele entregar más.

> $I_{sp}$ = 95 / 104 / 120 s → $m_p$ = 2.35 / 2.15 / 1.86 kg (paso 5).

Usar un valor bajo hace que el motor cargue propelente de más, que es el lado seguro para el apogeo.

</td>
</tr>
<tr>
<td valign="top">

**Densidad**

$$\rho_p = 0.95\,\rho_{ideal} = 0.95 \times 1841 = 1749\ \text{kg/m}^3$$

Al colar el propelente fundido quedan burbujas de aire atrapadas. Por eso el grano real es menos denso que la mezcla teórica. Entra en el paso 7 (volumen que ocupa el propelente).

</td>
<td valign="top">

**SP.2 · Densidad del 95 %**

Depende de la técnica de colado (temperatura, vacío, vibración). Debe medirse pesando y midiendo granos de prueba.

> 90 % → $V_p$ = 1297 cm³ (+5.6 %); 98 % → 1191 cm³ (−3 %).

Un grano menos denso ocupa más volumen y obliga a un motor más largo.

</td>
</tr>
<tr>
<td valign="top">

**Velocidad de regresión: ley de Vieille**

$$r = a\,P^{\,n}$$

- $r$: velocidad a la que retrocede la superficie que quema.
- $P$: presión de cámara. A más presión, la llama se acerca a la superficie y la calienta más.
- $a$, $n$: constantes medidas para cada propelente y cada rango de presión.

| P [MPa] | a [mm/s·MPaⁿ] | n |
|---|---|---|
| 0.10–0.81 | 10.708 | 0.625 |
| 0.81–1.50 | 8.763 | −0.314 |
| **1.50–3.79** | **7.852** | **−0.013** |
| 3.79–7.03 | 3.907 | 0.535 |
| 7.03–10.67 | 9.653 | 0.064 |

En la **meseta** (1.5–3.8 MPa), $n \approx 0$: la velocidad casi no depende de la presión. A 2.5 MPa, $r = 7.852 \times 2.5^{-0.013} = 7.76$ mm/s.

</td>
<td valign="top">

**SP.3 · El motor opera en la meseta**

Los ejemplos suponen 1.5–3.8 MPa. Ventaja: con $n \approx 0$ el motor es muy estable, porque un pico de presión no acelera la combustión.

> Se verifica en el modelo de cámara. Si la presión sale de la meseta, $r$ cambia y hay que rehacer los tiempos de combustión.

**SP.4 · Datos de laboratorio**

Los valores de $a$ y $n$ se midieron con muestras pequeñas (quemador de hebra). En un motor real pueden variar ±10 % por la composición, el tamaño de partícula y la humedad.

> Lo ideal es medir $r$ con el propelente propio del equipo.

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

La energía solo se conserva si no hay arrastre. Con aire, parte de la energía cinética se pierde durante la subida. Por eso el cohete real debe apagarse **más rápido** de lo que dice esta ecuación.

> Con aire (paso 4): $v_b$ = 166 m/s, un 19 % más que sin aire.

Este resultado es una **cota inferior**: sirve para conocer el orden de magnitud, no para diseñar.

**S2.2 · La masa se cancela**

Sin aire, un cohete de 1 kg y uno de 100 kg necesitan la misma velocidad. Con aire ya no: el efecto del arrastre sobre la velocidad es $F_D/m$, así que un cohete más pesado se frena menos.

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

No conocemos $h_b$ sin conocer el motor, así que lo tomamos como cero. En realidad el cohete sube mientras quema.

> Simulación (paso 4): $h_b$ ≈ 190 m → $v_b = \sqrt{2 \cdot 9.81 \cdot 810}$ = 126 m/s, un 10 % menos.

Este supuesto **sobrestima** $v_b$, mientras que S2.1 la **subestima**. Los dos errores se compensan en parte.

**S2.4 · Gravedad constante**

$g(h) = g_0\,[R/(R+h)]^2$, con $R$ = 6371 km.

> A 1000 m: $g$ = 0.9997 $g_0$ → efecto despreciable (0.03 %).

</td>
</tr>
</table>

> **Resultado del paso 2:** $v_b \approx$ **140 m/s** (cota inferior, sin aire).
>
> **Con este resultado →** ya sabemos qué velocidad hay que alcanzar. El paso 3 usa $v_b$ para calcular **cuánto impulso** necesita el motor para darle esa velocidad a 10 kg mientras vence la gravedad.

---

## Paso 3 — Impulso estimado a mano

**Pregunta:** ¿qué impulso total debe entregar el motor para llevar 10 kg hasta 140 m/s, sabiendo que mientras empuja la gravedad tira hacia abajo?

**Viene de:** $v_b$ = 140 m/s (paso 2), $m_0$ = 10 kg y $(F/W)_{min}$ = 5 (paso 1).

<table>
<tr><th width="60%">Resolución</th><th width="40%">Suposición y análisis</th></tr>
<tr>
<td valign="top">

**Variables**

| Símbolo | Nombre | Unidad |
|---|---|---|
| $I$ | Impulso total: el "empujón" acumulado del motor (fuerza × tiempo) | N·s |
| $F(t)$ | Empuje instantáneo del motor | N |
| $\bar F$ | Empuje medio durante la combustión | N |
| $t_b$ | Tiempo de combustión (*burn time*) | s |
| $m_0$ | Masa al despegue | kg |
| $v_b$ | Velocidad de apagado (del paso 2) | m/s |
| $L_{riel}$ | Largo del riel de lanzamiento | m |
| $v_{riel}$ | Velocidad del cohete al salir del riel | m/s |

</td>
<td valign="top">

*Fila de definiciones: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Qué es el impulso**

Es la fuerza acumulada en el tiempo. Un motor de 800 N durante 2 s y uno de 1600 N durante 1 s entregan el mismo impulso: 1600 N·s.

$$I = \int_0^{t_b} F(t)\,dt = \bar F\,t_b$$

- $\int F\,dt$: área bajo la curva de empuje contra tiempo.
- $\bar F\,t_b$: la misma área, como un rectángulo de altura igual al empuje medio.

</td>
<td valign="top">

*Definición exacta: no hay suposiciones.*

</td>
</tr>
<tr>
<td valign="top">

**Idea física: 2ª ley de Newton integrada en el tiempo**

Mientras el motor funciona actúan el empuje hacia arriba y el peso hacia abajo. Su suma, acumulada en el tiempo, cambia la cantidad de movimiento (masa × velocidad):

$$\underbrace{I}_{\text{impulso del motor}} - \underbrace{m_0\,g\,t_b}_{\text{lo que quita la gravedad}} = \underbrace{m_0\,v_b}_{\text{cantidad de movimiento final}}$$

- $I$: todo lo que empuja el motor.
- $m_0 g t_b$: **pérdida por gravedad**. Durante $t_b$ segundos, parte del empuje solo sirve para sostener el peso. Cuanto más dura la combustión, más se pierde.
- $m_0 v_b$: lo que realmente queda como movimiento: el cohete sale a $v_b$.

</td>
<td valign="top">

**S3.1 · Masa constante igual a $m_0$**

En realidad la masa baja de 10 kg a unos 8.2 kg mientras se quema el propelente. Usar $m_0$ sobreestima la cantidad de movimiento y la pérdida por gravedad.

> Con la masa media (9.1 kg): $I$ = 1434 N·s, un 10 % menos.

**S3.2 · Sin aire y $h_b \approx 0$**

Se heredan del paso 2. No incluir arrastre **subestima** el impulso; tomar $h_b$ = 0 lo **sobrestima**.

</td>
</tr>
<tr>
<td valign="top">

**Despeje sin depender de un paso posterior**

La ecuación tiene dos incógnitas, $I$ y $t_b$. Pero $t_b = I/\bar F$, así que si se elige el empuje medio queda una sola:

$$I = m_0 v_b + m_0 g\,\frac{I}{\bar F} \quad\Longrightarrow\quad \boxed{I = \frac{m_0\,v_b}{1 - \dfrac{m_0\,g}{\bar F}}}$$

- $m_0 g/\bar F$: fracción del empuje que se gasta en sostener el peso. Es el inverso de la relación empuje/peso.
- $1 - m_0 g/\bar F$: fracción del empuje que **sí acelera** al cohete.

**Lectura física:** si el empuje apenas iguala al peso ($\bar F \to m_0 g$), el denominador tiende a cero y el impulso necesario a infinito. Un motor así gasta todo en sostener el cohete y nunca lo acelera.

</td>
<td valign="top">

**S3.3 · Por qué hacer este paso si el 4 es más exacto**

Es una **verificación independiente**. Si la simulación diera, por ejemplo, 5000 N·s, esta estimación delataría un error en el código. Un resultado numérico sin un orden de magnitud de referencia no se puede auditar.

</td>
</tr>
<tr>
<td valign="top">

**Elección del empuje medio: criterio del riel**

Mientras el cohete está en el riel, el riel lo guía. Al salir, lo estabilizan las **aletas**, que solo funcionan con suficiente flujo de aire. Se pide salir del riel a $v_{riel} \ge$ 15–20 m/s. Con aceleración constante $a$:

$$v_{riel}^2 = 2\,a\,L_{riel}, \quad a = \frac{\bar F}{m_0} - g \;\Longrightarrow\; \bar F_{min} = m_0\left(\frac{v_{riel}^2}{2\,L_{riel}} + g\right)$$

- $v_{riel}^2/(2L_{riel})$: aceleración neta para alcanzar $v_{riel}$ en el largo del riel.
- $+\,g$: aceleración extra para vencer el peso.

| Largo del riel | $v_{riel}$ = 15 m/s | $v_{riel}$ = 20 m/s |
|---|---|---|
| 1.5 m | 848 N | 1431 N |
| 2 m | 661 N | 1098 N |
| **3 m** | 473 N | **765 N** |

Se elige $\bar F$ = **800 N**: cumple con un riel de 3 m a 20 m/s, y da una relación empuje/peso de 800/98.1 ≈ 8, por encima del mínimo de 5.

</td>
<td valign="top">

**S3.4 · $\bar F$ = 800 N es un supuesto**

El largo del riel **aún no está definido**. Con un riel de 2 m harían falta ≈1100 N.

Además, en el motor real el empuje no se elige: sale de la geometría del grano y de la presión. Este valor solo sirve para empezar. En cada ejemplo se verifica que el empuje real supere $\bar F_{min}$.

**Sensibilidad de este paso a $\bar F$**

| $\bar F$ | $I$ | $t_b$ |
|---|---|---|
| 600 N | 1674 N·s | 2.79 s |
| 800 N | 1596 N·s | 1.99 s |
| 1200 N | 1525 N·s | 1.27 s |

> Duplicar el empuje cambia el impulso ≈ 9 %: un motor más fuerte pierde menos por gravedad.

</td>
</tr>
<tr>
<td valign="top">

**Sustitución numérica**

$$I = \frac{10 \times 140}{1 - \dfrac{10 \times 9.81}{800}} = \frac{1400}{1 - 0.123} = \frac{1400}{0.877} \approx 1596\ \text{N·s}$$

$$t_b = \frac{I}{\bar F} = \frac{1596}{800} \approx 2.0\ \text{s}$$

Unidades: kg·m/s = N·s, porque 1 N = 1 kg·m/s².

</td>
<td valign="top">

**Balance de errores del paso 3**

| Supuesto | Efecto sobre $I$ |
|---|---|
| Sin aire | lo baja (subestima) |
| $h_b \approx 0$ | lo sube (sobrestima) |
| Masa constante $m_0$ | lo sube (sobrestima) |

Dos supuestos empujan hacia arriba y uno hacia abajo. Por eso 1596 queda **entre** el vuelo sin aire (1386, simulado) y el vuelo con aire (1826, paso 4).

</td>
</tr>
</table>

> **Resultado del paso 3:** $I \approx$ **1600 N·s**, $t_b \approx$ **2 s** (orden de magnitud).
>
> **Con este resultado →** sabemos en qué rango está el impulso. El paso 4 agrega lo que aquí se simplificó (aire, masa que disminuye, altura ganada al quemar) para obtener el **valor de diseño**, y usa 1600 N·s para validar la simulación.

---

## Paso 4 — Impulso requerido con vuelo simulado

**Pregunta:** ¿qué impulso lleva al cohete **exactamente** a 1000 m, teniendo en cuenta el aire, la masa que disminuye y la altura ganada durante la combustión?

**Viene de:** $m_0$ y $D_{cohete}$ (paso 1), $\bar F$ = 800 N y el rango ≈1600 N·s (paso 3), $I_{sp}$ = 104 s (propelente).

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

Se supone que el cohete sube en línea recta. En la práctica el riel se inclina unos grados por seguridad y el viento desvía la trayectoria, así que el apogeo real es algo menor.

> No cuantificado aquí: se cubre con el margen del 20 % del paso 5.

**S4.2 · Empuje constante (perfil rectangular)**

El empuje real varía: el BATES sube y baja ≈7.5 %, y hay un arranque y una cola. Lo que importa para el apogeo es el impulso total, no su forma.

> $\bar F$ = 600 / 800 / 1200 N → $I$ = 1840 / 1826 / 1812 N·s (±1 %).

</td>
</tr>
<tr>
<td valign="top">

**Ecuación 3: la masa disminuye**

$$\frac{dm}{dt} = -\dot m = -\frac{F}{I_{sp}\,g_0} \;\; (t < t_b), \qquad 0 \;\; (t \ge t_b)$$

**De dónde sale:** el impulso específico se define como $I_{sp} = F/(\dot m\,g_0)$: cuántos segundos puede un propelente producir un empuje igual a su propio peso. Despejando $\dot m$ se obtiene la ecuación. Un propelente con más $I_{sp}$ quema menos masa para el mismo empuje.

Integrando durante toda la combustión:

$$m_p = \frac{I}{I_{sp}\,g_0}$$

</td>
<td valign="top">

**S4.3 · $I_{sp}$ = 104 s**

Valor del modelo termoquímico previo. Es conservador: con una buena tobera el KNSB puede dar más. En este paso solo influye en cuán rápido se aliviana el cohete.

> $I_{sp}$ = 120 s → $I_{req}$ = 1836 N·s (+0.5 %). Influye mucho más en $m_p$ (paso 5).

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

**Orden de magnitud:** a 166 m/s, $F_D = \tfrac12 (1.225)(166)^2(0.5)(0.0177) \approx$ 149 N, que sobre unos 8 kg frena con ≈1.9 g adicionales.

</td>
<td valign="top">

**S4.4 · $C_d$ = 0.5**

Valor típico de cohetes amateur, que suelen estar entre 0.4 y 0.75. Sin túnel de viento ni CFD no se conoce mejor, por eso se prueban tres valores.

> ±20 % en $C_d$ → ±6 % en $I_{req}$.

**S4.5 · $\rho_0$ = 1.225 kg/m³ (nivel del mar)**

Es el caso más denso y por lo tanto conservador. Un sitio de lanzamiento alto, por ejemplo a ~1700 m de altitud, tiene $\rho \approx$ 1.0 kg/m³.

> $\rho_0$ = 1.0 → $I_{req}$ = 1731 N·s (−5 %).

**S4.6 · Atmósfera exponencial**

> A 1000 m da $\rho$ = 1.089 kg/m³ contra 1.112 de la atmósfera estándar (−2 %). Efecto menor.

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

**S4.7 · Paso de tiempo suficientemente fino**

Un método numérico solo vale si el resultado no depende del paso de tiempo. Se verificó con un paso 5 veces más chico.

> $\Delta t$ = 1 ms → 1825.6 N·s; $\Delta t$ = 0.2 ms → 1825.8 N·s. Convergido.

**Validación con el paso 3**

Simulación **sin aire**: 1386 N·s. La estimación a mano (1596) queda entre este valor y el vuelo con aire, como predice el balance de errores del paso 3. El código es coherente.

</td>
</tr>
<tr>
<td valign="top">

**Resultados**

| $C_d$ | $I_{req}$ [N·s] | $v_{max}$ [m/s] | $m_p$ [kg] | $t_b$ [s] |
|---|---|---|---|---|
| 0.4 | 1723 | 159 | 1.69 | 2.15 |
| **0.5** | **1826** | **166** | **1.79** | **2.28** |
| 0.6 | 1936 | 173 | 1.90 | 2.42 |

- $I_{req}$: impulso con el que el cohete llega justo a 1000 m (salida de la bisección).
- $v_{max}$: velocidad máxima; ocurre al apagarse el motor.
- $m_p = I_{req}/(I_{sp}\,g_0)$. Ejemplo: 1826 / (104 × 9.80665) = 1.79 kg.
- $t_b = I_{req}/\bar F$. Ejemplo: 1826 / 800 = 2.28 s.

</td>
<td valign="top">

**Qué enseña la tabla**

- **El aire cuesta +32 %:** sin aire bastan 1386 N·s; con aire hacen falta 1826.
- **$v_{max}$ = 166 m/s, no 140:** el cohete debe salir más rápido porque el aire lo frena durante la subida libre.
- **El supuesto más incierto ($C_d$) mueve poco el resultado:** un error razonable en $C_d$ no compromete el diseño.

</td>
</tr>
</table>

> **Resultado del paso 4:** $I_{req}$ = **1826 N·s** ($C_d$ = 0.5; $v_{max}$ = 166 m/s; $t_b$ = 2.28 s).
>
> **Con este resultado →** tenemos el impulso que la misión **exige**. El paso 5 le suma un **margen de diseño** para cubrir las suposiciones de estas notas ($C_d$, inclinación del riel, $I_{sp}$ real) y, con $I_{sp}$, obtiene la **masa de propelente** que debe cargar el motor.

---

## Paso 5 — Margen de diseño y masa de propelente

**Pregunta:** ¿cuánto impulso debe tener realmente el motor, considerando que las suposiciones de los pasos anteriores pueden fallar, y cuánto propelente hace falta para darlo?

**Viene de:** $I_{req}$ = 1826 N·s (paso 4) e $I_{sp}$ = 104 s (propelente).

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

**Por qué hace falta:** el paso 4 dio $I_{req}$ con supuestos ($C_d$, vuelo vertical, sin viento, empuje constante). Si el motor se diseñara con exactamente 1826 N·s, cualquier desviación desfavorable dejaría el cohete por debajo de 1000 m.

$$I_{dis} = 1.20 \times 1826 = 2191\ \text{N·s}$$

</td>
<td valign="top">

**S5.1 · $\mu$ = 20 %**

Es una decisión de ingeniería. El margen debe cubrir:

| Fuente | Efecto en $I_{req}$ |
|---|---|
| $C_d$ = 0.6 en vez de 0.5 | +6 % |
| Riel inclinado, viento | no cuantificado |
| Cohete más pesado de lo previsto | depende del paso 6 |

> El peor caso calculado ($C_d$ = 0.6 → 1936 N·s) queda cubierto con 13 % de holgura restante.

Un margen mayor da más seguridad de llegar, pero exige más propelente y un motor más pesado, lo que aprieta el presupuesto del paso 6.

</td>
</tr>
<tr>
<td valign="top">

**Masa de propelente**

De la definición de $I_{sp}$, integrada durante toda la combustión:

$$m_p = \frac{I_{dis}}{I_{sp}\, g_0}$$

- $I_{dis}$: impulso total a entregar.
- $I_{sp}\,g_0$: impulso que entrega cada kg de propelente (N·s/kg = m/s). Se llama **velocidad efectiva de escape**: 104 × 9.81 = 1020 m/s.

$$m_p = \frac{2191}{104 \times 9.80665} = \frac{2191}{1020} = 2.148\ \text{kg}$$

Unidades: N·s / (m/s) = (kg·m/s) / (m/s) = kg.

</td>
<td valign="top">

**S5.2 · Sensibilidad a $I_{sp}$**

| $I_{sp}$ | $m_p$ |
|---|---|
| 95 s | 2.35 kg |
| **104 s** | **2.15 kg** |
| 120 s | 1.86 kg |

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

Con 2191 N·s el motor es **clase K**.

**Apogeo con el margen:** simulando el vuelo con $I_{dis}$ el cohete llega a **1258 m**. Los 258 m de exceso son el margen expresado en altura.

</td>
<td valign="top">

**S5.3 · Implicaciones de la clase K**

Es un motor de cohetería de **alta potencia**. Antes de volarlo hacen falta pruebas estáticas en banco con distancia de seguridad, prueba hidrostática de la carcasa y los permisos que exija la normativa local.

</td>
</tr>
</table>

> **Resultado del paso 5:** $I_{dis}$ = **2191 N·s** (clase K), $m_p$ = **2.148 kg** de propelente.
>
> **Con este resultado →** sabemos cuánto propelente lleva el motor. El paso 6 verifica si **cabe en el presupuesto de 10 kg** junto con la estructura del motor y el resto del cohete.

---

## Paso 6 — Presupuesto de masa (parte común)

**Pregunta:** si el propelente pesa 2.148 kg, ¿cuánto puede pesar como máximo la estructura del motor para que el cohete completo no supere los 10 kg?

**Viene de:** $m_0$ = 10 kg (paso 1) y $m_p$ = 2.148 kg (paso 5).

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

Son valores típicos para un cohete de 150 mm con relación largo/diámetro ≈ 11 (unos 1.7 m de largo). El tubo, por ejemplo, sale de fibra de vidrio con 1.5 mm de pared: ≈1.33 kg/m.

> Se reemplazan por masas reales cuando el equipo de estructuras defina materiales. No hay carga útil incluida.

</td>
</tr>
<tr>
<td valign="top">

**Verificación del paracaídas**

En el descenso, a velocidad constante, el arrastre del paracaídas iguala al peso:

$$\tfrac{1}{2}\,\rho_0\, v_{desc}^2\, C_{D,par}\, A_{par} = m_{desc}\, g \;\Longrightarrow\; A_{par} = \frac{2\, m_{desc}\, g}{\rho_0\, C_{D,par}\, v_{desc}^2}$$

- Lado izquierdo: arrastre (misma forma que en el paso 4).
- Lado derecho: peso del cohete vacío, $m_{desc} = 10 - 2.148 = 7.85$ kg.

$$A_{par} = \frac{2 \times 7.85 \times 9.81}{1.225 \times 1.5 \times 5.5^2} = 2.77\ \text{m}^2 \;\Rightarrow\; \varnothing = \sqrt{\frac{4 A_{par}}{\pi}} = 1.88\ \text{m}$$

Un paracaídas de ese tamaño pesa ≈0.4 kg, así que cabe en los 0.90 kg de recuperación.

</td>
<td valign="top">

**S6.2 · $v_{desc}$ = 5.5 m/s**

Es una velocidad de aterrizaje segura habitual. Equivale a dejar caer el cohete desde ≈1.5 m.

| $v_{desc}$ | $\varnothing_{par}$ |
|---|---|
| 4.5 m/s | 2.30 m |
| **5.5 m/s** | **1.88 m** |
| 6.5 m/s | 1.59 m |

**S6.3 · $C_{D,par}$ = 1.5**

Depende del tipo de paracaídas y de qué área se toma como referencia. Debe tomarse del fabricante o de pruebas.

</td>
</tr>
<tr>
<td valign="top">

**Fracción de propelente mínima**

La masa total es la suma del motor y del resto. El motor pesa $m_p/\zeta$:

$$m_0 = \frac{m_p}{\zeta} + m_{resto} \quad\Longrightarrow\quad \boxed{\zeta_{min} = \frac{m_p}{m_0 - m_{resto}}}$$

- $m_0 - m_{resto}$: masa máxima disponible para el motor completo.
- $\zeta_{min}$: la menor fracción de propelente que aún cabe en 10 kg.

$$\zeta_{min} = \frac{2.148}{10 - 4.95} = \frac{2.148}{5.05} = 0.425$$

Masa máxima de la estructura del motor: $5.05 - 2.148 = 2.90$ kg.

</td>
<td valign="top">

**S6.4 · Sensibilidad a $m_{resto}$**

| $m_{resto}$ | $\zeta_{min}$ |
|---|---|
| 4.75 kg | 0.409 |
| **4.95 kg** | **0.425** |
| 5.15 kg | 0.443 |
| 5.45 kg | 0.472 |

> Cada 100 g extra en el resto del cohete exigen un motor un 2 % más eficiente en masa.

</td>
</tr>
</table>

> **Resultado del paso 6:** $\zeta_{min}$ = **0.425**. La estructura del motor (carcasa + tapas + tobera + liner) no puede pesar más de **2.90 kg**.
>
> **Con este resultado →** tenemos el límite de masa que cada ejemplo debe respetar según su material. El paso 7 calcula **cuánto espacio** ocupa el propelente, que es el dato con el que empieza la geometría del grano.

---

## Paso 7 — Volumen de propelente

**Pregunta:** ¿cuánto espacio ocupan los 2.148 kg de propelente?

**Viene de:** $m_p$ = 2.148 kg (paso 5) y $\rho_p$ = 1749 kg/m³ (propelente).

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

$$V_p = \frac{m_p}{\rho_p} = \frac{2.148\ \text{kg}}{1749\ \text{kg/m}^3} = 1.228 \times 10^{-3}\ \text{m}^3 = 1228\ \text{cm}^3$$

Es la definición de densidad: masa por unidad de volumen. 1228 cm³ es un poco más que una botella de 1.25 L.

</td>
<td valign="top">

**S7.1 · Hereda la densidad del 95 %**

> 90 % → 1297 cm³; 98 % → 1191 cm³ (ver SP.2).

Este volumen es **solo el propelente**. El motor ocupa más, porque el grano tiene un núcleo hueco por donde salen los gases. La relación entre ambos (carga volumétrica) depende de la geometría y se calcula en cada ejemplo.

</td>
</tr>
</table>

> **Resultado del paso 7:** $V_p$ = **1228 cm³**.
>
> **Con este resultado →** termina la parte común. Cada ejemplo toma $V_p$ y lo convierte en medidas reales: diámetro del grano, núcleo, largo y número de segmentos (pasos 8 a 12), con su propio material y geometría.

---

## Resumen de la cadena común

| Paso | Resultado | Pasa a |
|---|---|---|
| 1 · Requisitos | $m_0$ = 10 kg, $h_{ap}$ = 1000 m, $D$ = 150 mm | todos |
| Propelente | $I_{sp}$ = 104 s, $\rho_p$ = 1749 kg/m³ | 4, 5, 7 |
| 2 · Velocidad | $v_b \approx$ 140 m/s (cota inferior) | 3 |
| 3 · Impulso a mano | $I \approx$ 1600 N·s (validación) | 4 |
| 4 · Impulso simulado | $I_{req}$ = 1826 N·s | 5 |
| 5 · Margen | $I_{dis}$ = 2191 N·s, $m_p$ = 2.148 kg | 6, 7 |
| 6 · Masa | $\zeta_{min}$ = 0.425 (estructura ≤ 2.90 kg) | cada ejemplo |
| 7 · Volumen | $V_p$ = 1228 cm³ | cada ejemplo |
