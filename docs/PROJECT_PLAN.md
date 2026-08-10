# Plan Maestro — Curso de introducción a Python para ASyS

> Documento de referencia para organizar el trabajo a lo largo de múltiples sesiones.
> Última actualización: 2026-08-03 (L05 escrito — **los 6 laboratorios están completos**)
> Actualización previa: 2026-08-03 (reestructuración a L00–L05: Fourier queda en
> un único lab continuo→discreto, muestreo pasa a L03, Laplace y Z se unen en un
> lab de dos partes, y la serie de Fourier sale del material de laboratorio)

---

## Visión general

El proyecto es el **"Curso de introducción a Python para análisis de señales y sistemas"**, pensado para publicarse como material digital.

Tiene **tres ejes de trabajo**:

| Eje | Qué | Estado actual |
|-----|-----|---------------|
| **A. Módulos** (M01–M09) | Notebooks expositivos que cubren Python de cero | M01 ✅, M02 ✅, M03 ✅, M04 ✅, M05 ✅, M06 ✅, M07 ✅, M08 ✅, M09 ✅ |
| **B. Laboratorios** (L00–L05) | Notebooks entregables que aplican los módulos | L00 ✅, L01 ✅, L02 ✅, L03 ✅, L04 ✅, L05 ✅ — **completo** |
| **C. Página de inicio** | README.md / index.md | Desactualizada; reescribir en Fase 4 |

Y un **eje transversal de infraestructura**:

| Infraestructura | Propósito |
|-----------------|-----------|
| Workflow Markdown ↔ ipynb | Editar en `.md`, convertir a `.ipynb`. Ahorra tokens, facilita diffs |
| Sistema de IDs de celdas | Identificar unívocamente cada celda y su rol (provista / alumno) |
| Rúbricas de corrección | Archivos por laboratorio que permitan corrección automatizada con IA |

---

## Fase 0 — Infraestructura y tooling (esta sesión)

### 0.1 Herramientas de conversión
- [x] `tools/nb2md.py` — Extrae notebooks existentes a formato Markdown fuente
- [x] `tools/md2nb.py` — Convierte Markdown fuente a `.ipynb`
- [x] `tools/extract_student.py` — Extrae solo las celdas del alumno para corrección

### 0.2 Convenciones
- [x] `docs/FORMATO_CELDAS.md` — Convención de IDs y roles de celdas
- [x] `docs/GUIA_ESTILO.md` — Tono, formato, estructura de los notebooks

### 0.3 Memoria de proyecto
- [x] Archivos de memoria persistente en `.claude/projects/.../memory/`
- [x] Actualización de `CLAUDE.md` con nuevo workflow

---

## Fase 1 — Auditoría y extracción ✅

### 1.1 Extraer todos los notebooks a Markdown
- [x] 13 notebooks extraídos a `src/` con `python tools/nb2md.py --all`

### 1.2 Auditoría de contenido tutorial (01–07)
Para cada tutorial, documentado:
- [x] Temas cubiertos (checklist detallado)
- [x] Conceptos que se usan sin haber sido presentados antes
- [x] Calidad de las explicaciones (1–5)
- [x] Consistencia de tono y formato
- [x] Errores o imprecisiones

### 1.3 Auditoría de contenido laboratorios (TP0–TP4)
Para cada laboratorio, documentado:
- [x] Mapa de ejercicios con dificultad estimada
- [x] Qué conceptos de Python requiere cada ejercicio
- [x] Grado de guía provisto (1: sin guía, 5: paso a paso)
- [x] Consistencia con el formato de celdas definido

### 1.4 Resultado
Archivo `docs/AUDIT_REPORT.md` generado con hallazgos detallados, matriz de acción prioritaria y mapa de renumeración.

---

## Fase 2 — Módulos del curso (varias sesiones)

> **Nomenclatura:** los notebooks expositivos se llaman **módulos** (no "tutoriales"). Prefijo de archivo `MNN_*`.

### Estructura propuesta de módulos

