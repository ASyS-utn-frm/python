# Plan Maestro — Curso de introducción a Python para ASyS

> Documento de referencia para organizar el trabajo a lo largo de múltiples sesiones.
> Última actualización: 2026-04-16 (M01–M09 + L00 completados)

---

## Visión general

El proyecto es el **"Curso de introducción a Python para análisis de señales y sistemas"**, pensado para publicarse como material digital.

Tiene **tres ejes de trabajo**:

| Eje | Qué | Estado actual |
|-----|-----|---------------|
| **A. Módulos** (M01–M09) | Notebooks expositivos que cubren Python de cero | M01 ✅, M02 ✅, M03 ✅, M04 ✅, M05 ✅, M06 ✅, M07 ✅, M08 ✅, M09 ✅ |
| **B. Laboratorios** (L00–L08) | Notebooks entregables que aplican los módulos | L00 ✅, L01–L08 pendientes |
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
- **Celdas claramente separadas**: `enunciado` → `actividad` (ver `FORMATO_CELDAS.md`)
- **Tangibilidad**: siempre que sea posible, conectar con algo físico o audible (modelo: el lab de convolución actual)
- **Hilo continuo↔discreto**: se introduce en los tutoriales desde el primer `np.linspace`, se profundiza en el lab de Muestreo, y se recuerda en cada lab donde aplique. Cada `.ipynb` debe aclarar qué parte trabaja en continuo y qué parte en discreto.
- **Cada ejercicio indica qué conceptos de Python necesita**
- **Rúbrica asociada**: archivo en `rubrics/` para corrección automatizada

### Plan — 9 laboratorios (L00 + L01–L08)

| Lab | Tema | Rol didáctico |
|-----|------|---------------|
| L0 ✅ | Práctica integradora de Python | **Primer entregable del curso.** Ejercita todas las piezas de M01–M09 con escenarios nuevos (distintos a los de los módulos). Contextos de electrónica y telecomunicaciones (longitud de onda, notas musicales, bandas de radio, filtros RC, baterías, DTMF). Cierra con un mini-proyecto integrador (detector DTMF por MSE, sin Fourier). |
| L1 | Python aplicado a señales | Cierre conceptual de los módulos. Planta la bandera del hilo continuo↔discreto (muestras vs. señal, rol de `dt`, diferencia entre graficar "denso" y muestrear). |
| L2 | Variable compleja aplicada | Fracciones simples de funciones racionales; evaluación de módulo y fase sobre eje `jω` **y** sobre la circunferencia unitaria. Preludio común de Laplace y Z. |
| L3 | Convolución | Conservar el enfoque tangible del lab actual (favorito del docente). Graduar dificultad inicial. |
| L4 | Fourier de tiempo continuo | Serie + transformada en un mismo lab. Hacer explícita la tensión "lo que pido es continuo, lo que calculo es discreto". |
| L5 | Laplace — análisis de sistemas | Estilo MATLAB con `scipy.signal.TransferFunction`: respuesta al escalón, impulso, Bode, polos/ceros. **Dos ejemplos:** (a) circuito RC o RLC; (b) sistema de control **tangible** (cruise control de auto, control de temperatura de horno, o similar — *nunca algo abstracto tipo "planta genérica"*). Mostrar efecto de un parámetro (p.ej. ganancia proporcional) sobre polos y respuesta transitoria. |
| L6 | Muestreo | El puente. Se paga aquí la deuda conceptual del hilo continuo↔discreto, con aliasing tangible (audio si es posible). |
| L7 | FFT + modulación lúdica | "Radio AM clandestina": se entrega un `.wav` con **una sola portadora AM** a `fc` desconocida más ruido, transportando un mensaje reconocible (melodía corta, tono DTMF, o palabra codificada). El alumno: (1) FFT → identifica `fc`, (2) demodula multiplicando por `cos(2π·fc·t)`, (3) filtra pasa-bajos **con un LPF provisto ya diseñado** (coeficientes listos — el foco no es diseño de filtros), (4) recupera/decodifica el mensaje. |
| L8 | Transformada Z — sistemas discretos | Estilo MATLAB con `scipy.signal.dlti` / `freqz`: polos y ceros en el círculo unitario, respuesta en frecuencia, respuesta al impulso. Diseño/análisis de un filtro IIR simple. |

### Decisiones de scoping
- **No hay lab dedicado** a: ecuaciones diferenciales, sistemas de tiempo discreto (per se), DTFT/serie de Fourier discreta. Se cubren teóricamente y aparecen tangencialmente en los labs 3, 6 y 7/8.
- **L2 cumple doble función**: evita la necesidad de labs separados "introductorios" a Laplace y Z, porque los prerrequisitos de álgebra compleja se concentran ahí.
- **LPF provisto en L7**: decisión consciente para no distraer del objetivo (modulación/demodulación/FFT) con diseño de filtros.
- **Sistema de control en L5**: debe partir de un sistema **tangible y fácil de entender** (el alumno debe poder imaginar físicamente qué está controlando). Nada abstracto.

### Entregable por cada laboratorio
- Archivo fuente `src/Lx_tema.md` con celdas marcadas
- Archivo generado `Lx_tema.ipynb`
- Rúbrica `rubrics/Lx_rubric.md`

### Mapa de transición desde los TPs actuales
| TP actual | Destino |
|-----------|---------|
| TP0 (Python básico) | → L0 (Práctica integradora, escenarios nuevos) + L1 (Python aplicado a señales, foco continuo↔discreto) |
| TP1 (Variable compleja) | → L2 (Variable compleja aplicada) — reorientar hacia fracciones simples y evaluación sobre jω / círculo unitario |
| TP2 (Convolución) | → L3 — conservar, pulir |
| TP3 (Fourier continuo) | → L4 |
| TP4 (FFT y LTI) | → L7 (parte FFT/modulación) + material a repartir entre L5/L8 |
| — | → L5 Laplace (**nuevo**) |
| — | → L6 Muestreo (**nuevo**) |
| — | → L8 Z (**nuevo**) |

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
| 3. Laboratorios (L00 + L01–L08) | 🔶 En curso (L00 ✅) | Sesiones 7–11 |
| 4. Página inicio | ✅ Overhaul aplicado (se irá actualizando con cada Lx nuevo) | Hecho 2026-04-16 |

> Las sesiones son orientativas. Cada una puede subdividirse según la complejidad encontrada.
