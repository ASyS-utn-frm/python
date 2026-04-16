# Guía de estilo — Notebooks de ASyS

Lineamientos para mantener un tono, formato y estructura consistentes
en todos los notebooks del curso.

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
  desde cero en el tutorial correspondiente
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

## 2. Estructura de un tutorial

Cada tutorial sigue esta estructura general:

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
2. Objetivos del TP
3. Imports y configuración inicial
4. Bloques de ejercicios (orden ascendente de dificultad):
   a. Explicación del contexto / teoría necesaria
   b. Ejemplo resuelto (código provisto que el alumno ejecuta)
   c. Enunciado del ejercicio (celda enu-)
   d. Celda de actividad (celda act-)
   e. [Opcional] Verificación automática
5. [Opcional] Ejercicio integrador final
```

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

> **Recordá:** Este concepto lo vimos en el Tutorial 3, sección 2.1.
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
- En tutoriales iniciales, ser más generoso con los comentarios

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
- En tutoriales tempranos (antes de presentar f-strings), usar la forma simple:
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

## 7. Regla de oro: no usar lo que no se presentó

Antes de usar un concepto, función o construcción sintáctica en un notebook,
verificar que se haya presentado en un tutorial anterior o en el mismo notebook.

### Orden de dependencias de los tutoriales

```
T01 (Colab) → T02 (Tipos) → T03 (Colecciones) → T04 (Control)
                                                       ↓
T09 (SymPy) ← T08 (Matplotlib) ← T07 (NumPy) ← T05 (Funciones)
                                                       ↓
                                                  T06 (OOP)
```

Si un tutorial necesita algo de un tutorial posterior, hay dos opciones:
1. **Mover** el concepto al tutorial donde se necesita
2. **Dar una explicación mínima** inline con referencia al tutorial completo:
   > Usamos `range()` para generar una secuencia de números. Veremos más
   > detalles en el Tutorial 4, por ahora alcanza con saber que
   > `range(5)` genera los números del 0 al 4.

---

## 8. Checklist de revisión

Antes de dar por terminado un notebook, verificar:

- [ ] Todas las celdas tienen ID y rol asignado
- [ ] No se usan conceptos no presentados previamente
- [ ] El tono es consistente (tuteo con vos, cercano pero preciso)
- [ ] Las ecuaciones LaTeX renderizan correctamente
- [ ] Los gráficos tienen ejes etiquetados, título y grid
- [ ] Los imports están al inicio
- [ ] Las celdas de actividad tienen `# TU CÓDIGO AQUÍ`
- [ ] Los enunciados son claros y autocontenidos
- [ ] La dificultad es ascendente dentro del notebook
- [ ] No hay outputs guardados (notebooks limpios)