| # | Archivo | Tema | Dependencias |
|---|---------|------|-------------|
| 01 | M01_introduccion_colab ✅ | Qué es Colab, celdas, ejecución, Markdown básico | Ninguna |
| 02 | M02_tipos_de_datos ✅ | Variables, tipos (int, float, str, bool, complex), operaciones, conversiones, `input()` | M01 |
| 03 | M03_colecciones ✅ | Listas, tuplas, diccionarios, conjuntos, indexado, slicing | M02 |
| 04 | M04_estructuras_de_control ✅ | if/elif/else, for, while, break, continue, comprensiones | M02, M03 |
| 05 | M05_funciones ✅ | Definición, parámetros, return, scope, funciones lambda | M04 |
| 06 | M06_clases_objetos ✅ | **NUEVO**: Clases, atributos, métodos, herencia básica | M05 |
| 07 | M07_numpy ✅ | Arrays, operaciones vectorizadas, indexado, funciones matemáticas | M05, M06 |
| 08 | M08_matplotlib ✅ | Gráficos: plot, stem, subplot, scatter, formato | M07 |
| 09 | M09_sympy ✅ | Cálculo simbólico: símbolos, simplificación, `solve`, derivadas e integrales, `Piecewise`, `lambdify` | M07, M08 |

> **Nota:** Se reorganizan los temas para respetar el principio de "no usar lo que no se presentó".
> Se separa colecciones (listas/dicts) del tema de tipos básicos.
> Se agrega OOP como módulo 06.

### Principios de escritura (ver `docs/GUIA_ESTILO.md`)
- Tono: cercano pero preciso, como un tutor
- Progresión: cada ejemplo construye sobre el anterior
- Cada concepto: explicación → ejemplo → "probá vos"
- Sin conceptos huérfanos (todo se presenta antes de usarse)
- **No referenciar al profesor ni a la cátedra**: material autoconsistente, apto para publicación digital

### Orden de trabajo sugerido
1. ✅ M01 (rápido, es corto) — completado 2026-04-16
2. ✅ M02 (tipos y variables) — completado 2026-04-16
3. ✅ M03 (colecciones) — completado 2026-04-16
4. ✅ M04 (control) — completado 2026-04-16
5. ✅ M05 (funciones) — completado 2026-04-16
6. ✅ M06 (OOP, escrito desde cero) — completado 2026-04-16
7. ✅ M07 (NumPy, reescrito a partir del viejo) — completado 2026-04-16
8. ✅ M08 (Matplotlib, reescrito a partir del viejo) — completado 2026-04-16
9. ✅ M09 (SymPy, reescrito a partir del viejo) — completado 2026-04-16

---

## Fase 3 — Laboratorios: nueva estructura (varias sesiones)

### Filosofía
**Pocos laboratorios, hechos muy bien.** Se eligen en función de utilidad didáctica *y* valor a largo plazo para el uso de Python en electrónica y comunicaciones. Se privilegia profundidad sobre cobertura: temas como ecuaciones diferenciales, sistemas de tiempo discreto o DTFT no tienen lab propio y se apoyan en los labs elegidos.

### Principios de diseño
- **Dificultad ascendente**: cada lab comienza guiado paso a paso y progresa
- **Fuertemente guiados**: el objetivo es claridad, no frustración
- **Celdas claramente separadas**: `ejN-enunciado` → `ejN-code` → `ejN-pregunta` → `ejN-respuesta` (contrato del plugin `lab-notebook`)
- **Tangibilidad**: siempre que sea posible, conectar con algo físico o audible (modelo: el lab de convolución actual)
- **Hilo continuo↔discreto**: se introduce en los módulos desde el primer `np.linspace`, se profundiza en el lab de Muestreo, y se recuerda en cada lab donde aplique. Cada `.ipynb` debe aclarar qué parte trabaja en continuo y qué parte en discreto.
- **Cada ejercicio indica qué conceptos de Python necesita**
- **Preguntas de análisis**: cada ejercicio cierra pidiendo que el alumno explique lo observado, y eso también se corrige
- **Rúbrica**: la genera la app de corrección desde el par enunciado/solución

### Plan — 6 laboratorios (L00 + L01–L05)

