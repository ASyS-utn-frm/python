# Carryovers — decisiones transversales entre notebooks

Este archivo registra **decisiones que se toman al mejorar un notebook pero que
se deben aplicar en otro** (típicamente: "este tema lo sacamos de acá y va en
el siguiente"). Sirve como lista de pendientes inter-notebooks.

Cuando se trabaja sobre un notebook destino, **revisar primero este archivo**
para incorporar los carryovers pendientes y luego moverlos a "✅ Aplicados".

---

## ⬜ Pendientes

### Origen: reestructuración (2026-08-03) → Destino: L03, L04, L05

**El curso pasa de 8 laboratorios a 6.** Decisión del usuario, tomada al
revisar la carga del cuatrimestre antes de escribir el lab siguiente. Detalle
completo y justificación en la tabla de Fase 3 de `docs/PROJECT_PLAN.md`.

Numeración vigente: **L00 + L01–L05**.

| Antes | Ahora |
|---|---|
| L03 Fourier continuo (serie + transformada) | **sale la serie**; la transformada va a L04 Parte A |
| L04 Laplace | L05 Parte A |
| L05 Muestreo | **L03** |
| L06 FFT + modulación | L04 Parte B |
| L07 Z | L05 Parte B |

Pendientes que esto deja:

- **La serie de Fourier no se practica en ningún laboratorio.** Queda en
  teoría y gabinete. Al escribir L04 **no** reutilizar las secciones 1 y 2 del
  viejo `_legacy/src/TP3_analisis_de_fourier.md` (serie trigonométrica y serie
  exponencial), que eran la mitad de ese TP. El contenido armónico entra por el
  análisis —FFT de sonidos reales— y no por la síntesis a partir de armónicos.
- **L03 (Muestreo) no puede usar nada de Fourier.** El aliasing se explica en
  el dominio del tiempo, con la frecuencia aparente por plegado y verificación
  de oído. La lectura espectral ("el espectro se repite cada `fs`") es la
  apertura de L04 y hay que escribirla ahí como pago explícito de esta deuda:
  L03 cierra diciendo que se escucha el fenómeno pero todavía no se ve por qué.
- **L05 debe confrontar los dos planos.** La razón de unir Laplace y Z es
  justamente que el semiplano izquierdo y el interior del círculo unitario son
  la misma idea. Si las dos partes quedan escritas como labs independientes
  pegados, la unificación no aporta nada.
- **README/index:** al publicar cada lab nuevo va su fila; la nota sobre
  "L01–L08 en desarrollo" quedó desactualizada por partida doble y hay que
  ajustarla a L01–L05.

### Origen: L02 (2026-08-03) → Destino: repo público, L03 y L04

- **Audios en el repo público.** L02 descarga sus dos `.wav` desde
  `resources/audios/` vía `raw.githubusercontent.com`, y **L03 descarga
  `violin.wav` del mismo lugar**. **Ninguno de los dos notebooks funciona en
  Colab hasta que esos archivos estén commiteados y pusheados a `main`**;
  al 2026-08-03 `resources/audios/` sigue sin trackear. Créditos en
  `resources/audios/CREDITOS.md` (freesound.org: 180960 de kleeb y 92002 de
  jcveliz). Si en el futuro se agregan audios para otros labs, va la misma
  carpeta y se actualiza ese archivo.
- **`_fuente/Soluciones/audios/`** es una copia local de esos `.wav` que
  existe solo para poder ejecutar la solución antes del push (la celda de
  descarga los saltea si ya están). No hace falta versionarla.
- **Nueva dependencia: `scikit-image`.** La usa la sección D de L02
  (`data.camera()`, `data.coins()`). Viene preinstalada en Colab; hay que
  tenerla en cuenta si alguna vez se arma un `requirements.txt`.
- **Promesa hecha en el cierre de L02 → aplicar en L04 Parte A.** El footer
  anuncia que convolucionar en el tiempo equivale a multiplicar transformadas,
  y que esa es la razón por la que `signal.convolve` resuelve en segundos lo
  que con bucles llevaría media hora. Con la reestructuración del 2026-08-03 el
  cierre de L02 se reescribió para anunciar muestreo (L03) en vez de Fourier,
  **pero la promesa del teorema de convolución se conservó** apuntando a L04.
  Hay que pagarla ahí.
- **Arrays de dos dimensiones: presentados in situ en L02.** `src/M07_numpy.md`
  muestra una matriz de 2x3 y declara explícitamente que "no vamos a
  profundizar en 2D por ahora… aparecerán de forma natural cuando, en algún
  laboratorio, guardemos varias señales juntas". L02 es ese laboratorio, pero
  el caso no es "varias señales juntas": son el audio estéreo (sección C) y la
  imagen (sección D). Por eso L02 presenta en sus propias celdas el *slicing*
  con dos rangos (`I[100:106, 200:208]`, `h[:, 0]`), la representación de una
  imagen en escala de grises (`uint8`, 0 negro / 255 blanco, `shape` como
  filas × columnas) y `imshow` con `cmap="gray"`, que M08 tampoco cubre.
  **Decidir para la próxima edición** si eso vuelve a M07/M08 o se deja acá.
- **Anclaje disponible, ahora repartido entre L03 y L04.** L02 deja hechos y
  ejecutados el promediador móvil (ejercicio 4) y los kernels pasa-bajos /
  pasa-altos (ejercicio 9), presentados como filtros pero **sin** ningún
  argumento frecuencial. **L03** reusa el promediador móvil como filtro
  antialiasing antes de submuestrear, todavía sin espectro. **L04 Parte A**
  calcula su respuesta en frecuencia y recién ahí explica por qué uno era
  pasa-bajos y el otro pasa-altos.

### Origen: sesión 2026-08-02 → Destino: L01 (por escribir)

**Numeración vigente: L00 + L01–L07** (ver tabla de Fase 3 en
`docs/PROJECT_PLAN.md`). El lab de números complejos **no se dicta en
esta edición**; su scope completo quedó archivado en el **Anexo A** del
plan, con la intención declarada de retomarlo en la edición siguiente.
No borrar ese anexo.

#### L01 — "Señales y operaciones" (preludio manipulativo a convolución)

Scope aprobado en la sesión 2026-04-16 (donde figuraba como L02). Queda
sin cambios de contenido; solo cambió el número.

- **Rol didáctico:** preludio manipulativo a convolución. **No** es
  un lab sobre el hilo continuo↔discreto: ese hilo es transversal y
  se profundiza recién en L05 (Muestreo), como dicen los Principios
  de diseño del plan.
- **Scope aprobado** (orden tentativo, todas con contexto físico/
  audible):
  1. Construir señales elementales sobre un mismo eje `t`: escalón,
     pulso rectangular, rampa, exponencial decreciente, senoide
     (disparo de circuito, batería descargándose, diapasón).
  2. Desplazamiento temporal `x(t − t₀)`: eco de un pulso.
  3. Reflexión `x(−t)` (clave visual para convolución).
  4. Escalado de amplitud y suma: acorde musical; batido entre
     frecuencias cercanas.
  5. Producto punto a punto: ventaneo de una senoide con un pulso
     (pulso de radar) o envolvente decreciente sobre tono (nota de
     guitarra que se apaga).
  6. Recorte temporal con slicing / máscaras booleanas.
  7. Mini-proyecto: sintetizar un "beep-beep" de alarma (dos ráfagas
     de tono separadas por silencio) usando solo las operaciones de
     arriba; graficar y reproducir.
- **Fuera de alcance en L01:** convolución, Fourier, filtros,
  muestreo/aliasing, números complejos.

#### Cierre de L00 — ya aplicado

Se eliminó la promesa específica *"profundizar qué significa
representar una señal en la computadora (muestras vs. señal continua,
rol de `dt`)"*; ahora dice solo *"estás listo para entrar al
Laboratorio 1."* Cambio aplicado en el `.ipynb` (a mano por el usuario)
y sincronizado en `src/L00_practica_python.md` (prov-15).

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

- Cuando se escriba cada laboratorio nuevo (L01–L07), agregar su fila
  en la tabla "Laboratorios" del README/index con el link Colab
  correspondiente.
- ~~A medida que cada Lx reemplace a un TPn, borrar la fila
  correspondiente de "Material de ediciones anteriores".~~ Resuelto de
  una vez el 2026-08-02: los TP salieron del repo a `_legacy/` y esa
  sección ya no existe en README/index.

### Origen: revisión de coherencia L01↔módulos (2026-08-02) → Destino: M07, M08 (edición siguiente)

**Los módulos M01–M09 están publicados y NO se tocan en esta edición.** Lo que
sigue es la lista de huecos detectados al revisar L01 contra `src/M0*.md`, para
aplicar cuando se corrijan los módulos el año que viene. Mientras tanto, **cada
lab debe presentar por su cuenta lo que necesite de esta lista**, sin dar por
sentado que el alumno lo vio.

- **M07 — falta por completo la sección de comparaciones y máscaras booleanas.**
  Es el hueco más grande. M07 tiene "Indexado y *slicing*" (§7) y "Agregación"
  (§8), pero nunca compara un array (`t >= 0`), ni usa `&` entre arrays, ni
  `.astype(float)`, ni indexa con una máscara (`x[mascara]`). Es la técnica
  base para construir señales por tramos (escalón, pulso, ventana), así que la
  necesitan L01 y todos los labs que sigan. **Propuesta:** sección nueva entre
  §7 y §8, "Comparaciones y máscaras booleanas", con el par
  comparación → array de booleanos → `.astype(float)` para señales, y
  → indexado para recortar. Debe contrastar `&`/`|` con el `and`/`or` de M02,
  que no funcionan sobre arrays.
- **M07 — `np.argmin` / "encontrar el índice de un instante".** El patrón
  `np.argmin(np.abs(t - instante))` aparece en todos los labs que verifican un
  valor en un tiempo dado. Hoy hay que darlo como pista cada vez.
- **M07 — `endpoint=False` en `np.linspace`.** §3.3 y la tabla de "cuándo usar
  cada una" dicen que linspace incluye **ambos** extremos, y el parámetro no se
  menciona. Es justo lo que hace falta para ejes de audio y para señales que se
  repiten sin muestra doble.
- **M07 — `.size` vs `.shape`.** `.size` se nombra una sola vez de pasada
  (línea 74) y la Actividad 3 pide `.shape`. Los labs usan `.size` en todos
  lados; conviene fijarlo en el módulo.
- **M07 — `np.clip` y `np.tile`.** Menores, pero útiles: `clip` para señales
  definidas por tramos y `tile` para patrones que se repiten.
- **M08 — `sharex=True`.** §7 explica *conceptualmente* que los paneles
  comparten el eje x ("alcanza con etiquetarlo una vez") pero nunca muestra el
  argumento. Un lab que pida paneles con eje compartido no tiene de dónde
  sacarlo.
- **M08 — `linestyle=` por nombre.** Solo está el atajo estilo MATLAB (`"r--"`)
  y `color=`. Conviene mostrar `linestyle="--"` explícito, que es lo que se usa
  para dibujar envolventes sobre una señal.
- **M08 — colores `tab:`.** El módulo usa `color="red"`; los labs usan
  `color="tab:orange"` y similares. Unificar en la paleta `tab:`.
- **Ningún módulo presenta `IPython.display.Audio`.** No aparece en M01–M09 ni
  en L00, y varios labs producen sonido. Faltan además las dos trampas
  asociadas: (a) el `Audio(...)` tiene que ser **la última expresión de la
  celda** para que se vea el reproductor; (b) `Audio` trae `normalize=True`
  por defecto y **reescala la señal para que su pico llegue al tope del
  rango**, de modo que la amplitud del array deja de tener efecto audible —
  hay que pasar `normalize=False` siempre que la amplitud sea parte de lo que
  se quiere enseñar. Con `normalize=False` la celda además **falla** si algún
  valor sale de `[-1, 1]`, no recorta. **Propuesta:** presentarlo en M08 (o en
  M01, junto con lo que Colab sabe mostrar), no en cada lab.

---

## ✅ Aplicados

- **2026-08-03** — **Reestructuración a 6 labs y L03 (Muestreo) escrito.**
  Detalle de la reestructuración arriba, en Pendientes. Lo hecho en esta sesión:
  - `PROJECT_PLAN.md`: tabla de Fase 3 rehecha (L03 Muestreo, L04 Fourier en dos
    partes, L05 Laplace + Z en dos partes), decisiones de scoping, mapa de
    transición desde los TP y tabla de seguimiento.
  - **Cierre de L02 reescrito.** Anunciaba "En el Laboratorio 3 vas a abordar el
    análisis de Fourier". Ahora anuncia muestreo, partiendo de una deuda que el
    propio L02 dejó planteada —usó `fs = 44100` y exigió que las dos señales la
    compartieran sin explicar de dónde salía—, y difiere a L04 la promesa del
    teorema de convolución, que se conservó textualmente. L02 regenerado y su
    solución **reejecutada y guardada con outputs** (15 celdas de código, 0
    errores, 4 reproductores).
  - **L03 escrito**: 9 ejercicios en 4 secciones — `fs`/`dt`/`N` y la misma
    senoide a cuatro frecuencias de muestreo; reconstrucción lineal contra
    retención de orden cero; dos señales con las mismas muestras; aliasing
    audible (3000 Hz a `fs` = 4000 suena a 1000 Hz); la función
    `frecuencia_aparente` y la curva de plegado; barrido que sube, rebota y baja;
    el caso crítico $f = f_s/2$ donde la amplitud medida depende de la fase;
    decimación con y sin filtro antialiasing; y mini-proyecto de degradación del
    violín de L02 a 22050, 8820 y 4410 Hz. 18 ítems corregibles.
    `lab_validate.py`: 0 errores, 0 avisos. Solución ejecutada y guardada con
    outputs (15 reproductores, 9 gráficos, sin errores).
  - README/index: fila de L03 agregada y la nota de "L03 a L07 en desarrollo"
    corregida a "L04 y L05".

  **Defecto encontrado y corregido durante la verificación:** en el ejercicio 2
  el error máximo de las dos reconstrucciones daba 0,99 y 1,00, es decir
  indistinguibles. La causa era que `np.interp` y la retención repiten el último
  valor más allá de la última muestra, y ese tramo de **extrapolación**
  dominaba el máximo. Restringido el cálculo al tramo cubierto por las muestras
  (`t_ref <= t_20[-1]`), los errores pasan a 0,2105 y 1,0000, que es la
  comparación que el ejercicio quería mostrar. El enunciado ahora explica por
  qué se restringe y la solución imprime además el valor sin restringir, como
  contraste. **Cuidado al escribir ejercicios de reconstrucción o interpolación:
  el borde derecho miente.**

  **Nota sobre el ejercicio 8:** las atenuaciones del promediador móvil de 8
  muestras están medidas, no estimadas: 0,964 (−0,3 dB) a 300 Hz y 0,163
  (−15,7 dB) a 3400 Hz. Los tonos se eligieron para que el plegado dé un valor
  bien separado del útil (3400 Hz a `fs` = 2000 se presenta como 600 Hz). Evitar
  3000 Hz, que cae exactamente sobre la frecuencia de Nyquist y da un caso
  degenerado.

- **2026-08-02** — **L01: `Audio(..., normalize=False)` en todas las
  reproducciones.** Detectado al revisar un reporte de audio del usuario. `Audio`
  trae `normalize=True` por defecto y reescala cada señal para que su pico llegue
  al tope del rango; verificado midiendo el pico del WAV generado: amplitudes
  `0.5`, `0.25` y `0.6` producían las tres un pico de 32767 en `int16`. Eso
  **invalidaba la pregunta de análisis del ejercicio 3**, que pide comparar cómo
  se escucha la señal al bajar la amplitud de `0.5` a `0.25`: sonaban idénticas.
  Cambios en `L01_senales_y_operaciones.lab.md`:
  - `normalize=False` en las 7 apariciones de `Audio(...)` (6 celdas de código
    más la referencia del enunciado del ej3).
  - `setup-reproducir-intro` reescrita: explica qué hace la normalización y por
    qué acá conviene desactivarla, antes de la lista de advertencias.
  - Corregida la afirmación de que fuera de `[-1, 1]` la señal "se recorta
    (*clipping*)". Es falsa en los dos modos: con el default se reescala, y con
    `normalize=False` la celda aborta con
    `Audio data must be between -1 and 1 when normalize=False`. Ajustados en el
    mismo sentido los comentarios de solución del ej3 (`A = 0.5`) y del ej6
    (división por 3 del acorde).
  - Verificado que ninguna de las 6 señales excede el límite: los picos son
    0,300 / 0,500 / 0,9997 / 0,99998 / 0,599 / 0,500. `acorde` y `batido` quedan
    al filo pero están acotadas por construcción (`(do+mi+sol)/3` y `0.5 + 0.5`)
    y el chequeo de IPython solo falla con pico **estrictamente mayor** que 1.
  - **Cuidado al escribir labs futuros con audio:** cualquier señal nueva tiene
    que quedar dentro de `[-1, 1]` por construcción, o la celda del alumno
    revienta en lugar de sonar distorsionada.

  `lab_validate.py`: 0 errores, 0 avisos. Solución reejecutada y guardada con
  outputs (2,0 MB, 6 reproductores WAV embebidos, sin errores en ninguna celda).

  Nota aparte, no era un defecto: el usuario reportaba una especie de eco al
  final de los tonos. Las señales terminan al 6 % de su pico, un transitorio de
  unos −24 dBFS, y el efecto desaparecía al cambiar de posición en la sala. Era
  acústica del ambiente, no del notebook. No se cambió nada por eso.

- **2026-08-02** — **L01 hecho autocontenido frente a los módulos publicados.**
  Decisión del usuario: **M01–M09 ya se publicaron y no se tocan en esta
  edición**; los labs se redactan usando los módulos tal como están y
  presentando por su cuenta lo que les falte. Los huecos detectados quedaron
  anotados arriba, en Pendientes, para la revisión del año que viene.
  Cambios en `L01_senales_y_operaciones.lab.md`:
  - Celda provista nueva (`setup-mascaras`) que presenta comparaciones sobre
    arrays, `.astype(float)`, `&`/`|` contrastados con el `and`/`or` del
    Módulo 2, e indexado por máscara, sobre un eje de juguete de 9 puntos para
    que los arrays se lean enteros. Cierre que anticipa la pregunta del ej8.
  - Celdas provistas nuevas (`setup-reproducir`) que presentan `Audio` como
    herramienta de Colab, con las advertencias que si no parecen fallas:
    tiene que ser la **última línea de la celda**, los valores van dentro de
    −1 a 1, y hay que apretar *play*. Incluye tono de prueba para verificar
    que el audio funciona antes de llegar al ejercicio 3. (Ampliado el mismo
    día con `normalize=False`; ver la primera entrada de esta lista.)
  - Pistas nuevas o ampliadas: `sharex=True` (ej1, referida desde ej4 y
    contrastada en ej8), `np.argmin(np.abs(...))` explicado en vez de solo
    enunciado (ej2), `linestyle=` por nombre contra el atajo `"r--"` del
    Módulo 8 (ej7), `np.tile` y el eje que hace falta para graficarlo (ej9).
  - `endpoint=False` explicado en la intro de `setup-audio`, porque el
    Módulo 7 dice explícitamente que `linspace` incluye ambos extremos.
  - Vocabulario: "subgráficos" → "**paneles**", como en el Módulo 8. Se
    agregaron referencias explícitas a los Módulos 2, 7 y 8, que antes no
    aparecían en ningún lado del lab (L00 las tiene 9 veces).
  - Todo verificado en clave Colab: solo NumPy, Matplotlib e `IPython.display`,
    sin archivos externos ni instalaciones.

  Resultado: `lab_validate.py` da **0 errores, 0 avisos** — 9 ejercicios,
  19 ítems corregibles (10 de código, 9 de análisis). La solución quedó
  ejecutada y guardada con outputs, con sus 6 reproductores de audio.

- **2026-08-02** — **L01 escrito y L00 migrado al contrato `lab-notebook`.**
  L01 (`L01_senales_y_operaciones`) escrito desde cero con el scope aprobado:
  9 ejercicios en 5 secciones — escalón y pulso por comparaciones sobre `t`,
  exponencial de descarga de un capacitor, senoide de diapasón con audio,
  desplazamiento como eco de sonar, reflexión `x(-t)` con una rampa saturada,
  suma (acorde de Do mayor / batido de 3 Hz entre 440 y 443 Hz, en dos partes
  `ej6-code-a` y `-b`), producto punto a punto (nota de guitarra que se apaga),
  recorte por slicing vs. máscara booleana, y mini-proyecto del "beep-beep" de
  alarma con `np.tile`. 19 ítems corregibles. L00 migrado sin cambiar el
  contenido de los enunciados: se renombraron los `cell_id` (`act-NN` →
  `ejN-code`), se cambió el placeholder a `# Tu código aquí`, se incorporaron
  las soluciones desde la rúbrica vieja y se agregaron **9 preguntas de
  análisis** nuevas (por qué la antena de AM es enorme, diccionario vs. listas
  paralelas, `if/elif` vs. `if` sueltos, por qué los dB se suman, qué gana una
  clase, por qué los RMS se suman en cuadratura, `stem` vs. `plot`, qué aporta
  el despeje simbólico, y por qué el detector por MSE funciona y cuándo
  fallaría). 18 ítems corregibles. Los dos labs validan con cero errores y sus
  soluciones ejecutan limpias.

  **Consecuencias estructurales** (detalle en `CLAUDE.md`): los enunciados pasan
  a `Laboratorios/`; las fuentes `.lab.md` y las soluciones viven en un repo
  privado montado como `_fuente/` e ignorado por git, porque este repo es
  público y la fuente lleva las respuestas adentro. `rubrics/L00_rubric.md`
  **estaba publicado con las soluciones de referencia** y se movió a
  `_fuente/rubricas/`. El `L00_practica_python.ipynb` viejo de la raíz y su
  `src/*.md` quedaron en `_legacy/formato_viejo/`. `docs/FORMATO_CELDAS.md`
  pasa a aplicar solo a los módulos. README/index actualizados: L00 apunta al
  path nuevo, se agregó L01 y se corrigió el placeholder en las instrucciones
  de entrega.

  **(Resuelto)** El repo privado ya existe y está pusheado:
  `git@github.com:ASyS-utn-frm/python-fuente.git`. Las fuentes de los labs
  tienen respaldo fuera de este disco. Recordar que `_fuente/` es un repo
  **aparte**: commitear ahí los cambios de `.lab.md` y de las soluciones es un
  paso separado del commit del repo público.

- **2026-08-02** — **Renumeración de laboratorios y archivo del lab de
  complejos.** Decisión del usuario: no se dicta un lab de números
  complejos en esta edición, pero **probablemente sí en la siguiente**,
  así que el trabajo de diseño no se descarta. Cambios: (a) el lab de
  complejos sale de la tabla de Fase 3 y su scope completo se archiva
  íntegro en el nuevo **Anexo A — Laboratorios diferidos** de
  `PROJECT_PLAN.md` (justificación, restricción didáctica sobre
  fasores/electricidad, los 7 puntos del scope, fuera de alcance, y una
  nota de dónde se cubren mientras tanto sus prerrequisitos); (b) el lab
  de "Señales y operaciones" pasa de L02 a **L01** y todo lo posterior
  corre un número: la numeración vigente es **L00 + L01–L07**
  (L01 señales y operaciones, L02 convolución, L03 Fourier continuo,
  L04 Laplace, L05 muestreo, L06 FFT+modulación, L07 Z); (c) se agregó
  columna "Archivo" a la tabla de Fase 3 con los nombres propuestos;
  (d) se actualizaron decisiones de scoping, mapa de transición desde
  los TP y tabla de seguimiento. **Al retomar el lab de complejos:**
  mover la ficha del Anexo A de vuelta a Fase 3 entre L00 y L01, y
  renumerar hacia arriba.

- **2026-08-02** — **Los TP salen del repo.** `TP0`, `TP1_variable_compleja`,
  `TP2_convolucion`, `TP3_analisis_de_fourier`, `TP4_FFT_y_sistemas_LTI` y
  `TP4_FFT_y_sistemas_LTI_viejo` (los 6 `.ipynb` y sus 6 fuentes `.md`) se
  movieron a `_legacy/` y `_legacy/src/`, con `_legacy/` en un `.gitignore`
  nuevo. Quedan disponibles localmente como insumo para escribir L02, L03 y
  L06, pero ya no se publican. No rompió links: README/index no los
  referenciaban desde el overhaul de Fase 4.

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
