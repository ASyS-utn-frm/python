---
prefix: M08_matplotlib
source: M08_matplotlib.ipynb
---

%% md hdr-01
<center>


<div style="display: flex; justify-content: center;">
    <img src="data:image/jpeg;base64,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" alt="Logo UTN"/>
</div>
</center>
<center>
    <div style="font-family: 'Georgia', serif; font-size: 24px;">
        <p><strong>Análisis de Señales y Sistemas</strong></p>
        <p><strong>Ingeniería en Electrónica</strong></p>
        <p><strong>Ingeniería en Telecomunicaciones</strong></p>
    </div>
</center>

%% md prov-01
# Módulo 8 — Matplotlib

En el Módulo 7 aprendiste a **generar** arrays: un eje de tiempo con `linspace`, una senoidal con `np.sin`, miles de muestras en dos líneas. Pero mirarlas con `print` no ayuda mucho: un gráfico de una señal te dice en un vistazo lo que una columna de 200 números te oculta.

De eso se encarga **Matplotlib**: la librería estándar de Python para dibujar gráficos. Se integra de manera natural con NumPy — cualquier array se puede graficar tal cual, sin conversiones — y su API es deliberadamente parecida a la de MATLAB, lo que la vuelve familiar apenas la ves.

Los temas de este módulo son:

| Tema | Para qué sirve |
|------|----------------|
| `import matplotlib.pyplot as plt` | Cargar la librería con su alias convencional |
| `plt.plot(x, y)` | Graficar una curva uniendo puntos |
| `title`, `xlabel`, `ylabel`, `grid` | Que el gráfico cuente su historia solo |
| Varias curvas y leyendas | `label=` + `plt.legend()` |
| `plt.figure(figsize=...)` | Controlar el tamaño de la figura |
| `plt.subplots(filas, columnas)` | Varios paneles en una misma figura |
| `plt.stem(n, x)` | Señales discretas (un palito por muestra) |
| `plt.scatter(x, y)` | Puntos sueltos en el plano |

> **Conexión con el Módulo 7.** Todo lo que grafiques va a salir de un array de NumPy. Si te perdés en algún paso, es casi seguro un tema de cómo se generó el array, no del gráfico.

%% md prov-02
## 1. Cargar la librería

La convención es cargar el submódulo `pyplot` con el alias `plt`. `pyplot` es la parte de Matplotlib con la que vamos a trabajar todo este módulo: expone funciones simples (`plot`, `title`, `show`...) que se encadenan para construir un gráfico.

También cargamos NumPy porque prácticamente cualquier gráfico que hagamos parte de un array.

%% code prov-03
import matplotlib.pyplot as plt
import numpy as np

%% md prov-04
De ahora en adelante, cada vez que escribamos `plt.algo` le estamos pidiendo a Matplotlib una de sus funciones. El alias `plt`, como el `np` de NumPy, es universal: lo vas a ver en casi todo código Python que trabaje con gráficos.

> **Ejecutá esta celda una sola vez** al abrir el notebook. De ahí en adelante, `plt` y `np` quedan disponibles hasta que reinicies el entorno.

%% md prov-05
## 2. El primer gráfico

La función base es `plt.plot(x, y)`: toma dos arrays del mismo largo y une los puntos $(x_0, y_0), (x_1, y_1), \ldots$ con segmentos de recta.

Empecemos con una parábola:

%% code prov-06
x = np.linspace(-3, 3, 100)
y = x ** 2

plt.plot(x, y)
plt.show()

%% md prov-07
Tres cosas para notar:

- `x` tiene 100 puntos equiespaciados entre $-3$ y $3$; `y` tiene los cuadrados correspondientes. Son dos arrays del mismo largo.
- `plt.plot(x, y)` hace todo el trabajo: lee los dos arrays y dibuja la curva.
- `plt.show()` le indica a Matplotlib "mostrá ya". En Colab y otros notebooks el gráfico se muestra solo al final de la celda, así que `plt.show()` no siempre es necesario, pero incluirlo es una buena costumbre: deja explícito en qué momento termina el gráfico.

Lo que ves parece una curva suave, pero en realidad son 100 segmentos de recta muy cortos que, al tener los puntos cerca, dan la ilusión de continuidad. Si bajás el número de puntos de `linspace`, la "curva" se vuelve poligonal.

%% md prov-08
## 3. Títulos, etiquetas y grilla

Un gráfico sin títulos ni etiquetas obliga a quien lo lee a adivinar qué estamos mostrando. Cuatro funciones arreglan eso:

- `plt.title("...")` — título del gráfico.
- `plt.xlabel("...")` — etiqueta del eje horizontal.
- `plt.ylabel("...")` — etiqueta del eje vertical.
- `plt.grid(True)` — dibuja una grilla para leer valores con más precisión.

%% code prov-09
x = np.linspace(-3, 3, 100)
y = x ** 2

plt.plot(x, y)
plt.title("Parábola")
plt.xlabel("x")
plt.ylabel("y = x²")
plt.grid(True)
plt.show()

%% md prov-10
Estas cuatro llamadas van **antes** de `plt.show()` y operan sobre el último gráfico abierto. El orden entre ellas no importa.

Para el resto del curso vamos a asumir que todo gráfico tiene, como mínimo, título, etiquetas en ambos ejes y grilla. Es una cuestión de higiene: un gráfico sin contexto no sirve.

%% md prov-11
## 4. Graficar una señal muestreada

La receta más frecuente en este curso es:

1. Armar el eje de tiempos con `linspace`.
2. Calcular la señal como función de ese eje.
3. Graficar con `plot`.

Retomemos la senoidal del Módulo 7:

%% code prov-12
# Parámetros
A = 2          # amplitud en volts
f = 100        # frecuencia en Hz
duracion = 0.02   # 20 ms

# Eje de tiempos y señal
t = np.linspace(0, duracion, 200)
x = A * np.sin(2 * np.pi * f * t)

# Gráfico
plt.plot(t, x)
plt.title("Señal senoidal de 100 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Tensión [V]")
plt.grid(True)
plt.show()

%% md prov-13
Un detalle importante, que ya veníamos comentando: aunque la curva se ve "continua", en realidad son 200 puntos discretos conectados por segmentos. Matplotlib no sabe nada de la señal original; sólo conecta las muestras que le diste. Si el muestreo es lo suficientemente denso, el resultado parece continuo. Si es pobre, los segmentos se ven a ojo. En el lab de muestreo vamos a revisitar con más profundidad este tema.

%% md enu-01
### Actividad 1: graficar una senoidal

Partiendo de la receta anterior, graficá la señal

$$x(t) = 3 \cdot \sin(2\pi \cdot 50 \cdot t)$$

durante 40 ms, con 400 puntos.

1. Armá el eje de tiempos con `linspace`.
2. Calculá `x` aplicando la fórmula.
3. Graficá con título `"Senoidal de 50 Hz"`, ejes etiquetados en segundos y volts, y grilla.

%% code act-01
import numpy as np
import matplotlib.pyplot as plt

# TU CÓDIGO AQUÍ

%% md prov-14
## 5. Varias señales en un mismo gráfico

Llamadas consecutivas a `plt.plot` **comparten el mismo eje**: todo se dibuja encima, cada curva con un color distinto automáticamente asignado.

Para distinguirlas hace falta una *leyenda*. Se arma en dos pasos:

1. Pasarle a cada `plt.plot` un argumento `label="..."` con el nombre de esa curva.
2. Llamar a `plt.legend()` antes de `plt.show()`.

%% code prov-15
t = np.linspace(0, 0.03, 600)
x1 = np.sin(2 * np.pi * 100 * t)
x2 = np.sin(2 * np.pi * 250 * t)

plt.plot(t, x1, label="100 Hz")
plt.plot(t, x2, label="250 Hz")
plt.title("Dos senoidales superpuestas")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

%% md prov-16
Si querés forzar un color concreto, `plt.plot` acepta un argumento `color`:

```python
plt.plot(t, x1, color="red", label="100 Hz")
```

Y también acepta un "código corto" estilo MATLAB combinando color y estilo de línea, por ejemplo `"r--"` (rojo, línea entrecortada) o `"g-."` (verde, punto y raya). Son útiles para apurar un gráfico; para trabajos más prolijos conviene pasar los argumentos por nombre.

%% md enu-02
### Actividad 2: señal original y su versión amplificada

Simulemos la entrada y la salida de un amplificador de ganancia $G = 3$.

1. Generá `t` con 600 puntos entre 0 y 20 ms.
2. Generá `entrada = np.sin(2 * np.pi * 200 * t)` (señal a 200 Hz, amplitud 1).
3. Generá `salida = 3 * entrada`.
4. Graficá las dos señales en un mismo gráfico, con leyendas `"Entrada"` y `"Salida (G = 3)"`, ejes etiquetados y grilla.

%% code act-02
import numpy as np
import matplotlib.pyplot as plt

