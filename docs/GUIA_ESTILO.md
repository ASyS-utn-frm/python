# Guía de estilo — Notebooks de ASyS

Lineamientos para mantener un tono, formato y estructura consistentes
en todos los notebooks del curso.

---

## 0. Criterio rector

Estos notebooks son **documentos pedagógicos**: su único producto es la comprensión
del alumno. Por lo tanto, **la calidad de la redacción no es un acabado, es la
función del material**. Un notebook con el código correcto, los `cell_id` bien
puestos y los gráficos prolijos, pero con explicaciones vagas, vocabulario impreciso
o afirmaciones no verificadas, **no cumple su objetivo**: falló en lo único que tenía
que hacer.

De ahí el orden de prioridades al escribir o revisar:

1. **Que se entienda y que sea exacto** — §1 y §1 bis. Si algo hay que rehacer, se
   rehace por acá.
2. Que el recorrido didáctico funcione — dificultad ascendente, nada de conceptos
   huérfanos, ejercicios tangibles.
3. Que valide contra el contrato técnico — `cell_id`, placeholders, compilación.
4. Que el formato sea consistente — estructura de celdas, tablas, separadores.

Los puntos 3 y 4 son condiciones necesarias y verificables por script: si fallan, el
material no se puede corregir ni publicar. Pero cumplirlos no aporta ni un punto de
calidad — solo habilitan que el trabajo del punto 1 llegue al alumno. Cuando el
tiempo alcance para una sola revisión más, va sobre el punto 1.

---

## 1. Tono y voz

### Principio general
Escribir como un **tutor cercano y paciente** que explica con claridad,
sin ser condescendiente ni innecesariamente formal.

### Pautas
- **Usar "vos"** (español rioplatense/argentino): "fijate", "probá", "ejecutá"
- **Evitar jerga innecesaria** en inglés cuando hay equivalente claro en español
  - Bien: "cadena de texto" (y aclarar que en Python se dice *string*)
  - Mal: usar *string* sin haberlo presentado
- **Presentar el término en inglés** la primera vez que aparece, entre paréntesis:
  > Una lista (*list*) es una colección ordenada de elementos.
- **No asumir conocimientos previos** de programación. Cada concepto se presenta
  desde cero en el módulo correspondiente
- **Ser preciso sin ser exhaustivo**: dar la explicación suficiente para que el
  alumno entienda y pueda usar el concepto, no un tratado completo
- **Usar analogías concretas** de la vida cotidiana o de la ingeniería cuando ayuden

### Ejemplos de tono

**Bien:**
> Cuando Python encuentra un `for`, repite el bloque de código una vez
> por cada elemento de la secuencia. Pensalo como una máquina que procesa
> una caja de piezas: agarra una, la procesa, agarra la siguiente, y así
> hasta que se vacía la caja.

**Mal (muy formal):**
> La estructura iterativa `for` implementa un ciclo determinístico cuya
> cardinalidad está definida por la longitud del iterable proporcionado.

**Mal (muy informal):**
> El for es re fácil, básicamente hace lo mismo muchas veces jaja

---

## 1 bis. Registro y precisión del vocabulario

El tono cercano de la sección anterior **no habilita el coloquialismo**. El registro
es *semiformal y técnicamente preciso*: se conserva el voseo y la cercanía, pero se
nombra cada cosa con su término correcto. El destinatario es un alumno que recién
empieza, y el vocabulario preciso es parte de lo que tiene que aprender: si el
material lo nombra mal, no tiene de dónde sacar la referencia correcta.

### Coloquialismos a evitar

| En vez de | Escribir |
|-----------|----------|
| "un eje chiquito", "de juguete" | "un eje reducido", "de prueba" |
| "ese es todo el truco" | "esa es toda la técnica" |
| "quedarse con un pedazo" | "extraer un tramo / fragmento" |
| "cambia de golpe" | "cambia de manera instantánea" |
| "al rato vuelve" | "un tiempo después regresa" |
| "un poquito más rápido" | "levemente más rápido" |
| "apretá play" | "presioná el botón de reproducción" |
| "dar vuelta el array" | "invertir el array" |
| "el gráfico sale mal" | "el gráfico resulta incorrecto" |
| "cambiar un renglón" | "cambiar una sola línea" |
| "te dejamos una función" | "se provee una función" |
| "estas celdas no se tocan" | "estas celdas no deben modificarse" |
| "arranca en 0" | "comienza en 0" |
| "que no se pase de 1" | "que no supere 1" |
| "define dos cosas" | "define dos elementos / factores / recursos" |

### Término técnico exacto

