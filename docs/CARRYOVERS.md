# Carryovers — decisiones transversales entre notebooks

Este archivo registra **decisiones que se toman al mejorar un notebook pero que
se deben aplicar en otro** (típicamente: "este tema lo sacamos de acá y va en
el siguiente"). Sirve como lista de pendientes inter-notebooks.

Cuando se trabaja sobre un notebook destino, **revisar primero este archivo**
para incorporar los carryovers pendientes y luego moverlos a "✅ Aplicados".

---

## ⬜ Pendientes

### Origen: Auditoría global → Destino: nuevos módulos

- **M06 (OOP)**: no existe en el material viejo. Escribir desde cero.

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