# TU CÓDIGO AQUÍ

%% md prov-17
## 6. Controlar el tamaño de la figura

Por defecto los gráficos salen cuadrados y más bien chicos. Para señales temporales suele servir algo ancho y bajo, que deje ver varios ciclos sin apretarse.

Se controla con `plt.figure(figsize=(ancho, alto))`, **antes** del primer `plt.plot`. Las medidas están en pulgadas.

%% code prov-18
t = np.linspace(0, 0.05, 500)
x = np.sin(2 * np.pi * 100 * t)

plt.figure(figsize=(10, 3))
plt.plot(t, x)
plt.title("Senoidal con figura ancha")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

%% md prov-19
## 7. Varios paneles: `plt.subplots`

A veces queremos dos gráficos **distintos** en la misma figura (por ejemplo, la señal arriba y algo derivado de ella abajo). Para eso se usa `plt.subplots(filas, columnas)`, que devuelve dos cosas:

- una **figura** (el lienzo completo),
- un **array de ejes** (`axs`), uno por panel.

Sobre cada `axs[i]` llamamos sus propios métodos, que tienen nombres ligeramente distintos a los que venimos usando: `ax.plot`, `ax.set_title`, `ax.set_xlabel`, `ax.set_ylabel`, `ax.grid`. Los prefijos `set_` son una particularidad de esta API orientada a objetos.

%% code prov-20
t = np.linspace(0, 0.04, 400)
seno = np.sin(2 * np.pi * 50 * t)
coseno = np.cos(2 * np.pi * 50 * t)

fig, axs = plt.subplots(2, 1, figsize=(9, 5))

axs[0].plot(t, seno)
axs[0].set_title("Seno")
axs[0].set_ylabel("Amplitud")
axs[0].grid(True)

axs[1].plot(t, coseno)
axs[1].set_title("Coseno")
axs[1].set_xlabel("Tiempo [s]")
axs[1].set_ylabel("Amplitud")
axs[1].grid(True)

plt.tight_layout()
plt.show()

%% md prov-21
Tres detalles:

- `plt.subplots(2, 1, ...)` arma **2 filas y 1 columna**. Si pusiéramos `(1, 2)` quedarían lado a lado.
- Notá que solo le puse `xlabel` al panel de abajo: los dos paneles comparten el eje x (tiempo), así que alcanza con etiquetarlo una vez.
- `plt.tight_layout()` al final ajusta los márgenes para que los títulos no se superpongan entre paneles. Es casi gratis incluirlo siempre que uses subplots.

%% md enu-03
### Actividad 3: tensión y potencia instantánea

Una resistencia de $R = 1\ \Omega$ recibe una señal senoidal. Queremos ver en paneles separados la tensión $v(t)$ y la potencia instantánea $p(t) = v^2(t) / R$.

1. Generá `t` con 400 puntos entre 0 y 40 ms.
2. Generá `v = 2 * np.sin(2 * np.pi * 50 * t)`.
3. Calculá `p = v ** 2` (con $R = 1$, queda así de simple).
4. Armá una figura con dos paneles, uno arriba del otro, con `figsize=(9, 5)`. En el panel de arriba graficá `v`; en el de abajo, `p`. Etiquetá ejes y títulos con unidades apropiadas (V para tensión, V² para potencia con $R=1$).

Al mirar el gráfico, fijate en dos cosas: la potencia es **siempre positiva** (es un cuadrado), y oscila al **doble de frecuencia** que la tensión.

%% code act-03
import numpy as np
import matplotlib.pyplot as plt

# TU CÓDIGO AQUÍ

%% md prov-22
## 8. Señales discretas: `plt.stem`

Hasta acá graficamos conectando puntos con líneas, lo que es natural cuando la señal de fondo es continua y lo que tenemos son muestras densas. Para una señal **inherentemente discreta** (definida solo en índices enteros $n = 0, 1, 2, \ldots$), unirlos con líneas engaña: sugiere que hay algo entre muestra y muestra cuando no hay nada.

Para estos casos está `plt.stem(n, x)`: dibuja un palito vertical en cada muestra, rematado con un punto. Así queda visualmente claro que la señal vive solo en esos índices.

%% code prov-23
n = np.arange(0, 10)
x_n = np.sin(2 * np.pi * n / 10)