- **muestra** (no "punto") para los valores de una señal muestreada.
- **instante** para los elementos de un eje de tiempo. Un eje tiene *instantes*;
  una señal tiene *muestras*. No llamar "puntos" a ninguno de los dos.
- **índice** (no "posición") para ubicar un elemento de un array.
- **longitud** (no "largo") de un array.
- **frecuencia de muestreo** para `fs`, expresada en muestras por segundo.
- **reflejar** (no "invertir") para $x(-t)$; **invertir** queda para dar vuelta un
  array o para la simetría respecto del eje horizontal.
- **anular** (no "apagar") para el resultado de multiplicar por cero.
- Anglicismos técnicos en cursiva la primera vez: *slicing*, *clipping*, *string*.

### Definir, no solo nombrar

Introducir un objeto por su nombre no lo define. La prueba es preguntarse si el
alumno podría reconstruir el objeto a partir de la frase.

**Mal:**
> **`t`** es el eje de tiempo, en segundos.

**Bien:**
> **`t`** es lo que llamamos el eje de tiempo, pero conviene precisar qué es
> exactamente: un array que contiene **instantes medidos en segundos**, y no
> valores de ninguna señal. Contiene 1401 instantes entre −2 s y 5 s, separados
> 5 ms. Una señal queda entonces representada por **dos arrays de la misma
> longitud** que se leen en paralelo: `t` dice *en qué instante*, y el otro dice
> *cuánto vale* la señal en ese instante.

Reglas prácticas que se desprenden:

- Dar siempre los **números concretos** (cantidad, paso, rango, unidades) en lugar
  de adjetivos vagos como "denso", "grueso" o "chico".
- Justificar cuantitativamente las decisiones de diseño: no "el eje es demasiado
  grueso para audio", sino "un período de 440 Hz dura 2,3 ms y el paso del eje es
  de 5 ms, así que no entra ni una oscilación entre dos instantes".
- Nombrar correctamente la **procedencia** de cada herramienta (`Audio` es de
  IPython, no "de Colab").

### Verificar antes de afirmar

Toda afirmación cuantitativa y toda referencia cruzada se comprueban, no se estiman:

- Los números que aparecen en el texto (frecuencias, porcentajes, cantidades de
  muestras, resultados de una cuenta) se corren en un script antes de escribirlos.
- Las afirmaciones del tipo "esto no se presenta en el Módulo 7" se verifican con
  `grep` sobre `src/M*.md`.
- Cuidado especial con los resultados que tienen dos lecturas posibles. Ejemplo
  real: en un batido de 440 y 443 Hz la envolvente $\cos(2\pi\frac{\Delta f}{2}t)$
  tiene frecuencia 1,5 Hz, pero se oyen **3** pulsaciones por segundo porque el
  volumen sigue el valor absoluto. Decir "la envolvente pulsa 3 veces por segundo"
  es incorrecto; hay que distinguir las dos cosas.

---

## 2. Estructura de un módulo

Cada módulo sigue esta estructura general:

```
1. Encabezado (logo + título)
2. Introducción breve (¿qué vamos a aprender? ¿para qué sirve?)
3. Secciones de contenido (numeradas)
   3.1 Explicación del concepto
   3.2 Ejemplo de código ejecutable
   3.3 [Opcional] "Probá vos" — mini ejercicio inline
4. Resumen de lo aprendido
5. [Opcional] Ejercicios integradores
```

### Ritmo: explicar → mostrar → practicar

Cada concepto nuevo sigue el ciclo:
1. **Explicar** en markdown (1-3 párrafos máximo)
2. **Mostrar** con un ejemplo de código ejecutable
3. **Practicar** (opcional): celda vacía para que el alumno pruebe una variación

---

## 3. Estructura de un laboratorio

```
1. Encabezado (logo + título)
2. Objetivos del laboratorio
3. Reglas de entrega (qué celdas se pueden modificar)
4. Preparación: imports y configuración inicial, presentados por una celda de texto
5. Bloques de ejercicios (orden ascendente de dificultad):
   a. Explicación del contexto / teoría necesaria
   b. Ejemplo resuelto (código provisto que el alumno ejecuta)
   c. Enunciado del ejercicio (celda ejN-enunciado)
   d. Celda de actividad (celda ejN-code)
   e. Pregunta de análisis + celda de respuesta (ejN-pregunta / ejN-respuesta)
6. [Opcional] Ejercicio integrador final
7. Checklist de entrega y cierre
```

### Regla: ninguna celda aparece sin explicación

