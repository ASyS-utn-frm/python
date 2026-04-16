---
prefix: M01_introduccion_colab
source: M01_introduccion_colab.ipynb
---

%% md hdr-01
@header

%% md prov-01
# Módulo 1 — Introducción a Google Colab

Este es el primer módulo del **curso de introducción a Python para análisis de señales y sistemas**. Acá vas a conocer el entorno donde se va a trabajar en todo el curso: **Jupyter Notebooks** corriendo en **Google Colab**. Todavía no vas a escribir código de Python — eso empieza en el Módulo 2. Por ahora el objetivo es que aprendas a moverte cómodamente por el entorno: ejecutar celdas, escribir texto formateado y entender cómo se organiza un notebook.

%% md prov-02
## 1. ¿Qué es un Jupyter Notebook?

Un **Jupyter Notebook** es un documento interactivo que combina, en una misma página, bloques de texto explicativo y bloques de código que se pueden ejecutar. Cada bloque se llama **celda** (*cell*). Hay dos tipos principales:

- **Celdas de código:** donde se escribe y ejecuta código Python.
- **Celdas de texto:** donde se escriben explicaciones usando un lenguaje de marcado llamado Markdown.

Este formato es muy usado en ciencia, ingeniería y educación porque permite mezclar teoría, código y resultados (gráficos, tablas, ecuaciones) en un único documento.

> **Dato:** el nombre *Jupyter* viene de los tres lenguajes que soportaba originalmente: **Ju**lia, **Py**thon y **R**.

%% md prov-03
## 2. ¿Qué es Google Colab?

**Google Colab** (abreviación de *Colaboratory*) es un servicio gratuito de Google que permite ejecutar Jupyter Notebooks **en la nube**, sin instalar nada en tu computadora. Solo necesitás una cuenta de Google y acceso a internet.

Ventajas principales:

- No hace falta instalar Python ni ninguna librería.
- Los notebooks se guardan automáticamente en tu Google Drive.
- Se pueden compartir con otras personas fácilmente (igual que un documento de Google Docs).
- Tenés acceso gratuito a hardware potente (GPU/TPU), útil para cálculos intensivos.

En este curso vamos a usar Colab para todos los módulos y laboratorios.