| Lab | Archivo | Tema | Rol didáctico |
|-----|---------|------|---------------|
| L00 ✅ | `L00_practica_python` | Práctica integradora de Python | **Primer entregable del curso.** Ejercita todas las piezas de M01–M09 con escenarios nuevos (distintos a los de los módulos). Contextos de electrónica y telecomunicaciones (longitud de onda, notas musicales, bandas de radio, filtros RC, baterías, DTMF). Cierra con un mini-proyecto integrador (detector DTMF por MSE, sin Fourier). |
| L01 ✅ | `L01_senales_y_operaciones` | Señales y operaciones | **Preludio manipulativo a convolución.** Señales elementales sobre un mismo eje `t` (escalón, pulso, rampa, exponencial, senoide), desplazamiento `x(t − t₀)`, reflexión `x(−t)`, escalado y suma, producto punto a punto, recorte con slicing y máscaras. Mini-proyecto: sintetizar un "beep-beep" de alarma. |
| L02 ✅ | `L02_convolucion` | Convolución | Conservar el enfoque tangible del lab anterior (reverberación de galpón sobre grabación de violín). Dificultad graduada: definición con bucles sobre 5 muestras → flip-and-slide → LTI → audio → convolución 2D en imágenes. |
| L03 ✅ | `L03_muestreo` | Muestreo | **El puente.** Se paga acá la deuda conceptual del hilo continuo↔discreto: `fs`, `dt`, reconstrucción, criterio de Nyquist y aliasing **audible**. Explicación en el dominio del tiempo (frecuencia aparente por plegado); la lectura espectral —"el espectro se repite cada `fs`"— queda como apertura de L04. Cierra con filtrado antialiasing reusando el promediador móvil de L02. |
| L04 ✅ | `L04_fourier` | Fourier, del continuo al discreto | Lab de **dos partes**. **Parte A (continuo):** transformada de Fourier por definición, espectro del pulso rectangular, duración ↔ ancho de banda, retardo ↔ fase lineal, **teorema de convolución** y respuesta en frecuencia de los filtros de L02 (recién acá se explica por qué uno era pasa-bajos y el otro pasa-altos). **Parte B (discreto):** DFT/FFT como el cálculo efectivo sobre muestras, resolución en frecuencia, espectro de audio real (timbre: dos instrumentos en la misma nota) y proyecto de la **radio AM clandestina** — se entrega un `.wav` con una portadora a `fc` desconocida más ruido; el alumno identifica `fc` por FFT, demodula multiplicando por `cos(2π·fc·t)`, filtra con un **pasa-bajos provisto ya diseñado** y recupera el mensaje. |
| L05 ✅ | `L05_analisis_de_sistemas` | Laplace y transformada Z | Lab de **dos partes**, unificado porque es el mismo laboratorio en dos planos: mismo *toolchain* (`scipy.signal`), mismas figuras (polos y ceros, respuesta al escalón, respuesta al impulso, respuesta en frecuencia) y la misma lectura "dónde están los polos → cómo se comporta el sistema". **Parte A (Laplace):** `scipy.signal.TransferFunction`, con dos ejemplos — (a) circuito RC o RLC; (b) sistema de control **tangible** (cruise control, control de temperatura de un horno — *nunca una "planta genérica"*), mostrando el efecto de un parámetro sobre polos y respuesta transitoria. **Parte B (Z):** `scipy.signal.dlti` / `freqz`, polos y ceros en el círculo unitario, filtro IIR simple. El cierre confronta explícitamente semiplano izquierdo ↔ interior del círculo unitario, que es la analogía que se pierde cuando los dos temas se dictan por separado. |

> **Nota de numeración (2026-08-03):** esta tabla reemplaza al plan de 8 labs del
> 2026-08-02, que a su vez había reemplazado al de 9. Cambios de esta revisión:
> (a) **la serie de Fourier sale del material de laboratorio** y queda solo en
> teoría y gabinete; (b) sin la serie, la transformada continua no alcanza para
> un lab propio y **Fourier se unifica en L04**, en dos partes, continuo→discreto;
> (c) eso obliga a **adelantar muestreo a L03**, porque no se puede calcular una
> FFT sin haber fijado `fs`; (d) **Laplace y Z se unen en L05**. El lab de
> **números complejos aplicados** sigue archivado en el **Anexo A**.

### Decisiones de scoping
- **No hay lab dedicado** a: números complejos (ver Anexo A), ecuaciones diferenciales, sistemas de tiempo discreto (per se), DTFT/serie de Fourier discreta. Se cubren teóricamente y aparecen tangencialmente en L02, L03 y L04/L05.
- **La serie de Fourier no se practica en ningún lab** (decisión del 2026-08-03). Queda en teoría y gabinete. El contenido armónico llega a los labs por el lado del análisis —FFT de sonidos reales en L04— y no por el de la síntesis a partir de armónicos.
- **Álgebra compleja sin lab propio**: la base operatoria (crear complejos, `.real`, `.imag`, `abs()`) ya está en M02, y graficarlos en el plano está en M08. Lo específico se explica *in situ*: evaluación de $H(j\omega)$ sobre el eje imaginario en la Parte A de **L05**, círculo unitario en la Parte B.
- **LPF provisto en la Parte B de L04**: decisión consciente para no distraer del objetivo (modulación/demodulación/FFT) con diseño de filtros.
- **Sistema de control en la Parte A de L05**: debe partir de un sistema **tangible y fácil de entender** (el alumno debe poder imaginar físicamente qué está controlando). Nada abstracto.
- **L01 no es el lab del hilo continuo↔discreto**: ese hilo es transversal y se profundiza recién en L03 (Muestreo).
- **Muestreo antes de Fourier, y sin espectro**: L03 explica el aliasing en el dominio del tiempo —frecuencia aparente por plegado, verificada de oído— y deja la explicación espectral para la apertura de L04. Primero se escucha el fenómeno, después se ve por qué. Escribir L03 **no** requiere ningún concepto de Fourier.

