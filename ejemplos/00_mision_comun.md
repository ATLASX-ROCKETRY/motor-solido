# Misión común — pasos 1–5 y 7

Estos pasos **no dependen ni del grano ni del material de la carcasa**: el impulso
lo exigen la masa, el apogeo y el arrastre. Se calculan una vez y los usan los tres
ejemplos.

Ecuaciones: [`docs/01_mision_a_geometria.md`](../docs/01_mision_a_geometria.md).
Cálculo: `python3 scripts/comun.py`.

---

## Paso 1 — Requisitos

| Símbolo | Valor |
|---|---|
| $m_0$ | 10 kg (incluye el motor cargado) |
| $h_{ap}$ | 1000 m |
| $D_{cohete}$ | 150 mm |
| $(F/W)_{min}$ | 5 → $\bar F \ge 5 \times 10 \times 9.81 = 490$ N |

## Propelente: KNSB (65 % KNO₃ / 35 % sorbitol)

| Propiedad | Valor | Origen |
|---|---|---|
| $I_{sp}$ | 104 s | modelo termoquímico previo (conservador) |
| $\rho_{ideal}$ | 1841 kg/m³ | teórico |
| $\rho_p$ | 1749 kg/m³ | 95 % del ideal (grano colado real) |
| $r = aP^n$ | por tramos (tabla abajo) | datos experimentales de R. Nakka |

| P [MPa] | a [mm/s·MPaⁿ] | n |
|---|---|---|
| 0.10–0.81 | 10.708 | 0.625 |
| 0.81–1.50 | 8.763 | −0.314 |
| **1.50–3.79** | **7.852** | **−0.013** |
| 3.79–7.03 | 3.907 | 0.535 |
| 7.03–10.67 | 9.653 | 0.064 |

En la **meseta** (1.5–3.8 MPa), $n \approx 0$: a 2.5 MPa, $r = 7.76$ mm/s, y casi no
cambia con la presión. Los tres ejemplos suponen que el motor opera en la meseta.
El modelo de cámara lo verificará.

## Cómo leer los pasos 2, 3 y 4

Cada paso es una hoja dividida en dos columnas:

- **Resolución** (izquierda): qué se calcula, con qué ecuación, qué significa cada término y el resultado.
- **Suposición y análisis** (derecha): cada simplificación usada en esa fila, por qué se acepta y cuánto cambia el resultado si no se cumple.

Al final de cada paso se indica el **resultado** y qué permite calcular en el **paso siguiente**.

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

## Paso 5 — Margen y propelente

$$I_{dis} = 1.20 \times 1826 = 2191\ \text{N·s} \quad(\text{clase K})$$

$$m_p = \frac{2191}{104 \times 9.80665} = 2.148\ \text{kg}$$

Apogeo nominal con $I_{dis}$: **1258 m**. El exceso sobre 1000 m es el margen.

## Paso 7 — Volumen de propelente

$$V_p = \frac{2.148}{1749} = 1228\ \text{cm}^3$$

## Presupuesto del resto del cohete (entra al paso 6 de cada ejemplo)

| Componente | Masa |
|---|---|
| Tubo de fuselaje (~1.3 m, fibra de vidrio) | 1.75 kg |
| Cono de nariz | 0.70 kg |
| Aletas | 0.60 kg |
| Soporte del motor | 0.50 kg |
| Recuperación | 0.90 kg |
| Aviónica | 0.50 kg |
| **Total necesario** | **4.95 kg** |

**Paracaídas** (descenso a 5.5 m/s, $m_{desc} = 10 - 2.148 = 7.85$ kg, $C_{D,par} = 1.5$):

$$A_{par} = \frac{2 \times 7.85 \times 9.81}{1.225 \times 1.5 \times 5.5^2} = 2.77\ \text{m}^2 \;\Rightarrow\; \varnothing = 1.88\ \text{m}$$

**Fracción de propelente mínima** para que el presupuesto cierre:

$$\zeta_{min} = \frac{m_p}{m_0 - m_{resto}} = \frac{2.148}{10 - 4.95} = 0.425$$

Cualquier motor con $\zeta < 0.425$ hace que el cohete supere los 10 kg.