**Toda celda que el alumno ve tiene que estar justificada por qué está ahí.**
Esto vale especialmente para las celdas de código **provistas** (imports,
funciones auxiliares, ejes de tiempo, generadores de datos): cada una debe venir
precedida por una celda de texto que explique qué hace, por qué aparece en ese
punto del recorrido y qué se espera del alumno (habitualmente, solo ejecutarla).

No alcanza con poner la explicación como comentario adentro del código: el
alumno que recorre el notebook leyendo los textos se saltea los comentarios, y
la celda le queda descolgada.

Mal:

```
[markdown] ## IMPORTANTE: qué celdas podés modificar
[code]     import numpy as np ...        ← aparece de la nada
[markdown] ## Sección A
```

Bien:

```
[markdown] ## Preparación
           Ejecutá la celda que sigue una sola vez. Además de las librerías,
           define `t`, el eje de tiempo que usan todas las señales del lab...
[code]     import numpy as np ...
[markdown] ## Sección A
```

Verificación rápida sobre un `.ipynb` generado: toda celda de código cuyo
`cell_id` no matchee `ejN-code` debe tener una celda markdown inmediatamente
antes.

### Niveles de dificultad

Los ejercicios dentro de cada laboratorio se organizan en tres niveles:

| Nivel | Guía | Descripción |
|-------|------|-------------|
| 1. Guiado | Alta | Se da scaffold, el alumno completa líneas específicas |
| 2. Semi-guiado | Media | Se da la estructura, el alumno implementa la lógica |
| 3. Abierto | Baja | Se da el enunciado, el alumno diseña la solución |

Cada laboratorio debe tener **al menos** ejercicios de nivel 1 y 2.
Los de nivel 3 son opcionales o bonus.

---

## 4. Formato Markdown

### Encabezados
```markdown
# 1. Título de sección principal
## 1.1 Subsección
### Actividad 1
```

- Numeración arábiga para secciones (1, 2, 3...)
- Subsecciones con punto (1.1, 1.2...)
- Actividades con título descriptivo: "### Actividad 1: Suma de complejos"

### Ecuaciones LaTeX
- Inline: `$z = a + bj$`
- Display: `$$|z| = \sqrt{a^2 + b^2}$$`
- Usar `j` (no `i`) para la unidad imaginaria (convención de ingeniería)

### Código inline
- Usar backticks para `funciones()`, `variables`, `tipos` mencionados en el texto
- Ejemplo: "La función `abs()` calcula el módulo de un número complejo"

### Tablas
Preferir tablas Markdown para resúmenes comparativos:
```markdown
| Operación | Sintaxis | Ejemplo |
|-----------|----------|---------|
| Suma      | `a + b`  | `3 + 4` → `7` |
```

### Notas y advertencias
Usar blockquotes con prefijo:

```markdown
> **Nota:** Los índices en Python comienzan en 0, no en 1.

> **Importante:** No olvides ejecutar la celda de imports antes de continuar.

> **Recordá:** Este concepto lo vimos en el Módulo 3, sección 2.1.
```

---

## 5. Código Python

### Estilo general
- Seguir PEP 8 (nombres_con_guiones_bajos, 4 espacios de indentación)
- Comentarios en español
- Nombres de variables descriptivos en español cuando son del dominio:
  ```python
  frecuencia = 1000        # Hz
  periodo = 1 / frecuencia  # segundos
  ```
- Nombres técnicos de Python/NumPy en inglés (son parte del lenguaje):
  ```python
  import numpy as np
  array_señal = np.array([1, 2, 3])
  ```

### Imports
Siempre al inicio del notebook, agrupados:
```python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
```

### Comentarios en código de ejemplo
- Explicar **qué** hace cada bloque significativo
- No comentar lo obvio
- En los primeros módulos, ser más generoso con los comentarios

```python
# Bien: explica el propósito
# Generamos una señal senoidal de 1 kHz
t = np.linspace(0, 0.01, 1000)  # 10 ms, 1000 puntos
señal = np.sin(2 * np.pi * 1000 * t)

# Mal: comenta lo obvio
t = np.linspace(0, 0.01, 1000)  # creamos un array con linspace
señal = np.sin(2 * np.pi * 1000 * t)  # calculamos el seno
```

### Prints y salidas
- Usar f-strings para salidas formateadas:
  ```python
  print(f"El módulo de z es: {abs(z):.2f}")
  ```
- En los primeros módulos (antes de presentar f-strings), usar la forma simple:
  ```python
  print("El módulo de z es:", abs(z))
  ```

---

## 6. Gráficos