### Entregable por cada laboratorio

> **Cambio de toolchain (2026-08-02):** los laboratorios pasaron al contrato del
> plugin `lab-notebook`. Ya no se escriben como `src/Lx.md` + `md2nb.py`. Ver la
> sección "two different toolchains" de `CLAUDE.md`. Los **módulos** siguen con
> el flujo viejo (`src/*.md` + `md2nb.py`), que no cambió.

- Fuente única `_fuente/sources/Lx_tema.lab.md` — enunciado y solución juntos,
  en el repo **privado** (`_fuente/` está en `.gitignore`, porque este repo es
  público y la fuente lleva las respuestas adentro).
- Enunciado generado `Laboratorios/Lx_tema.ipynb` — es lo único que se publica.
- Solución generada `_fuente/Soluciones/Lx_tema_Solucion.ipynb`, **ejecutada y
  guardada con sus outputs** (los necesita la app para armar la rúbrica).
- Validación con `lab_validate.py` en cero errores antes de dar el lab por hecho.
- Rúbrica: la genera la app de corrección desde el par enunciado/solución. No se
  escribe a mano.

Cada lab lleva, además del código, **preguntas de análisis** (`ejN-pregunta` +
`ejN-respuesta`): el alumno explica con sus palabras qué observó. Es un rol que
el formato viejo no tenía y que ahora se corrige junto con el código.

---

## Anexo A — Laboratorios diferidos

> Trabajo de diseño ya hecho y **aprobado**, que no se dicta en la edición
> actual pero se quiere conservar. No está descartado: está en pausa. Al
> retomarlo, mover la ficha de vuelta a la tabla de Fase 3 y renumerar.

### A.1 — Números complejos aplicados

- **Estado:** diferido el **2026-08-02**. Diseñado el 2026-04-16, nunca escrito
  (no existe `src/` ni `.ipynb`).
- **Motivo del diferimiento:** decisión de cátedra para esta edición. La
  intención declarada es **retomarlo en la edición siguiente**.
- **Ubicación prevista al retomarlo:** entre L00 y el actual L01
  (Señales y operaciones), es decir como primer lab después del integrador de
  Python. Todo lo posterior corre un número hacia arriba.
- **Nota del 2026-08-03:** con la reestructuración a 6 labs hay lugar de sobra
  para reincorporarlo sin que el cuatrimestre quede sobrecargado.

**Justificación didáctica original:** con el material previo (L00 y los
módulos) el alumno ya tiene las herramientas para trabajar con complejos de
forma tangible; los complejos son además prerrequisito operativo para todo lo
que viene. No se ubican temprano porque conceptualmente sean anteriores, sino
porque es lo que está más a mano y ayuda visualmente (rotación, círculo,
espiral).

**Restricción didáctica clave:** los alumnos en ese punto del cursado **no
saben nada de impedancia, fasores, ni principios básicos de electricidad**
(algunos todavía no cursaron la Física correspondiente; "fasor" lo ven en una
instancia posterior). → El lab se ancla en **geometría y cinemática** (cosas
que rotan, oscilan, se apagan), nunca en circuitos eléctricos.

**Scope aprobado** (orden tentativo):

1. Repaso operatorio: `j`, binómica ↔ polar, `abs(z)`, `np.angle(z)`.
2. Complejo como punto en el plano. `plt.scatter(z.real, z.imag)` con
   `axhline`/`axvline`. Suma de complejos = regla del paralelogramo.
3. Multiplicación como giro: `z0` multiplicado repetidamente por
   $e^{j\varphi}$ (φ = 30°) genera 12 puntos en el círculo.
   Anclaje: **aguja de reloj hora a hora**.
4. Exponencial compleja $e^{j\omega t}$ como *punto que gira en el tiempo*.
   Graficar en el plano (círculo) y `Re`/`Im` vs `t` (sinusoides desfasadas
   90°). Anclaje: **punta de aguja de reloj o punto sobre un disco que gira**.
5. **"La sombra de un punto que gira es una senoide"** — ejercicio central.
   Vincular *"visto desde arriba"* (plano complejo) con *"visto de costado"*
   (onda en el tiempo). Introduce la exponencial compleja como forma natural
   de describir lo que oscila, **sin nombrar "fasor"**.
