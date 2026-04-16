# Convención de formato de celdas

Este documento define cómo se identifican y clasifican las celdas en los notebooks
del curso de Análisis de Señales y Sistemas.

---

## 1. Formato Markdown fuente

Los notebooks se editan como archivos `.md` en el directorio `src/`.
Cada celda se delimita con una línea que comienza con `%%`:

```
%% tipo id
contenido de la celda...
```

Donde:
- **tipo**: `md` (markdown) o `code` (código Python)
- **id**: identificador corto de la celda (ver sección 2)

### Ejemplo completo

```markdown
---
prefix: TP1_variable_compleja
source: TP1_variable_compleja.ipynb
---

%% md hdr-01
# Trabajo Práctico 1: Variable Compleja

%% md prov-01
## 1. Representación de números complejos
Un número complejo $z$ se puede expresar en forma cartesiana...

%% code prov-01
import numpy as np
z = 3 + 4j
print(f"|z| = {abs(z)}")

%% md enu-01
## Actividad 1
Dado $z_1 = 2 + 3j$ y $z_2 = 1 - j$, calculá:
1. La suma $z_1 + z_2$
2. El módulo de cada uno

%% code act-01
# TU CÓDIGO AQUÍ
```

---

## 2. Identificadores de celda

Cada celda tiene un ID con el formato `prefijo-NN` donde:

| Prefijo | Rol | Significado |
|---------|-----|-------------|
| `hdr` | `header` | Encabezado del notebook (logo, título) |
| `prov` | `provided` | Contenido provisto por el profesor (explicaciones, código ejemplo) |
| `enu` | `enunciado` | Enunciado de una actividad para el alumno |
| `act` | `student` | Celda donde el alumno escribe su respuesta |

El número `NN` es secuencial dentro de cada prefijo (01, 02, 03...).

### ID completo en el notebook generado

Al convertir a `.ipynb`, el ID de celda se construye como:

```
{prefix del notebook}-{id de celda}
```

Ejemplo: `TP1_variable_compleja-act-01`

Esto permite identificar unívocamente cualquier celda en cualquier notebook.

---

## 3. Roles y su uso

### `header` — Encabezado
- Logo de UTN y título del notebook
- Solo al inicio del notebook
- **El alumno NO modifica estas celdas**

### `provided` — Material provisto
- Explicaciones teóricas (markdown)
- Código de ejemplo que el alumno debe leer/ejecutar (code)
- **El alumno NO modifica estas celdas** (solo las ejecuta/lee)

### `enunciado` — Consigna
- Descripción de la actividad que el alumno debe realizar
- Siempre en markdown
- Precede inmediatamente a una o más celdas `act`
- **El alumno NO modifica estas celdas**

### `student` — Actividad del alumno
- Celda donde el alumno escribe su código o respuesta
- Comienza vacía o con un comentario guía: `# TU CÓDIGO AQUÍ`
- Puede tener un scaffold mínimo (variables pre-definidas, estructura de función)
- **Esta es la ÚNICA celda que el alumno modifica**

---

## 4. Convenciones de contenido en celdas `act`

Las celdas de actividad pueden estar:

### Vacías (ejercicio abierto)
```python
# TU CÓDIGO AQUÍ
```

### Con scaffold (ejercicio guiado)
```python
# Definí la función pedida
def calcular_modulo(z):
    # TU CÓDIGO AQUÍ
    pass

# Probá tu función (no modificar)
print(calcular_modulo(3 + 4j))  # Debería dar 5.0
```

### Con estructura parcial (ejercicio semi-guiado)
```python
z1 = 2 + 3j
z2 = 1 - 1j

# Calculá la suma y guardala en 'suma'
suma = # TU CÓDIGO AQUÍ

# Calculá el módulo de z1 y guardalo en 'mod_z1'
mod_z1 = # TU CÓDIGO AQUÍ

print(f"Suma: {suma}, |z1|: {mod_z1}")
```

---

## 5. Flujo de trabajo

```
                    Edición
  src/*.md  ──────────────────►  src/*.md (modificado)
     │                                │
     │  nb2md.py                      │  md2nb.py
     │  (extracción                   │  (generación)
     │   inicial)                     │
     ▼                                ▼
  *.ipynb ◄──── estado actual    *.ipynb (actualizado)
                                      │
                                      │  Alumno trabaja
                                      │  en Google Colab
                                      ▼
                                 *.ipynb (entregado)
                                      │
                                      │  extract_student.py
                                      ▼
                                 Celdas act + rúbrica
                                      │
                                      │  Corrección (IA)
                                      ▼
                                 Calificación
```

---

## 6. Metadata en el notebook generado

Cada celda en el `.ipynb` contiene metadata con el rol:

```json
{
  "cell_type": "code",
  "id": "TP1_variable_compleja-act-01",
  "metadata": {
    "role": "student"
  },
  "source": ["# TU CÓDIGO AQUÍ"],
  "execution_count": null,
  "outputs": []
}
```

Esto permite que `extract_student.py` identifique las celdas del alumno
sin depender de heurísticas de contenido.
