# Carryovers — decisiones transversales entre notebooks

Este archivo registra **decisiones que se toman al mejorar un notebook pero que
se deben aplicar en otro** (típicamente: "este tema lo sacamos de acá y va en
el siguiente"). Sirve como lista de pendientes inter-notebooks.

Cuando se trabaja sobre un notebook destino, **revisar primero este archivo**
para incorporar los carryovers pendientes y luego moverlos a "✅ Aplicados".

---

## ⬜ Pendientes

### Origen: renombres (tutoriales → módulos) → Destino: Fase 4 (página de inicio)

- El link del M01 en `README.md` e `index.md` ya se actualizó (apunta a
  `M01_introduccion_colab.ipynb`). Los otros 6 links siguen apuntando a los
  nombres viejos (`02_Ttipos_de_datos.ipynb`, etc.).
- **A medida que se reescriba cada módulo (M02–M09)**: actualizar su link
  correspondiente en README/index y borrar el `.ipynb` viejo. Hacerlo en el
  mismo commit que el rename evita tener links rotos en la página pública.
- **Fase 4 hará el overhaul completo** del README/index: reemplazar
  "tutoriales" por "módulos", reorganizar tabla, eliminar fechas viejas,
  actualizar autor/introducción para tono publicable.

---

## ✅ Aplicados

- **2026-04-16** — M09 (`M09_sympy`) reescrito a partir del
  `07_SymPy` viejo. Secciones: `import sympy as sy` + `init_printing`
  (con nota sobre numérico vs. simbólico), `sy.symbols` (una y
  múltiples variables, restricciones `integer`/`real`/`positive`),
  manipulación (`factor`, `expand`, `simplify`, mención de
  `trigsimp`/`expand_trig`), sustitución (`.subs` simbólica y
  numérica, `.evalf`, `sy.Rational`), `sy.solve` (lineal, cuadrática,
  con variable específica, sistema de ecuaciones con tupla),
  derivadas (`sy.diff`, orden superior, parciales), integrales
  (indefinida y definida con `sy.pi` simbólica), `sy.Piecewise`, y
  puente al mundo numérico con `sy.lambdify(..., "numpy")` + `plt.plot`.
  5 actividades tangibles: factorizar/expandir un polinomio, resolver
  `R1` en un divisor de tensión, derivar la energía de un capacitor
  ($E = \tfrac{1}{2}Cv^2$), integrar corriente lineal para obtener
  carga acumulada, y graficar $f(x) = x^3 - 3x$ junto con su derivada
  vía `lambdify`. **Se deja fuera intencionalmente:** Laplace,
  transformada Z, series de Fourier, convolución y cualquier otro
  contenido de la asignatura (decisión: los módulos enseñan Python,
  los labs aplican la teoría). También `sy.plot` nativo (se usa
  Matplotlib vía `lambdify`, consistente con M08). Link de la fila 9
  del README/index actualizado a `M09_sympy.ipynb` con texto
  "9. SymPy". `07_SymPy.ipynb` y `src/07_SymPy.md` viejos borrados
  del repo. Notebook validado con `jupyter nbconvert --execute`
  (91 celdas, ejecuta limpio).

- **2026-04-16** — M08 (`M08_matplotlib`) reescrito a partir del
  `06_MatPlotLib` viejo. Secciones: `import matplotlib.pyplot as plt`
  (con `np` en paralelo), primer gráfico con `plt.plot` (parábola +
  `plt.show()`), personalización básica (`title`, `xlabel`, `ylabel`,
  `grid`), graficar una señal muestreada reusando la senoidal del
  Módulo 7 (con la nota de que Matplotlib "conecta muestras" —
  adelanta el hilo continuo↔discreto sin profundizar), varias señales
  con `label=` + `plt.legend()` (y mención de `color=`/códigos estilo
  MATLAB), `plt.figure(figsize=...)`, `plt.subplots(filas, columnas)`
  con API OO (`axs[i].set_title` etc.) + `plt.tight_layout()`,
  `plt.stem` para señales discretas (con regla `plot` vs `stem`),
  `plt.scatter` con complejos en el plano (`z.real`/`z.imag`,
  `axhline`/`axvline`). 5 actividades tangibles: senoidal de 50 Hz,
  entrada/salida de un amplificador (G=3) con leyenda, tensión y
  potencia instantánea en subplots, descarga muestreada de un capacitor
  con `stem`, impedancia medida a 4 frecuencias en el plano complejo.
  **Se deja fuera intencionalmente:** `scipy.signal` (square, sawtooth
  — van a L1/L3), `np.heaviside` y `np.piecewise`, aliasing/muestreo
  bajo (va a L6), desplazamiento temporal y componente DC (conceptos
  de señales, no de Matplotlib). Link de la fila 8 del README/index
  actualizado a `M08_matplotlib.ipynb` con texto "8. Matplotlib".
  `06_MatPlotLib.ipynb` y su fuente viejos borrados del repo. Notebook
  validado con `jupyter nbconvert --execute` (39 celdas, ejecutan
  limpio).

- **2026-04-16** — M07 (`M07_numpy`) reescrito a partir del
  `05_Introduccion_NumPy` viejo. Secciones: `import numpy as np` (con
  recordatorio del `from math import` de M05), creación de arrays
  (`np.array`, `.shape`/`.size`/`.dtype`, mención breve de 2D),
  `zeros`/`ones`/`arange`/`linspace` (con tabla de cuándo usar cada uno),
  operaciones vectorizadas con escalar y entre arrays (nota breve sobre
  *broadcasting* para adelantarlo sin profundizar), funciones
  matemáticas (`sin`/`cos`/`exp`/`sqrt`/`log`/`abs`) y constantes
  (`np.pi`, `np.e`), indexado y slicing (con nota breve sobre
  vistas vs. copias sin actividad dedicada), agregación (`sum`, `mean`,
  `std`, `min`, `max`) destacando que también existen como métodos
  (`arr.mean()`) y cerrando el puente con M06. 5 actividades tangibles:
  ley de Ohm vectorizada, muestrear senoidal con `linspace`+`np.sin`,
  recortar primeros 5 ms con slicing, potencia media con `np.mean`, y
  telecom con longitudes de onda de cuatro canales de la banda
  ciudadana (27 MHz) calculando la antena de cuarto de onda. **Se deja
  fuera intencionalmente:** arrays de complejos (se trata en L2),
  indexado booleano/fancy (se delega a los labs), 2D más allá de una
  mención. Link de la fila 7 de README/index actualizado a
  `M07_numpy.ipynb` con texto "7. NumPy". `05_Introduccion_NumPy.ipynb`
  y su fuente viejos borrados del repo.

- **2026-04-16** — M06 (`M06_clases_objetos`) escrito desde cero (no
  existía en el material viejo). Secciones: objetos que ya se venían
  usando (atributos `.real`/`.imag` en complejos, métodos en strings y
  listas), definición de clases con `class`/`__init__`/`self`, métodos
  propios, ejemplo rico con `Senoidal` (usa `math.sin`/`pi`) incluyendo
  `valor_en(t)` y `periodo()`, evaluación de una señal en muchos
  instantes combinando comprensión de lista y `zip`. Herencia sólo
  *mencionada* (sintaxis `class Hija(Madre):`), sin profundizar —
  decidido con el usuario. No se presentan `__str__`/`__repr__`. 4
  actividades tangibles: `Capacitor` con `capacidad` y `tension_max`,
  método `energia(v)`, clase `CircuitoRC` con `tau()` y
  `frecuencia_corte()`, comparación de dos senoidales a distintas
  frecuencias usando `zip`. Se inserta nueva fila en README/index (M06
  Clases y objetos) entre Funciones y Numpy, se renumeran las filas
  6→7, 7→8, 8→9 y se sube el rowspan del TP0 de 8 a 9.

- **2026-04-16** — M05 retoque: se detectó que la actividad 4 usaba
  `from math import log10` sin haberlo presentado. Se agregó una
  sub-sección "Usar funciones que ya vienen con Python: `import`"
  (prov-22c/d/e) justo antes de la actividad 4, que introduce `from
  math import log10, sqrt, pi` con ejemplo corto y una nota anticipando
  `import numpy as np` para M07. M06 se apoya en esta presentación sin
  volver a explicarla. `M05_funciones.ipynb` regenerado (51 celdas).

- **2026-04-16** — M05 (`M05_funciones`) reescrito a partir del 04_Funciones
  viejo. Secciones: definición y llamada (`def`/`return`), parámetros
  posicionales y con nombre (*keyword arguments*), valores por defecto
  (con nota sobre *docstrings*), retorno múltiple con desempacado,
  composición (una función que llama a otras), alcance (local vs
  global, con recomendación de pasar por parámetro y devolver con
  `return`), funciones como valores y `lambda` (con `sorted(..., key=...)`
  como caso de uso canónico). 5 actividades tangibles (ley de Ohm,
  divisor de tensión con valor por defecto, estadísticos con retorno
  múltiple, potencia en dBm vía composición de funciones, ordenar
  señales por amplitud pico a pico con `lambda`). Eliminadas las
  referencias a profesor/cátedra del 04_Funciones viejo. Link de la
  fila 5 del README/index actualizado a `M05_funciones.ipynb`.
  `04_Funciones.ipynb` viejo borrado del repo.

- **2026-04-16** — M04 (`M04_estructuras_de_control`) reescrito a partir
  del T03 viejo. Secciones: condicionales (`if/elif/else`, indentación,
  comparaciones encadenadas, anidamiento), bucle `for` (iterar lista/string,
  patrón acumulador, `range()`, `enumerate()`, recorrido de diccionario con
  `.items()`), bucle `while` (con nota sobre bucles infinitos y cómo
  detenerlos en Colab), `break`/`continue` con ejemplos tangibles,
  comprensiones de lista (con filtro y con `if/else` inline), integrador
  final clasificando resistencias. 4 actividades tangibles (clasificar
  tensión, analizar muestras, carga de capacitor con `while`, comprensiones
  sobre una señal). Eliminadas las referencias a profesor/cátedra del T03
  viejo. Link de la fila 4 del README/index actualizado a
  `M04_estructuras_de_control.ipynb`; se renumeran las filas 4–7 a 5–8 y
  se sube el rowspan del TP0 a 8. `03_estructuras_de_control.ipynb` viejo
  borrado del repo.

- **2026-04-16** — M01 reescrito con nueva nomenclatura ("Módulo 1"),
  actividades agregadas (enu/act), tono publicable sin referencias a
  profesor/ayudantes, Shift+Enter vs Ctrl+Enter, sección reiniciar entorno.
  Link en README/index actualizado. `.ipynb` viejo
  (`01_Introduccion_a_colab.ipynb`) borrado.

- **2026-04-16** — M03 (`M03_colecciones`) escrito desde cero: cuatro
  colecciones (lista/tupla/dict/set), indexado y slicing, métodos básicos,
  operador `in`, `len`/`sum`/`min`/`max`/`sorted`, desempacado de tuplas,
  operaciones de conjuntos. 6 actividades con contexto tangible
  (temperaturas, señal, tensiones, capacitor, LED, frecuencias). Se asoma
  un `for` mínimo al final con aviso de que se formaliza en M04. Link de la
  fila 3 del README/index actualizado a `M03_colecciones.ipynb`; el link
  público a "Estructuras de Control" se retira hasta que M04 esté listo.
  El archivo `03_estructuras_de_control.ipynb` se conserva en el repo como
  insumo para M04.

- **2026-04-16** — M02 escrito desde cero con lineamiento "solo contenido útil
  (balance entre señales y utilidad general de Python)". Aplicados los
  carryovers de M01→M02 (presentación formal de variables/`=`, `print()` con
  f-strings) y los de auditoría→M02 (conversiones de tipo, comillas triples
  como *string literal* no comentario, `input()`). Secciones: variables,
  `print()`, numéricos, booleanos/comparaciones (intro mínima, se profundiza
  en M04), strings, complejos (solo creación/`.real`/`.imag`/`abs()` — resto
  delegado a M07 y L2), conversiones, `input()`. Indexación/slicing quedan
  para M03. Link en README/index actualizado a `M02_tipos_de_datos.ipynb`;
  `.ipynb` viejo (`02_Ttipos_de_datos.ipynb`) borrado.