> **Nota:** si algún día querés trabajar sin internet, podés instalar Python y Jupyter localmente (por ejemplo con la distribución [Anaconda](https://www.anaconda.com/)). Pero eso queda fuera del alcance de este curso.

%% md prov-04
### Recursos adicionales

Si tenés curiosidad y querés conocer más sobre Colab:

- [¿Qué es Colaboratory? (notebook oficial de Google)](https://colab.research.google.com/notebooks/intro.ipynb)

%% md prov-05
## 3. El entorno de ejecución

Para que las celdas de código puedan ejecutarse, el notebook necesita estar conectado a un **entorno de ejecución** (*runtime*). Un entorno es el conjunto de recursos donde se corre tu código: hardware (CPU, memoria), sistema operativo y el intérprete de Python con sus librerías.

En Colab, el entorno vive en un servidor de Google: es una **máquina virtual** con Ubuntu + Python + un montón de librerías ya instaladas (NumPy, Matplotlib, etc.).

**Para conectarte:** hacé clic en el botón **Conectar** que aparece arriba a la derecha. Después de unos segundos, Colab te asigna una máquina virtual y ya podés ejecutar celdas.

![Botón conectar en Colab](https://www.adictosaltrabajo.com/wp-content/uploads/2019/05/connect-colab.png)

> **Dato práctico:** una sesión dura como máximo 12 horas, y si dejás el notebook inactivo más de 90 minutos, el entorno se desconecta solo.

%% md prov-06
## 4. Celdas

Un notebook se organiza como una secuencia de celdas, una abajo de la otra. Podés crear, borrar, mover o editar cada una de forma independiente.

**Crear una celda nueva:** pasá el mouse sobre el borde inferior de una celda existente y aparecen dos botones:

- **+ Código** → crea una celda de código.
- **+ Texto** → crea una celda de texto.

También podés insertarlas desde el menú **Insertar** en la barra superior.

%% md prov-07
### 4.1. Celdas de código

Una celda de código es donde se escribe Python. Para ejecutarla hay tres formas equivalentes:

| Acción | Qué hace |
|--------|----------|
| Clic en el botón ▶ a la izquierda | Ejecuta la celda |
| `Ctrl + Enter` | Ejecuta la celda y deja el foco ahí |
| `Shift + Enter` | Ejecuta la celda y pasa a la siguiente |

El resultado (si hay) aparece debajo de la celda.

A continuación tenés un ejemplo de celda de código. Todavía no vimos nada de Python, así que por ahora limitate a **ejecutarla** y observar qué aparece debajo. La sintaxis la vas a entender a partir del Módulo 2.

%% code prov-08
print("Hola, mundo!")

%% md enu-01
### Actividad 1: crear tu primera celda

Agregá una **celda de código nueva** debajo de esta (usando el botón **+ Código**) y escribí dentro:

```python
print("Hola, soy <tu nombre>")
```

Reemplazá `<tu nombre>` por tu nombre real y ejecutá la celda. Debería aparecer un saludo personalizado debajo.

%% code act-01
# TU CÓDIGO AQUÍ

%% md prov-09
### 4.2. Celdas de texto (Markdown)

Las celdas de texto se escriben en **Markdown**, un lenguaje de marcado muy liviano y parecido al que usás sin darte cuenta en WhatsApp (por ejemplo `*texto*` para cursiva o `**texto**` para negrita).

Una celda de texto tiene dos modos:

- **Visualización:** mostrando el texto ya formateado (el modo por defecto).
- **Edición:** para modificar el contenido. Para entrar, **hacé doble clic** sobre la celda. Para salir y ver el resultado, apretá `Ctrl + Enter`.

La celda que estás leyendo ahora es una celda de texto. Probá: hacé doble clic sobre ella para ver cómo está escrita en Markdown, y después `Ctrl + Enter` para volver a verla formateada.

%% md prov-10
### 4.3. Sintaxis básica de Markdown

Estos son los elementos más frecuentes (hacé doble clic en esta celda para ver cómo se escriben):

# Título de nivel 1 (un `#`)
## Título de nivel 2 (dos `#`)
### Título de nivel 3 (tres `#`)

*cursiva* — con asteriscos simples

**negrita** — con asteriscos dobles

~~tachado~~ — con tildes dobles

Listas con viñetas:
- manzana
- pera
- uva

Listas numeradas:
1. primero
2. segundo
3. tercero

Un enlace: [Google](https://google.com)

> Una cita (se pone `>` al principio de la línea).

Referencia completa de Markdown: [daringfireball.net/projects/markdown/syntax](https://daringfireball.net/projects/markdown/syntax).

%% md prov-11
### 4.4. Fórmulas matemáticas (LaTeX)

Para escribir ecuaciones, Markdown soporta **LaTeX** (un lenguaje que vas a ver más adelante en la carrera). No es necesario que lo aprendas ahora, pero conviene que reconozcas la sintaxis cuando la veas.

- Inline (en medio de un párrafo): `$y = x^2$` se ve como $y = x^2$.
- En una línea aparte: `$$e^{j\pi} + 1 = 0$$` se ve como $$e^{j\pi} + 1 = 0$$

Ejemplos de fórmulas más complejas (hacé doble clic para ver el código):

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

%% md enu-02
### Actividad 2: escribir en Markdown

Hacé **doble clic** en la celda de abajo y reemplazá su contenido para escribir un mini CV tuyo en Markdown que incluya:

1. Un **título** con tu nombre (usá `#`).
2. Una **lista con viñetas** con al menos tres de tus materias favoritas.
3. Alguna palabra en **negrita**.

Cuando termines, apretá `Ctrl + Enter` para ver el resultado formateado.

%% md act-02
# Mi nombre

Acá va una breve presentación. Por ejemplo, una palabra en **negrita**.

Mis materias favoritas:
- (materia 1)
- (materia 2)
- (materia 3)

%% md prov-12
## 5. El kernel: por qué el orden importa

Todas las celdas de un mismo notebook comparten un **kernel**: un proceso de Python que mantiene en memoria todo lo que vas ejecutando (variables, funciones, resultados). Podés pensar al kernel como el "cerebro" del notebook — recuerda todo lo que hiciste durante la sesión.

Esto tiene una consecuencia importante: **el orden en que ejecutás las celdas importa, no el orden en que aparecen**. Si una celda usa algo que se definió en otra, esa otra tiene que haberse ejecutado antes.

Cada celda ejecutada muestra un número a su izquierda (`[1]`, `[2]`, `[3]`...) que indica el orden real de ejecución. Eso te ayuda a detectar si alguien (o vos) ejecutó las cosas en un orden raro.

A continuación, tres celdas: las dos primeras guardan valores en dos "cajitas" llamadas `a` y `b`, y la tercera las suma y muestra el resultado. No te preocupes por la sintaxis — la vas a ver en detalle en el Módulo 2. Por ahora alcanza con saber que `a = 2` guarda el número 2 en `a`, y que `print(...)` muestra cosas en pantalla.

%% code prov-13
a = 2

%% code prov-14
b = 3

%% code prov-15
print("El resultado de a + b es:", a + b)

%% md enu-03
### Actividad 3: probá el orden de ejecución

Hacé este pequeño experimento para ver el kernel en acción:

1. Ejecutá las tres celdas anteriores (`a = 2`, `b = 3`, `print(...)`) **en orden**. Fijate en el número que aparece a la izquierda de cada una: debería ser `[1]`, `[2]`, `[3]`.
2. Ahora volvé a la primera celda (`a = 2`), cambiá el `2` por un `10` y ejecutala de nuevo.
3. **Sin ejecutar de nuevo la celda del `print`**, observá que el resultado mostrado abajo todavía dice `5`. Eso es porque el kernel sigue recordando el último cálculo.
4. Ejecutá la celda del `print` de nuevo. Ahora sí debería decir `13`.

No hace falta escribir código en la celda de abajo — esta actividad es solo para observar.

%% code act-03
# Esta celda queda vacía a propósito — la actividad es de observación.

%% md prov-16
### Reiniciar el entorno

A veces, después de probar muchas cosas, conviene "empezar de cero" para asegurarse de que todo funciona desde el inicio sin depender de ejecuciones viejas. Desde el menú **Entorno de ejecución** podés elegir:

- **Reiniciar sesión:** borra toda la memoria (variables, funciones) pero mantiene la conexión con la máquina virtual.
- **Reiniciar y ejecutar todo:** reinicia y vuelve a correr todas las celdas desde arriba hacia abajo.

Es una buena costumbre, antes de entregar un trabajo, hacer "Reiniciar y ejecutar todo" para confirmar que el notebook corre limpio de principio a fin.

%% md prov-17
## 6. Comentarios en el código

Los **comentarios** son notas que escribís dentro del código pero que Python ignora al ejecutarlo. Sirven para explicar qué hace cada parte. En Python, todo lo que va después del símbolo `#` en una línea es un comentario.

%% code prov-18
# Esto es un comentario: Python lo ignora.
print("Hola")  # También pueden ir al final de una línea con código.

%% md prov-19
Si querés escribir un comentario de varias líneas, simplemente poné un `#` al principio de cada línea:

%% code prov-20
# Este es un comentario
# que ocupa varias líneas.
# Cada línea empieza con #.

%% md prov-21
## 7. Comandos del sistema operativo

Como Colab corre sobre una máquina virtual con Linux (Ubuntu), desde una celda de código podés ejecutar comandos del sistema operativo escribiendo `!` al principio. El uso más común es instalar librerías que no vienen preinstaladas:

%% code prov-22
!pip install nombre_de_la_libreria

%% md prov-23
No vamos a necesitar esto en los primeros módulos, porque Colab ya trae instaladas todas las librerías que usamos en el curso (NumPy, Matplotlib, SymPy, SciPy). Lo dejamos acá para que lo conozcas.

%% md prov-24
## 8. Panel lateral

A la izquierda de la pantalla hay un panel con varios íconos. Por ahora solo nos interesa uno:

- **`{x}` Variables:** muestra todas las variables que tenés en memoria con sus valores actuales. Es muy útil para inspeccionar qué pasó tras ejecutar algo y para depurar errores.

Los otros íconos (archivos, búsqueda, tabla de contenidos) los vas a ir descubriendo con el uso.

%% md prov-25
## Cierre

Con esto tenés lo mínimo necesario para moverte en Colab durante el resto del curso:

- Sabés qué es un notebook y cómo se organiza en celdas.
- Podés crear, editar y ejecutar celdas de código y de texto.
- Entendés que el orden de ejecución importa, gracias al kernel compartido.
- Sabés formatear texto con Markdown y escribir fórmulas con LaTeX.
- Conocés comentarios (`#`) y comandos del sistema (`!`).

**En el próximo módulo** vas a empezar con Python propiamente dicho: tipos de datos, variables, operaciones y la función `print()` vista en detalle.