plt.stem(n, x_n)
plt.title("Señal discreta: sin(2πn/10)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()

%% md prov-24
Resumen rápido:

- Señales continuas muestreadas con muestreo denso → `plt.plot`.
- Señales discretas (o cuando querés resaltar que son muestras individuales) → `plt.stem`.

La elección **comunica** qué tipo de señal estás mostrando, y se convierte en una convención que vas a usar durante toda la cursada.

%% md enu-04
### Actividad 4: descarga muestreada de un capacitor

Un capacitor se descarga a través de una resistencia. Tomamos muestras a intervalos regulares y obtenemos la secuencia

$$v[n] = V_0 \cdot e^{-n/\tau_n}$$

con $V_0 = 10$ V y $\tau_n = 4$ (constante de tiempo expresada en cantidad de muestras).

1. Generá `n = np.arange(0, 20)`.
2. Calculá `v_n = 10 * np.exp(-n / 4)` aprovechando que `np.exp` opera sobre el array entero.
3. Graficalo con `plt.stem`, título `"Descarga muestreada"`, `xlabel = "n"`, `ylabel = "v[n] [V]"`, grilla.

%% code act-04
import numpy as np
import matplotlib.pyplot as plt

# TU CÓDIGO AQUÍ

%% md prov-25
## 9. Puntos en el plano: `plt.scatter`

`plot` y `stem` asumen que hay una secuencia ordenada: a cada valor del eje x le corresponde uno del eje y. A veces lo que querés es graficar **puntos sueltos** en el plano, sin conectarlos ni representar una variable temporal. Para eso sirve `plt.scatter(x, y)`.

Un caso natural: un número complejo $z = a + jb$ se puede ver como un punto $(a, b)$ en el plano. Recordá del Módulo 2 que los complejos tienen los atributos `.real` y `.imag`, que sobre arrays de NumPy devuelven arrays con las partes reales e imaginarias respectivamente.

%% code prov-26
z = np.array([1 + 2j, -2 + 1j, -1 - 1j, 2 - 2j])

plt.scatter(z.real, z.imag)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Cuatro números complejos en el plano")
plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
plt.grid(True)
plt.show()

%% md prov-27
Dos funciones nuevas aparecen aquí:

- `plt.axhline(0, ...)` dibuja una línea **h**orizontal a la altura $y = 0$.
- `plt.axvline(0, ...)` dibuja una línea **v**ertical en $x = 0$.

En el plano complejo son útiles para marcar bien los ejes real e imaginario. El argumento `color="black"` las pone en negro; `linewidth=0.5` las hace finitas para que no compitan con los datos.

%% md enu-05
### Actividad 5: impedancia en el plano complejo

Medimos la impedancia $Z$ de un componente a cuatro frecuencias distintas y obtenemos estos valores (en ohms):

```python
Z = np.array([5 + 1j, 5 + 3j, 5 + 6j, 5 + 10j])
```

1. Graficá los cuatro puntos con `plt.scatter(Z.real, Z.imag)`.
2. Agregá los ejes real e imaginario con `plt.axhline(0, ...)` y `plt.axvline(0, ...)`.
3. Etiquetá: título `"Impedancia medida"`, `xlabel = "Parte real [Ω]"`, `ylabel = "Parte imaginaria [Ω]"`, grilla.
4. Mirando el gráfico, ¿qué dirías que es constante y qué crece al subir la frecuencia? (No hace falta escribir la respuesta, pero pensala.)

%% code act-05
import numpy as np
import matplotlib.pyplot as plt

# TU CÓDIGO AQUÍ

%% md prov-28
## Cierre

Con lo que aprendiste en este módulo, ya podés convertir cualquier array en una imagen legible:

- `plt.plot(x, y)` para curvas continuas muestreadas densamente.
- `plt.stem(n, x)` para señales discretas.
- `plt.scatter(x, y)` para puntos sueltos (por ejemplo, complejos en el plano).
- `plt.title`, `plt.xlabel`, `plt.ylabel`, `plt.grid`, `plt.legend` para que el gráfico se explique solo.
- `plt.figure(figsize=...)` para elegir el tamaño.
- `plt.subplots(filas, columnas)` para varios paneles en una misma figura.

En los módulos y laboratorios siguientes van a aparecer variantes más específicas (escalas logarítmicas, anotaciones, estilos de línea, gráficos polares, *diagramas de Bode*), pero todas se construyen sobre esta base.

> **Para explorar más:** la galería oficial de Matplotlib está en [matplotlib.org/stable/gallery](https://matplotlib.org/stable/gallery/index.html). Miles de ejemplos, cada uno con su código completo; suele ser más rápido buscar ahí que intentar adivinar el argumento correcto de una función.