6. Exponencial compleja amortiguada $e^{(-\alpha + j\omega)t}$: la espiral.
   Anclaje: **trompo que gira y se cae, péndulo que se detiene**. Preview mudo
   de decaer+oscilar, sin Laplace ni polos.
7. Mini-proyecto: curva de **Lissajous** combinando dos exponenciales de
   frecuencias proporcionales (1:2, 2:3). Cierre visualmente fuerte.

**Fuera de alcance:** impedancia, fasor (palabra y concepto), fracciones
parciales / `apart`, evaluación de $H(j\omega)$ como "transferencia" (va a
Laplace), círculo unitario como dominio de Z (va al lab de Z).

**Mientras el lab no exista**, sus prerrequisitos se cubren así: la base
operatoria de complejos está en M02 y graficarlos en el plano está en M08;
$H(j\omega)$ se explica *in situ* en L04 y el círculo unitario en L07. Lo que
queda genuinamente sin práctica es la **exponencial compleja $e^{j\omega t}$
y la espiral amortiguada**; si se extraña, el lugar natural para una sección
corta es la Parte A de L04 (Fourier).

### Mapa de transición desde los TPs anteriores

> **Los TP ya no viven en el repo.** Desde 2026-08-02 están en `_legacy/`
> (carpeta local, ignorada por git) y sirven solo como insumo de redacción.

| TP anterior | Destino |
|-------------|---------|
| TP0 (Python básico) | → L00 (Práctica integradora, escenarios nuevos) ✅ — ya consumido |
| TP1 (Variable compleja) | → aporta su parte de **operaciones sobre señales** a L01. La parte de variable compleja queda sin destino en esta edición (ver Anexo A) |
| TP2 (Convolución) | → L02 — conservar, pulir |
| TP3 (Fourier continuo) | → L04 Parte A. **Su sección 1 (serie trigonométrica) y su sección 2 (serie exponencial) no se reutilizan**: la serie sale del material de laboratorio |
| TP4 (FFT y LTI) | → L04 Parte B (FFT y modulación) + material a repartir entre las dos partes de L05 |
| — | → L03 Muestreo (**nuevo**) |
| — | → L05 Parte A, Laplace (**nuevo**) |
| — | → L05 Parte B, Z (**nuevo**) |

---

## Fase 4 — Página de inicio (una sesión)

### Cambios necesarios en README.md / index.md
- [ ] Eliminar "Fecha de entrega de laboratorio n° 4: Domingo 23/11"
- [ ] Eliminar aviso rojo de "nueva metodología de entrega" (ya no es nueva)
- [ ] Actualizar tabla de notebooks con la nueva numeración (01–09)
- [ ] Agregar tabla de laboratorios actualizada
- [ ] Revisar texto introductorio
- [ ] Asegurar que los links de Colab apunten a los archivos correctos

---

## Convenciones de archivos

```
proyecto/
├── docs/
│   ├── PROJECT_PLAN.md          ← Este archivo
│   ├── FORMATO_CELDAS.md        ← Convenciones de IDs y roles
│   ├── GUIA_ESTILO.md           ← Guía de estilo editorial
│   └── AUDIT_REPORT.md          ← (se genera en Fase 1)
├── tools/
│   ├── md2nb.py                 ← Markdown → ipynb
│   ├── nb2md.py                 ← ipynb → Markdown
│   └── extract_student.py       ← Extractor para corrección
├── src/                         ← Fuentes Markdown de notebooks
│   ├── T01_introduccion_colab.md
│   ├── ...
│   ├── TP0_python_basico.md
│   └── ...
├── rubrics/                     ← Rúbricas de corrección
│   ├── TP0_rubric.md
│   └── ...
├── *.ipynb                      ← Archivos generados (output)
├── CLAUDE.md                    ← Instrucciones para Claude Code
└── README.md / index.md         ← GitHub Pages
```

---

## Seguimiento de progreso

| Fase | Estado | Sesión estimada |
|------|--------|----------------|
| 0. Infraestructura | ✅ Completada | Sesión 1 |
| 1. Auditoría | ✅ Completada | Sesión 2 |
| 2. Módulos | ✅ Completada (M01–M09) | Sesiones 3–6 |
| 3. Laboratorios (L00 + L01–L05) | ✅ Completada (L00–L05 escritos, validados y con solución ejecutada) | Sesiones 7–10 |
| 4. Página inicio | ✅ Overhaul aplicado (se irá actualizando con cada Lx nuevo) | Hecho 2026-04-16 |

> Las sesiones son orientativas. Cada una puede subdividirse según la complejidad encontrada.
