# Informe de Auditoría — Fase 1

> Generado: 2026-04-16
> Alcance: Tutoriales 01–07, Laboratorios TP0–TP4
> Metodología: Extracción a Markdown con `nb2md.py`, revisión de cada archivo en `src/`

---

## Índice

1. [Resumen ejecutivo](#resumen-ejecutivo)
2. [Hallazgos transversales](#hallazgos-transversales)
3. [Auditoría de tutoriales](#auditoría-de-tutoriales) 
   - [T01: Introducción a Colab](#t01-introducción-a-colab)
   - [T02: Tipos de datos](#t02-tipos-de-datos)
   - [T03: Estructuras de control](#t03-estructuras-de-control)
   - [T04: Funciones](#t04-funciones)
   - [T05: NumPy](#t05-numpy)
   - [T06: Matplotlib](#t06-matplotlib)
   - [T07: SymPy](#t07-sympy)
4. [Auditoría de los laboratorios](#auditoría-de-laboratorios)
   - [TP0: Python básico](#tp0-python-básico)
   - [TP1: Variable compleja](#tp1-variable-compleja)
   - [TP2: Convolución](#tp2-convolución)
   - [TP3: Análisis de Fourier](#tp3-análisis-de-fourier)
   - [TP4: FFT y sistemas LTI](#tp4-fft-y-sistemas-lti)
5. [Comparación TP4 viejo vs actual](#comparación-tp4-viejo-vs-actual)
6. [Matriz de acción prioritaria](#matriz-de-acción-prioritaria)

---

## Resumen ejecutivo

### Estado general

| Notebook | Celdas | Calidad | Tono | Formato | Actividades |
|----------|:------:|:-------:|:----:|:-------:|:-----------:|
| T01 Colab | 33 | 4/5 | 3/5 | Regular | Ninguna |
| T02 Tipos | 112 | 3.5/5 | 2.5/5 | Regular | Ninguna |
| T03 Control | 42 | 4/5 | 3/5 | Regular | Ninguna |
| T04 Funciones | 30 | 3/5 | 2/5 | Aceptable | Ninguna |
| T05 NumPy | 62 | 4/5 | 2/5 | Bajo | Ninguna |
| T06 Matplotlib | 52 | 4/5 | 2/5 | Bajo | Ninguna |
| T07 SymPy | 92 | 4/5 | 2/5 | Bajo | Mal clasificadas |
| TP0 Python | 46 | — | 2/5 | Malo | 22 (sin scaffold) |
| TP1 Compleja | 65 | — | 4/5 | Regular | 8 (con `# TU CÓDIGO AQUÍ`) |
| TP2 Convolución | 64 | — | 2/5 | Malo | 13 (con `#completar`) |
| TP3 Fourier | 79 | — | 3/5 | Malo | 2 (faltan celdas) |
| TP4 FFT/LTI | 61 | — | 3/5 | Regular | 2 (compartidas) |

### Problemas críticos (5)

1. **Ningún tutorial tiene actividades prácticas.** Los 7 tutoriales son 100% expositivos, violando el ciclo "explicar → mostrar → practicar".
2. **Desajuste de numeración con el plan.** El actual T03 es "Estructuras de control" (debería ser T04). No existe tutorial de Colecciones (T03 planificado). No se enseñan diccionarios ni conjuntos.
3. **Contenido mal ubicado en T02.** Listas/tuplas/indexación/slicing (→ T03 Colecciones) y `cmath` avanzado (→ TP1) están incrustados en T02.
4. **TP3: Ejercicios 2 y 4 no tienen celda `act`.** El alumno no tiene dónde escribir código.
5. **Inconsistencia global de tono.** Ningún notebook usa voseo argentino de forma consistente. Se mezcla tú/vos/ustedes/impersonal.

---

## Hallazgos transversales

### A. Tono y voseo

Ninguno de los 12 notebooks usa consistentemente el voseo argentino requerido por la guía de estilo. Patrones detectados:

| Forma incorrecta | Forma correcta (voseo) | Notebooks afectados |
|-------------------|----------------------|---------------------|
| "Recuerda que..." | "Recordá que..." | T01, T02, T03, T04, T05, T06, T07 |
| "haz doble clic" | "hacé doble clic" | T01 |
| "no dudes" | "no dudes" (OK) / "no dejes de" | T01–T07 |
| "Puedes" | "Podés" | T05, T06 |
| "deberán" (ustedes) | "vas a tener que" / "deberías" | TP2 |

**Acción:** Pasada de normalización a voseo en todos los notebooks.

### B. Actividades prácticas

| Notebook | Celdas `enu-` | Celdas `act-` | Scaffold | Cumple ciclo explicar→mostrar→practicar |
|----------|:------------:|:------------:|:--------:|:---------------------------------------:|
| T01–T07 | 0 | 0 (T07: 5 mal clasificadas) | — | No |
| TP0 | 1 (falta reclasificar ~15) | 22 | Ninguno | Parcial |
| TP1 | 3 (faltan ~5) | 8 | `# TU CÓDIGO AQUÍ` | Parcial |
| TP2 | 1 (faltan ~12) | 13 | `#completar` (no estándar) | Parcial |
| TP3 | 4 | 2 (faltan 2) | Ninguno | No |
| TP4 | 2 | 2 (compartidas) | Ninguno | Parcial |

### C. Formato de celdas

Problemas recurrentes:
- **Celdas `hdr` usadas para contenido didáctico** (T05: `hdr-02`, `hdr-03`; T06: `hdr-03`–`hdr-06`; TP3: `hdr-02`).
- **Enunciados marcados como `prov-`** en vez de `enu-` (TP0, TP1, TP2, TP3).
- **Imports repetidos** en múltiples celdas en vez de estar agrupados al inicio (T05, T06).
- **Celdas `act-` del T07 (SymPy) contienen código completo** — deberían ser `prov-`.

### D. Conceptos huérfanos recurrentes

| Concepto | Primera aparición | Tutorial donde debería presentarse |
|----------|-------------------|-------------------------------------|
| `print()` | T01 `prov-08` (sin explicar) | T01 o inicio de T02 |
| `type()` | T02 `prov-04` (antes de explicar) | T02 (reordenar) |
| `input()` | T03 `prov-09` (sin presentar) | T02 o T03 |
| `int()` como conversión | T03 `prov-09` (sin presentar) | T02 |
| f-strings | T02 `prov-29` (usadas antes de explicar) | T02 (reordenar) |
| `import` | T02 `prov-92` (informal) | T01 o T02 (presentación formal) |
| `display()` | T07 `prov-05` | T01 (Colab) o T07 (SymPy) |
| `&` con arrays | T05 `prov-13` | T05 (NumPy) |
| `scipy.signal` | T06 `hdr-05` | T06 (Matplotlib) o tutorial aparte |
| `ipywidgets` | TP3 `prov-70` / TP4 `prov-20` | Ninguno — necesita explicación inline |

### E. Errores tipográficos

| Notebook | Celda | Error | Corrección |
|----------|-------|-------|------------|
| T02 | frontmatter | "02_Ttipos" | "02_Tipos" |
| T02 | `prov-28` | "obviemente" | "obviamente" |
| T02 | `prov-60` | "Indexaxión" | "Indexación" |
| T03 | `prov-03` | "contronl" | "control" |
| T04 | `prov-19` | "Farenheit" | "Fahrenheit" |
| T06 | `prov-07` | "floar" | "float" |
| T06 | `hdr-04` | "escalon nuitario" | "escalón unitario" |
| T06 | `prov-07` | "fecuencia" | "frecuencia" |
| T07 | `prov-02` | "usamaremos" | "usaremos" |
| T07 | `prov-17` | "expancion" | "expansión" |
| T07 | `prov-57` | "avaluamos" | "evaluamos" |
| TP0 | `enu-06` | "atrazo" | "atraso" |
| TP2 | `prov-02` | "librieras" | "librerías" |
| TP2 | `prov-02` | "Comenzaremos ejecutaremos" | "Comenzaremos ejecutando" |
| TP2 | `prov-41` | "de del" | "del" |
| TP3 | `prov-29` | "variabla", "preríodo" | "variable", "período" |
| TP3 | `prov-35` | "Identidicar" | "Identificar" |
| TP3 | `prov-67` | "intensión", "exitar" | "intención", "excitar" |

---

## Auditoría de tutoriales

### T01: Introducción a Colab

**Archivo:** `src/01_Introduccion_a_colab.md` (33 celdas)

#### Temas cubiertos
- [x] Qué es Jupyter y qué son los notebooks
- [x] Qué es Google Colab (ventajas, nube, gratuidad)
- [x] Entorno de ejecución (hardware, SO, librerías)
- [x] Conexión al entorno
- [x] Celdas de código (ejecución, Play, Ctrl+Enter)
- [x] Celdas de texto / Markdown (sintaxis básica, LaTeX, tablas)
- [x] Kernel compartido (variables compartidas, orden de ejecución)
- [x] Reiniciar sesión, tiempo máximo de conexión
- [x] Comentarios en Python (`#` y `"""`)
- [x] Comandos bash en Colab (`!pip install`)

#### Conceptos huérfanos
- `print()` (`prov-08`): usada sin explicar.
- Variables (`prov-17`/`prov-18`): `a = 2`, `b = 3` sin explicar asignación.
- `"""` como "comentario" (`prov-28`): técnicamente es un string literal, no un comentario.

#### Problemas de formato
- `hdr-02` tiene contenido extenso de recursos; debería ser `prov-`.
- Sin celdas `enu-` ni `act-`. Tutorial 100% expositivo.

#### Contenido faltante
- Mini-ejercicio para crear primera celda de código.
- Mini-ejercicio de Markdown (título, negrita, lista).
- Mención de Shift+Enter vs Ctrl+Enter.

#### Contenido que pertenece a otro lugar
- `prov-28`: comillas triples como "comentario" → posponer a T02 donde se presentan strings.

---

### T02: Tipos de datos

**Archivo:** `src/02_Ttipos_de_datos.md` (112 celdas)

#### Temas cubiertos
- [x] Qué es Python, comparación con C++
- [x] Strings, `print()`, `type()`
- [x] Enteros, flotantes, operaciones aritméticas, precedencia
- [x] Números complejos (`a + bj`)
- [x] Booleanos
- [x] Variables, asignación, nombres válidos, palabras reservadas
- [x] f-strings
- [x] Operadores de comparación y booleanos
- [x] Listas y tuplas (definición, indexación, slicing, mutabilidad)
- [x] `cmath` avanzado (polar, rectangular, trig compleja)

#### Conceptos huérfanos
- `print()` y `type()` usadas en `prov-04` antes de explicarse en `prov-05`.
- f-strings usadas en `prov-29` antes de explicarse en `prov-30`.
- `import cmath` en `prov-92`: primera aparición de `import`, sin presentación formal.
- Desempaquetado de tupla en `prov-102`: no conectado con asignación múltiple.

#### Problemas de estructura
- **Celda fantasma `prov-65`**: "Y llegamos al final de este tutorial!" está en la mitad del documento. Remanente de versión anterior.
- **`prov-104`**: `cmath.sin(z1)` duplicado (copy-paste).
- **`prov-36`**: `Nombre = ('Braulio')` no crea una tupla (falta coma). Puede confundir.

#### Contenido faltante
- **Conversiones de tipo** (`int()`, `float()`, `str()`, `bool()`): no cubiertas.
- **`input()`**: no presentada. Se usa en T03 sin explicación.

#### Contenido que pertenece a otro lugar
- **Listas, tuplas, indexación, slicing** (`prov-49` a `prov-82`): → T03 (Colecciones).
- **`cmath` avanzado** (`prov-83` a `prov-110`): → TP1 o tutorial avanzado. Ocupa ~30% del notebook.

---

### T03: Estructuras de control

**Archivo:** `src/03_estructuras_de_control.md` (42 celdas)

> **ALERTA:** Según el plan, T03 debería ser "Colecciones". El contenido actual (control de flujo) corresponde a T04. No existe tutorial de Colecciones — diccionarios y conjuntos no se enseñan en ningún tutorial.

#### Temas cubiertos
- [x] Condicionales: `if`, `elif`, `else`
- [x] `input()` e `int()` (usadas sin presentación previa)
- [x] `for` con listas, strings, `range()`
- [x] `range(len(...))` para iteración con índices
- [x] Bucles anidados (lista de listas)
- [x] Parámetro `end` de `print()`
- [x] `while`, operadores de asignación compuesta (`+=`)
- [x] Bucles infinitos, `break`, `continue`

#### Conceptos huérfanos
- `input()` (`prov-09`): no presentada en T01 ni T02.
- `int()` como conversión (`prov-09`): nunca presentada.
- Lista de listas (`prov-26`): no explicada como patrón.
- Parámetro `end` de `print()` (`prov-28`): primer keyword argument, concepto no presentado.

#### Contenido faltante (respecto al plan T04)
- List comprehensions.
- `enumerate()`.
- Actividades de práctica.

---

### T04: Funciones

**Archivo:** `src/04_Funciones.md` (30 celdas)

#### Temas cubiertos
- [x] Definición con `def`, sintaxis, llamada
- [x] Funciones sin parámetros y con parámetros
- [x] Parámetros por defecto
- [x] Valores de retorno (`return`)
- [x] Composición de funciones (excelente ejemplo Fahrenheit→Kelvin→Celsius)
- [x] Alcance (scope): variables globales y locales

#### Problemas
- **Error conceptual en `prov-28`**: "Los argumentos se devuelven con `return`" — debería decir "los **resultados** se devuelven".
- **`prov-26`**: genera error a propósito (`print(y)` fuera del scope) sin advertir al estudiante.
- Sin actividades prácticas.

#### Contenido faltante
- Funciones lambda (previstas en el plan para T05).
- Keyword arguments.
- Docstrings.

---

### T05: NumPy

**Archivo:** `src/05_Introduccion_NumPy.md` (62 celdas)

#### Temas cubiertos
- [x] Concepto de librería e `import ... as`
- [x] Arrays 1D y 2D, `shape`
- [x] `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
- [x] Operaciones con escalares y entre arrays
- [x] Funciones matemáticas (`sin`, `cos`, `exp`, `sqrt`, `log`)
- [x] Agregación (`sum`, `mean`, `std`, `min`, `max`)
- [x] Constantes (`np.pi`, `np.e`)
- [x] Slicing, vistas vs copias (`.copy()`)
- [x] Arrays complejos, `.real`, `.imag`, `np.abs`, `np.angle`

#### Problemas
- **`prov-40` (código duplicado)**: idéntico a `prov-36`. Copy-paste erróneo.
- **`hdr-02` y `hdr-03`** mal clasificadas: contienen contenido didáctico, deberían ser `prov-`.
- **`prov-41`**: `use_line_collection=True` — deprecated en Matplotlib >= 3.8.
- Operador `&` con arrays (`prov-13`) sin explicación.
- Imports repetidos en 4 celdas.

#### Contenido faltante
- Fancy indexing, boolean indexing.
- `reshape`, `flatten`, `ravel`.
- Broadcasting (explicación formal).

---

### T06: Matplotlib

**Archivo:** `src/06_MatPlotLib.md` (52 celdas)

#### Temas cubiertos
- [x] `plt.plot`, títulos, labels, grilla
- [x] Frecuencia de muestreo y señales
- [x] `np.heaviside`, `np.piecewise`
- [x] SciPy: señal cuadrada, triangular, diente de sierra
- [x] Componente DC, desplazamiento temporal
- [x] Leyendas, `figsize`, subplots
- [x] `plt.stem`, `plt.scatter`
- [x] Plano complejo

#### Problemas
- Múltiples erratas: "floar", "escalon nuitario", "fecuencia".
- **Numeración duplicada**: dos secciones "2.2".
- **`prov-31`**: usa variable `x` definida muchas celdas antes (frágil).
- **`hdr-03` a `hdr-06`** mal clasificadas (contenido didáctico, no headers).
- `use_line_collection=True` deprecated.

#### Contenido que pertenece a otro lugar
- Frecuencia de muestreo, Nyquist, aliasing → material de la materia/TP, no tutorial de Matplotlib.
- SciPy completo → podría tener sección propia o tutorial aparte.

---

### T07: SymPy

**Archivo:** `src/07_SymPy.md` (92 celdas)

#### Temas cubiertos
- [x] Qué es SymPy, `import sympy as sy`
- [x] `init_printing()`, `display()`
- [x] Variables simbólicas (`sy.symbols`)
- [x] Factorización, expansión, simplificación
- [x] Sustituciones (`.subs`), evaluación numérica (`.evalf()`)
- [x] `sy.Rational`
- [x] Resolución de ecuaciones (`sy.solve`)
- [x] Derivadas (`sy.diff`), integrales (`sy.integrate`)
- [x] Graficación (`sy.plot`), `sy.Piecewise`

#### Problemas
- **Alias `sy` en vez de `sp`**: inconsistente con la guía de estilo.
- **Celdas `act-01` a `act-05` contienen código completo**: mal clasificadas, deberían ser `prov-`. No hay `# TU CÓDIGO AQUÍ`.
- **`prov-78`/`prov-79`**: texto dice $\int_0^{\pi} \sin x\,dx$ pero el código calcula $\int_{-5}^{5} z^2\,dz$. Inconsistencia.
- **Sección 8.1 duplicada**: `sy.plot()` y `sy.Piecewise` ambas numeradas 8.1.
- Múltiples erratas: "usamaremos", "expancion", "avaluamos".

#### Contenido faltante
- Transformada de Laplace (`sy.laplace_transform`).
- Series de Taylor/Fourier.
- Ecuaciones diferenciales (`sy.dsolve`).
- Matrices simbólicas (`sy.Matrix`).

---

## Auditoría de los laboratorios

### TP0: Python básico

**Archivo:** `src/TP0.md` (46 celdas)

#### Mapa de ejercicios

| # | Descripción | Dificultad | Guía |
|---|-------------|:----------:|:----:|
| 1.1 | Variables string, concatenar, imprimir | 1 | 2 |
| 1.2 | Operaciones numéricas básicas | 1 | 3 |
| 1.3 | Operaciones con complejos | 1 | 3 |
| 2.1 | Condicional positivo/negativo/cero con `input` | 2 | 2 |
| 2.2a | Bucle `for` del 1 al 10 | 1 | 3 |
| 2.2b | Bucle `while` del 10 al 1 | 1 | 3 |
| 3.1 | Función `es_par` | 2 | 3 |
| 3.2 | Función `suma_complejos` | 2 | 3 |
| 4.1–4.3 | Arrays NumPy: crear, operar, slice | 1 | 3 |
| 5.1–5.5 | Matplotlib: plot, personalizar, subplots, stem, scatter | 1–2 | 2–3 |
| 6 | Señal cuadrada con SciPy (integrador) | 3 | 3–4 |

#### Problemas principales
- **Scaffold nulo**: todas las `act-` están vacías, sin `# TU CÓDIGO AQUÍ`.
- **~15 enunciados marcados como `prov-`** en vez de `enu-`.
- **Ejercicio 6 incompleto**: el Paso 4 no tiene celda `act-`.
- **Salto brusco** al Ej. 6: introduce `scipy.signal.square` sin ejemplo previo.
- Tono: imperativo formal, sin voseo.

#### Conceptos huérfanos en ejercicios
- `plt.subplots()`, `plt.stem()`, `plt.scatter()`, `.real`/`.imag`: no se presentan en el notebook.
- `scipy.signal.square`: no se importa ni se muestra ejemplo.

---

### TP1: Variable compleja

**Archivo:** `src/TP1_variable_compleja.md` (65 celdas)

#### Mapa de ejercicios

| # | Descripción | Dificultad | Guía |
|---|-------------|:----------:|:----:|
| Act. 1 | Input x,y → construir z, módulo, fase, graficar | 2 | 3 |
| Act. 2 | Mapeo de segmento, f(z)=1/z, comparar | 3 | 4 |
| Act. 3 | Funciones armónicas, Cauchy-Riemann con SymPy | 3 | 3 |
| Act. 4a | Serie de Taylor de cos(z) | 1 | 4 |
| Act. 4b | Serie de Laurent de 1/(z²(z-2)) | 2 | 3 |
| Act. 5 | Integral por residuos | 2 | 3 |

#### Progresión de dificultad
Ascendente y bien lograda. Cada sección tiene ejemplo guiado completo → actividad. **Modelo a seguir** para los demás TPs.

#### Problemas principales
- **Error factual en `enu-03`**: pide serie de Taylor de cos(z) "que incluya términos hasta 1/z²". cos(z) es entera, no tiene potencias negativas. Mezcla el enunciado de Taylor con el de Laurent.
- **~5 enunciados marcados como `prov-`** en vez de `enu-`.
- `sp.Matrix` y `sp.Rational` usados sin presentar.
- Scaffold mínimo (solo `# TU CÓDIGO AQUÍ`, sin variables predefinidas).
- Falta `dz` en la integral del enunciado `prov-52`.

#### Tono
**El mejor de todos los notebooks.** Usa voseo consistente ("Completá", "Repetí", "Construí"). Tono cercano y paciente. Modelo a seguir.

---

### TP2: Convolución

**Archivo:** `src/TP2_convolucion.md` (64 celdas)

#### Mapa de ejercicios

| # | Descripción | Dificultad | Guía |
|---|-------------|:----------:|:----:|
| act-01 a act-08 | Cargar/verificar/normalizar/graficar señal violin.wav | 1 | 4–5 |
| act-09, act-10 | Reproducir y graficar convolución | 1–2 | 3–4 |
| act-11 | Convolución discreta (ej. 10.a de gabinete) | 3 | 1 |
| act-12, act-13 | Filtro pasaaltos 2D en imágenes | 2 | 3–4 |

#### Problemas principales
- **12 de 13 enunciados marcados como `prov-`** en vez de `enu-`.
- **`act-11` no autocontenido**: referencia "ejercicio 10.a del TP6 de gabinete" sin incluir las señales.
- **Scaffold con `#completar`** en vez de `# TU CÓDIGO AQUÍ`.
- **`prov-35`**: función `convolve_signals(x, h)` que tarda >30 min. Peligrosa si se ejecuta por accidente.
- **Título incorrecto** (`prov-01`): dice "Trabajo práctico n 3" pero es TP2.
- **Tono muy inconsistente**: mezcla vos/tú/usted/ustedes.
- Múltiples erratas: "librieras", "de del", "Comenzaremos ejecutaremos".

---

### TP3: Análisis de Fourier

**Archivo:** `src/TP3_analisis_de_fourier.md` (79 celdas)

#### Mapa de ejercicios

| # | Descripción | Dificultad | Guía |
|---|-------------|:----------:|:----:|
| Ej. 1 | Serie trigonométrica de Fourier, espectros, truncada a 20 componentes | 2 | 3 |
| Ej. 2 | Serie exponencial compleja, espectros, truncada a 30 términos | 2–3 | 2 |
| Ej. 3 | Espectro de pulso con retraso 0.2s, comparar | 2 | 2 |
| Ej. 4 | Espectros de rampa finita | 1–2 | 3 |

#### Problemas principales
- **Ej. 2 y Ej. 4 no tienen celda `act`**: el alumno no tiene dónde escribir.
- **Ej. 2 no autocontenido**: referencia "ejercicio 4b del práctico de gabinete" sin definir la señal.
- **Título incorrecto** (`prov-01`): dice "TP N°2" pero es TP3.
- **`hdr-02` mal clasificada**: contiene imagen de circuito RL, no es header.
- **Cuerpo de enunciados en celdas `prov-`**: el texto de enu-03/enu-04 está separado del encabezado.
- **`prov-70`**: comenta "5 períodos" pero la fórmula calcula 65.
- **Celdas `act` sin scaffold**.
- Erratas: "variabla", "preríodo", "Identidicar", "intensión", "exitar".

#### Sección sin ejercicio
La sección 4 (Respuesta en frecuencia, con circuito RL y widgets interactivos) es material provisto sin actividad.

---

### TP4: FFT y sistemas LTI

**Archivo:** `src/TP4_FFT_y_sistemas_LTI.md` (61 celdas)

#### Mapa de ejercicios

| # | Descripción | Dificultad | Guía |
|---|-------------|:----------:|:----:|
| Ej. 1 | Sumar senoidal 80 Hz, FFT, espectro | 1–2 | 4 |
| Ej. 2 | Espectro de onda cuadrada 25 Hz, armónicos impares | 2 | 4 |
| Ej. 3 | Sistema LTI: H(s), resp. impulso, polos/ceros, resp. frecuencia | 2–3 | 4 |

#### Problemas principales
- **Ej. 1 y 2 comparten una sola celda `act-01`**: dificulta corrección automatizada.
- **Ej. 3 parcialmente no autocontenido**: depende de "ejercicio 5b del TP7 de gabinete" para H(s).
- **Celdas `act` sin scaffold**.
- Inconsistencia entre texto y código en normalización FFT (`prov-14` vs `prov-15`).
- Sin voseo argentino.

#### Aspectos positivos
- Enunciados excelentes: pasos numerados, claros, con contexto pedagógico.
- Material provisto muy completo sobre sistemas LTI (impulso, escalón, entrada arbitraria, resp. frecuencia, polos/ceros).
- Widget interactivo de sistema LTI (sección nueva vs versión vieja).

---

## Comparación TP4 viejo vs actual

| Aspecto | TP4_viejo | TP4 actual |
|---------|-----------|------------|
| Estructura | Monolítico | Dividido en FFT + Sistemas LTI |
| Introducción teórica | Breve | Extensa y didáctica |
| Normalización FFT | Sin explicar | Sección completa |
| Bug en gráfico | `amplitud_normalizada(x_fft)` (error de sintaxis) | Corregido |
| Enunciados | Marcados como `prov-`, escuetos | Marcados como `enu-`, detallados |
| Sistemas LTI | Explicación mínima | 5 operaciones con subtítulos "Qué es / Por qué / En Python" |
| Widget interactivo | No existe | Sección completa nueva |
| Celdas `act` separadas | Sí (una por ejercicio) | No (Ej. 1 y 2 comparten) |

**Conclusión:** La versión actual es una mejora sustancial. El único retroceso es que los ejercicios 1 y 2 perdieron sus celdas `act` separadas.

---

## Matriz de acción prioritaria

### Prioridad 1 — Crítico (antes de Fase 2)

| Acción | Notebooks afectados |
|--------|---------------------|
| Crear tutorial T03 Colecciones (extraer de T02 + agregar dicts/sets) | Nuevo T03 |
| Renumerar actual T03 (control) como T04, T04 (funciones) como T05, etc. | T03–T07 |
| Agregar celdas `act-` faltantes en TP3 (Ej. 2 y 4) | TP3 |
| Separar celdas `act-` de Ej. 1 y 2 en TP4 | TP4 |
| Normalizar tono a voseo argentino | Todos |
| Agregar actividades prácticas a tutoriales (mín. 2–3 por tutorial) | T01–T07 |

### Prioridad 2 — Importante (durante Fase 2/3)

| Acción | Notebooks afectados |
|--------|---------------------|
| Reclasificar enunciados `prov-` → `enu-` | TP0, TP1, TP2, TP3 |
| Reclasificar `hdr-` → `prov-` donde corresponda | T05, T06, TP3 |
| Reclasificar `act-` → `prov-` en T07 (contienen código completo) | T07 |
| Estandarizar scaffold a `# TU CÓDIGO AQUÍ` | TP0, TP2 |
| Mover sección `cmath` de T02 → TP1 | T02, TP1 |
| Presentar `print()`, `type()`, conversiones, `input()` antes de usarlos | T01, T02 |
| Corregir error factual en TP1 `enu-03` (Taylor ≠ Laurent) | TP1 |
| Hacer enunciados autocontenidos (incluir señales/H(s) en el notebook) | TP2 act-11, TP3 Ej. 2, TP4 Ej. 3 |

### Prioridad 3 — Mejoras (durante Fase 2/3)

| Acción | Notebooks afectados |
|--------|---------------------|
| Corregir todas las erratas tipográficas | Ver tabla en sección E |
| Eliminar celda fantasma `prov-65` de T02 | T02 |
| Eliminar código duplicado (`prov-40` = `prov-36` en T05, `prov-104` en T02) | T02, T05 |
| Cambiar alias `sy` → `sp` en T07 | T07 |
| Corregir inconsistencia texto/código en T07 (integral) y TP3 (`prov-70`) | T07, TP3 |
| Agrupar imports al inicio de cada notebook | T05, T06 |
| Eliminar `use_line_collection=True` (deprecated) | T05, T06 |
| Agregar scaffold a celdas `act-` (variables, firmas, verificaciones) | TP0, TP1, TP3, TP4 |
| Corregir numeración de títulos internos vs nombres de archivo | TP2 ("TP3"), TP3 ("TP2") |
| Mover frecuencia de muestreo/Nyquist de T06 a material de materia | T06 |

---

## Apéndice: Mapa de renumeración propuesto

| Archivo actual | Contenido | Número propuesto | Nombre propuesto |
|----------------|-----------|:----------------:|------------------|
| `01_Introduccion_a_colab` | Colab | T01 | `T01_introduccion_colab` |
| `02_Ttipos_de_datos` | Tipos básicos | T02 | `T02_tipos_de_datos` |
| *(nuevo)* | Colecciones | T03 | `T03_colecciones` |
| `03_estructuras_de_control` | Control de flujo | T04 | `T04_control_de_flujo` |
| `04_Funciones` | Funciones | T05 | `T05_funciones` |
| *(nuevo)* | OOP | T06 | `T06_clases_objetos` |
| `05_Introduccion_NumPy` | NumPy | T07 | `T07_numpy` |
| `06_MatPlotLib` | Matplotlib | T08 | `T08_matplotlib` |
| `07_SymPy` | SymPy | T09 | `T09_sympy` |