### Estilo consistente
```python
plt.figure(figsize=(10, 4))
plt.plot(t, señal, 'b-', linewidth=1.5, label='Señal')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Señal senoidal de 1 kHz')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Pautas
- Siempre incluir **labels en los ejes** con unidades
- Siempre incluir **título**
- Usar `grid(True, alpha=0.3)` por defecto
- Usar `tight_layout()` para evitar recortes
- `figsize=(10, 4)` como tamaño por defecto para señales temporales
- `figsize=(8, 6)` para gráficos 2D o polares

---

## 6 bis. Audio

Varios laboratorios reproducen señales con `Audio`, de `IPython.display`. Hay
tres reglas que **no son opcionales**: si se rompen, el notebook parece
funcionar pero enseña algo falso, o directamente falla en la celda del alumno.

### Siempre `normalize=False`

```python
Audio(senal, rate=fs, normalize=False)
```

`Audio` trae `normalize=True` por defecto, y eso **reescala la señal para que
su pico llegue al tope del rango disponible**. La consecuencia es que la
amplitud del array deja de tener efecto audible: una sinusoide de amplitud `0.5`
y una de `0.05` suenan exactamente igual de fuerte. Cualquier ejercicio o
pregunta de análisis que hable de volumen queda invalidado en silencio, sin
error ni advertencia.

### Toda señal audible va acotada a `[-1, 1]` **por construcción**

Con `normalize=False`, un solo valor fuera de rango aborta la celda con:

```
ValueError: Audio data must be between -1 and 1 when normalize=False
```

No recorta ni distorsiona: **falla**. Por eso la cota tiene que salir de cómo
está armada la señal, no de la confianza en que los números den bien. Al sumar
$n$ señales de amplitud 1, dividir por $n$; al usar una envolvente, elegir la
amplitud del tono por debajo de 1. Amplitudes habituales: `0.5` o `0.6`.

Verificar el pico antes de dar el lab por terminado:

```python
print(abs(senal).max())   # tiene que dar ≤ 1
```

### El `Audio(...)` va como última expresión de la celda

El reproductor aparece porque el notebook muestra el resultado de la última
expresión. Si después hay un `print()` o un `plt.show()`, no se ve nada. En
celdas con gráfico y sonido, el `Audio` va al final.

### Al escribir el enunciado

Nombrar la procedencia (`Audio` no es de NumPy ni de Matplotlib, viene de
IPython) y advertir que el reproductor **no arranca solo**: hay que apretar
*play*. Agregar siempre que quien trabaje en un equipo sin audio puede resolver
los ejercicios a partir del gráfico.

---

## 7. Regla de oro: no usar lo que no se presentó

Antes de usar un concepto, función o construcción sintáctica en un notebook,
verificar que se haya presentado en un módulo anterior o en el mismo notebook.

### Orden de dependencias de los módulos

```
M01 (Colab) → M02 (Tipos) → M03 (Colecciones) → M04 (Control)
                                                       ↓
M09 (SymPy) ← M08 (Matplotlib) ← M07 (NumPy) ← M05 (Funciones)
                                                       ↓
                                                  M06 (OOP)
```

Si un módulo necesita algo de un módulo posterior, hay dos opciones:
1. **Mover** el concepto al módulo donde se necesita
2. **Dar una explicación mínima** inline con referencia al módulo completo:
   > Usamos `range()` para generar una secuencia de números. Veremos más
   > detalles en el Módulo 4, por ahora alcanza con saber que
   > `range(5)` genera los números del 0 al 4.

---

## 8. Checklist de revisión

Antes de dar por terminado un notebook, verificar:

- [ ] Todas las celdas tienen ID y rol asignado
- [ ] No se usan conceptos no presentados previamente
- [ ] El tono es consistente (tuteo con vos, cercano pero preciso)
- [ ] No quedan coloquialismos de la tabla de la sección 1 bis
- [ ] Cada objeto nuevo está **definido**, no solo nombrado (sección 1 bis)
- [ ] Los términos técnicos son los exactos (instante/muestra, índice, longitud)
- [ ] Los números del texto se verificaron corriéndolos, y las referencias a otros
      módulos con `grep` sobre `src/`
- [ ] Las ecuaciones LaTeX renderizan correctamente
- [ ] Los gráficos tienen ejes etiquetados, título y grid
- [ ] Si hay audio: todos los `Audio(...)` llevan `normalize=False`, van como
      última expresión de su celda, y ninguna señal supera 1 en valor absoluto
      (sección 6 bis)
- [ ] Los imports están al inicio
- [ ] Las celdas de actividad tienen `# TU CÓDIGO AQUÍ`
- [ ] Los enunciados son claros y autocontenidos
- [ ] La dificultad es ascendente dentro del notebook
- [ ] No hay outputs guardados (notebooks limpios)
