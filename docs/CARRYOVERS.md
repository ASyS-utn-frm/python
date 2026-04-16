# Carryovers — decisiones transversales entre notebooks

Este archivo registra **decisiones que se toman al mejorar un notebook pero que
se deben aplicar en otro** (típicamente: "este tema lo sacamos de acá y va en
el siguiente"). Sirve como lista de pendientes inter-notebooks.

Cuando se trabaja sobre un notebook destino, **revisar primero este archivo**
para incorporar los carryovers pendientes y luego moverlos a "✅ Aplicados".

---

## ⬜ Pendientes

### Origen: tooling `@header` → Destino: todos los `src/*.md`

- El tooling (`md2nb.py` / `nb2md.py`) ya soporta la directiva `@header`:
  en `src/*.md` la celda de encabezado se escribe solo como `@header` y
  `md2nb.py` expande al convertir usando `src/_header.md` +
  `resources/logoUTN.jpg` (base64 calculado al vuelo). El `.ipynb`
  generado queda idéntico al actual (logo embebido).
- **Pendiente:** cuando se reescriba cada `src/*.md`, colapsar el bloque
  HTML del encabezado (`<center>... base64 ...</center>`) a una sola
  línea `@header`. Esto reduce drásticamente el tamaño de la fuente y
  unifica el texto al nuevo "Departamento de Ingeniería en Tecnologías
  Electrónicas" (ver `docs/FORMATO_CELDAS.md` §3).
- No hay migración masiva programada: se aplica oportunísticamente cada
  vez que se toque un `src/*.md`.

### (Resuelto 2026-04-16) Overhaul de README/index

El overhaul completo de Fase 4 se adelantó (ver "Aplicados"). Todos
los links de los módulos apuntan al nombre nuevo `MNN_*.ipynb`, y se
reemplazó "tutoriales" por "módulos", se añadió la sección
**Laboratorios** con L00, se reformuló **Entrega** y se eliminaron
las fechas de entrega / avisos rojos. Queda como seguimiento:

- Cuando se escriba cada laboratorio nuevo (L01–L08), agregar su fila
  en la tabla "Laboratorios" del README/index con el link Colab
  correspondiente.
- A medida que cada Lx reemplace a un TPn, borrar la fila
  correspondiente de "Material de ediciones anteriores".

---

## ✅ Aplicados

- **2026-04-16** — README.md / index.md: **overhaul completo (Fase 4
  adelantada)**. Reescritura con tono publicable: (a) título ahora es
  "Curso introductorio de Python para Análisis de Señales y Sistemas";
  (b) intro reemplaza "tutoriales" por "módulos" y menciona
  explícitamente el Departamento de Ingeniería en Tecnologías
  Electrónicas (estudiantes con poca o ninguna experiencia previa);
  (c) secciones separadas **Módulos** y **Laboratorios**, la segunda
  con L00 visible y una nota sobre L01–L08 en desarrollo; (d) TP1–TP4
  quedan bajo la subsección "Material de ediciones anteriores" con
  nota de que se van a reemplazar; (e) sección **Entrega** nueva y
  detallada (6 pasos: resolver en Colab → respetar celdas → reiniciar y
  correr → descargar .ipynb → renombrar con apellido → subir al
  campus), con advertencia destacada de que solo se modifican las
  celdas `# TU CÓDIGO AQUÍ`; (f) se eliminaron la fecha de entrega del
  TP4 y el aviso rojo de "nueva metodología"; las fechas van solo al
  campus virtual; (g) autor reescrito sobrio. `index.md` sincronizado
  con `README.md` con `cp`. `TP0.ipynb` y `src/TP0.md` se conservan
  en el repo por ahora como insumo para L1.

- **2026-04-16** — L00 actualizado según lineamiento "entrega en
  README, aviso explícito en labs": (a) se reemplazó la sección corta
  "## Entrega" por un bloque **## IMPORTANTE: qué celdas podés
  modificar** que explica que solo se modifican las celdas con
  `# TU CÓDIGO AQUÍ` y por qué (corrección automática celda por celda);
  (b) el cierre (prov-15) ahora remite a la página del curso para las
  instrucciones de entrega y se agregó un item de checklist "no
  modifiqué ninguna celda fuera de las de actividad"; (c) también se
  corrigió la abreviatura "telecom" → "telecomunicaciones" en prov-01
  (nueva memoria `feedback_no_abreviaturas`). Notebook regenerado y
  validado con `jupyter nbconvert --execute`.

- **2026-04-16** — L00 (`L00_practica_python`) escrito desde cero como
  **primer laboratorio entregable** del curso. Decisión con el usuario:
  se agrega L00 a la estructura original de 8 labs (ahora 9: L00 + L01–L08).
  L00 practica todo lo visto en M01–M09 con **ejercicios nuevos** que no
  duplican los de los módulos. 8 bloques, uno por módulo: (1) longitud
  de onda `λ = c/f` para AM/FM/Wi-Fi [M02], (2) diccionario de notas
  musicales → frecuencias de una melodía [M03], (3) clasificar
  frecuencias en bandas HF/VHF/UHF con `if/elif` + comprensión filtro
  [M04], (4) funciones `fc_rc`, `ganancia_db`, `ganancia_total_db` con
  composición [M05], (5) clase `Bateria` con `energia_wh` y `autonomia`
  [M06], (6) tono DTMF tecla "5" + cálculo RMS [M07], (7) tres señales
  en subplots (exp creciente, tren de pulsos con `stem`, senoidal
  amortiguada) [M08], (8) despejar `C` del filtro RC con `sp.solve` +
  `.subs` + `.evalf` [M09]. Integrador final: **detector DTMF por MSE**
  (sin Fourier) — el alumno recibe un tono misterioso generado con
  `np.random.default_rng(seed=42)`, compara con los 12 candidatos y
  elige el de menor error cuadrático. Tono super explicativo en cada
  enunciado (qué se pide + qué herramienta usar + conceptos del dominio
  como DTMF, RMS, bandas RF, dB de tensión explicados desde cero).
  Decisiones clave: (a) nomenclatura `L00_*` siguiendo convención
  `LNN_*` de CLAUDE.md; (b) no se mete en muestreo/`dt`/Nyquist (eso
  queda para L1); (c) sí usa `linspace`/`plot`/`stem` pero sin entrar
  en la reflexión continuo↔discreto. Archivos: `src/L00_practica_python.md`
  (34 celdas), notebook generado con `md2nb.py`, y `rubrics/L00_rubric.md`
  con solución de referencia y puntajes (total 100 pts + bonus 5 pts).
  Notebook validado con `jupyter nbconvert --execute` (corre limpio)
  y soluciones de referencia validadas con un script aparte.
  `PROJECT_PLAN.md` actualizado: la transición TP0→L1 ahora es
  TP0→L0+L1, y el rol de L1 se aclaró como "cierre **conceptual**"
  (vs. "cierre integrador" que pasó a L0).

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
