# Créditos y licencias de los archivos de audio

| Archivo | Usado en | Origen | Licencia |
|---|---|---|---|
| `impulsiva_galpon.wav` | Laboratorio 2 | freesound.org, sonido n° 180960 (`gunshot`), de kleeb | **No verificable** (ver nota) |
| `violin.wav` | Laboratorios 2 y 3 | freesound.org, sonido n° 92002 (`violin origional`), de jcveliz | CC Sampling Plus 1.0 (ver nota) |
| `nota_violin_A4.wav` | Laboratorios 4 y 5 | University of Iowa *Musical Instrument Samples*, `Violin.arco.ff.sulA.A4` | Uso libre sin restricciones |
| `nota_flauta_A4.wav` | Laboratorio 4 | University of Iowa *Musical Instrument Samples*, `Flute.nonvib.ff.A4` | Uso libre sin restricciones |
| `am_misteriosa.wav` | Laboratorio 4 | Generado para este curso a partir de `favorite_station.wav`, freesound.org n° 105977, de wcfl10 | CC0 1.0 (dominio público) |

Formato de los dos archivos anteriores tal como están en esta carpeta:

- `impulsiva_galpon.wav` — 44100 Hz, estéreo, 94398 muestras (2,14 s).
- `violin.wav` — 44100 Hz, mono, 220500 muestras (5,00 s).

## Detalle de los archivos del Laboratorio 4

### University of Iowa — Musical Instrument Samples

Grabaciones de Lawrence Fritts, Director de los Electronic Music Studios de la
University of Iowa. El sitio declara: *"Since 1997, these recordings have been
freely available on this website and may be downloaded and used for any
projects, without restrictions."*

Las notas se registraron en cámara anecoica. Para este repositorio se
convirtieron de AIFF estéreo a WAV mono de 16 bits a 44100 Hz, se recortó el
silencio de los extremos y se normalizó el pico a 0,95.

- `nota_violin_A4.wav` — 44100 Hz, mono, 95163 muestras (2,16 s).
- `nota_flauta_A4.wav` — 44100 Hz, mono, 89286 muestras (2,02 s).

Las dos son un La4 y su fundamental medida es de 443 Hz, doce *cents* por encima
del La de concierto de 440 Hz. No es un error: refleja la afinación con la que se
grabaron.

### `am_misteriosa.wav`

Generado para el proyecto final del Laboratorio 4. El mensaje es
`favorite_station.wav` (freesound.org n° 105977, de wcfl10, voz de un locutor de
radio), publicado bajo **CC0 1.0**, es decir dominio público, sin obligación de
atribución. Se lo limitó a la banda telefónica de 3400 Hz, se lo moduló en
amplitud con portadora —índice de modulación 0,8, portadora de 13750 Hz— y se le
sumó ruido gaussiano de desviación estándar 0,03.

- 48000 Hz, mono, 144000 muestras (3,000 s exactos).

La duración es exacta a propósito: con 3 segundos justos la resolución del
análisis es de 1/3 Hz y la portadora de 13750 Hz cae exactamente sobre una línea
de la FFT, de modo que el alumno la localiza sin error residual y la demodulación
coherente funciona. **Si se regenera el archivo, mantener esa condición.**

## Nota sobre los dos audios anteriores

Revisado el **2026-08-03**, al preparar el Laboratorio 4:

- **`impulsiva_galpon.wav`**: el sonido n° 180960 **fue borrado de Freesound**,
  así que su licencia ya no puede verificarse. Queda pendiente reemplazarlo.
  Candidato acordado: freesound.org n° 718451, de peter1955
  (*IR — Wave pipe 3 — Science Museum London UK*), **CC BY-NC 4.0**, 48000 Hz,
  mono, 2,28 s.
- **`violin.wav`**: su licencia es **CC Sampling Plus 1.0**, que Creative Commons
  retiró. Permite redistribuir copias literales solo con fines no comerciales, y
  exige atribución. Es defendible para material educativo gratuito, pero conviene
  reemplazarlo por una fuente de licencia vigente.

El Laboratorio 4 **no depende de ninguno de los dos**: usa exclusivamente los
tres archivos nuevos, cuyas licencias están verificadas. El detalle del pendiente
está en `docs/CARRYOVERS.md`.
