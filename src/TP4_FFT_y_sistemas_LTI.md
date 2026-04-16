---
prefix: TP4_FFT_y_sistemas_LTI
source: TP4_FFT_y_sistemas_LTI.ipynb
---

%% md hdr-01
<center>


<div style="display: flex; justify-content: center;">
    <img src="data:image/jpeg;base64,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" alt="Logo UTN"/>
</div>
</center>
<center>
    <div style="font-family: 'Georgia', serif; font-size: 24px;">
        <p><strong>Ingeniería en Electrónica. Análisis de Señales y Sistemas</strong></p>
    </div>
</center>

%% md prov-01
# Trabajo Práctico $N^{\circ}4$. 

%% md prov-02
## Primera parte: Análisis de Fourier en tiempo discreto 

%% md prov-03
En el ámbito del procesamiento de señales discretas, existen varias razones que justifican la utilización de la Transformada de Fourier en Tiempo Discreto (DTFT) y sus versiones computacionales más utilizadas: la Transformada de Fourier Discreta (DFT) y la Transformada Rápida de Fourier (FFT).

La idea central del **Análisis de Fourier** es una herramienta matemática increíblemente poderosa que nos permite "descomponer" una señal compleja (como una onda de audio, una vibración o incluso una imagen) en la suma de sus partes fundamentales: un conjunto de ondas senoidales simples, cada una con una frecuencia, amplitud y fase específicas.

Al hacer esto, pasamos de ver la señal en el **"dominio del tiempo"** (cómo cambia su amplitud a medida que pasa el tiempo) al **"dominio de la frecuencia"** (cuánta energía o "presencia" tiene la señal en cada frecuencia).

Algunas de las principales aplicaciones incluyen:

- **Análisis de Audio**: Permite analizar el "contenido frecuencial" o "espectro" de un sonido. Esto es la base de los ecualizadores (que suben o bajan el volumen de rangos de frecuencia, como los "bajos", "medios" y "altos"), la eliminación de ruido (identificando la frecuencia del ruido y filtrándola) y la compresión de datos (como en el formato MP3, que elimina frecuencias que el oído humano apenas percibe).

- **Procesamiento de Imágenes**: En una imagen, la "frecuencia" no es temporal, sino **espacial**.
    - **Bajas frecuencias espaciales** corresponden a cambios suaves y lentos de color o brillo (como un cielo despejado o una pared lisa).
    - **Altas frecuencias espaciales** corresponden a cambios rápidos y abruptos (como los bordes de un objeto, la textura de una tela o el "grano" en una foto).
    Al aplicar la FFT 2D, podemos diseñar filtros para, por ejemplo, suavizar una imagen (eliminar altas frecuencias) o detectar bordes (realzar altas frecuencias).

- **Telecomunicaciones**: El análisis en frecuencia es clave para la **multiplexación por división de frecuencia (FDM)**. Esto permite que múltiples señales (como diferentes estaciones de radio o canales de TV) viajen por el mismo medio (el aire) al mismo tiempo sin interferirse, simplemente asignando a cada una un "carril" de frecuencia diferente.

- **Diagnóstico de Sistemas**: En el análisis de vibraciones, cada componente de una máquina (un motor, un rodamiento) vibra a una frecuencia característica cuando funciona correctamente. Si una pieza empieza a fallar, generará vibraciones a nuevas frecuencias. Usando la FFT, un técnico puede ver el espectro de vibración y diagnosticar fallos antes de que ocurran fallas catastróficas.

### Diferencias entre DTFT, DFT y FFT

Este es un punto clave. La diferencia fundamental radica en si tratamos con señales teóricas (infinitas) o señales reales (finitas) que una computadora puede procesar.

- **Transformada de Fourier en Tiempo Discreto (DTFT)**:
    - **Entrada:** Una señal discreta en el tiempo (es decir, muestreada) que se asume de duración **infinita**.
    - **Salida:** Un espectro de frecuencia que es **continuo** (no está muestreado).
    - **Uso:** Es una herramienta puramente **teórica** y analítica. No podemos calcularla en una computadora porque requeriría infinitas muestras de entrada y produciría un espectro *continuo* (que tendría infinitos puntos de frecuencia para almacenar).

- **Transformada de Fourier Discreta (DFT)**:
    - **Entrada:** Una señal discreta en el tiempo y de duración **finita** (un número $N$ de muestras).
    - **Salida:** Un espectro de frecuencia que también es **discreto** (compuesto exactamente por $N$ puntos o "bins" de frecuencia).
    - **Uso:** Esta es la versión **computable** de la DTFT. Es lo que realmente usamos en las computadoras y en Python. La DFT toma un "trozo" finito de nuestra señal y calcula su espectro en un número finito de puntos de frecuencia.

- **Transformada Rápida de Fourier (FFT)**:
    - **No es una transformada nueva.** Es simplemente un conjunto de **algoritmos** (como el famoso algoritmo de Cooley-Tukey) extremadamente eficientes diseñados para calcular la DFT.
    - Su descubrimiento revolucionó el procesamiento digital de señales, haciéndolo lo suficientemente rápido para aplicaciones en tiempo real.

**Nota sobre Complejidad Computacional**: La complejidad computacional se refiere al tiempo que un algoritmo tarda en ejecutarse, en función de la cantidad de datos ($N$) que procesa.
-   Calcular la DFT directamente tiene una complejidad de $O(N^2)$ (Orden N-cuadrado).
-   Calcular la DFT usando el algoritmo FFT tiene una complejidad de $O(N \log N)$.

Esta diferencia es drástica. Para señales con muchas muestras ($N$ muy grande), la FFT es cientos de veces más rápida que la DFT directa.

%% md prov-04
### Objetivos del Trabajo Práctico
El objetivo de este trabajo práctico es proporcionar una comprensión profunda del análisis de Fourier en tiempo discreto y cómo aplicarlo de manera efectiva utilizando herramientas computacionales como Python. Exploraremos cómo realizar la Transformada de Fourier Discreta de señales, interpretar el espectro de frecuencia, y aplicar filtros en el dominio de la frecuencia para manipular las señales. Además, se busca que los estudiantes desarrollen la capacidad de interpretar y analizar espectros de frecuencia en aplicaciones prácticas.

%% md prov-05
## Uso de la función `fft` de Scipy

Para calcular la Transformada Rápida de Fourier (FFT), utilizaremos la función `fft` del módulo `scipy.fft`.

### Uso Básico de `fft`

El uso básico de `fft` es directo y permite transformar una señal en el dominio del tiempo al dominio de la frecuencia:

%% code prov-06
from scipy.fft import fft

# Definimos una señal de ejemplo
data = [0.0, 1.0, 0.0, -1.0]

# Calculamos la FFT de la señal
data_fft = fft(data)
data_fft


%% md prov-07
En este ejemplo, `data` contiene valores de una señal discreta en el tiempo, y `fft(data)` devuelve su representación en el dominio de la frecuencia como `data_fft`, con coeficientes complejos que corresponden a las diferentes componentes de frecuencia.

%% md prov-08
### Ejemplo Completo con `fft` y `fftfreq`

Vamos a realizar un ejemplo completo paso a paso. Para visualizar los resultados de la `fft`, no solo necesitamos el vector de amplitudes (`x_fft`), sino también el vector de frecuencias (`frecuencias`) al que corresponde cada amplitud.

Para esto, usaremos la función `fftfreq` de `scipy`.

La función `fftfreq` toma dos parámetros principales:
- **N**: La cantidad de muestras de la señal (el número de puntos en el dominio temporal).
- **T**: El intervalo de tiempo entre cada muestra (el **período de muestreo**, $ T = \frac{1}{f_s}$, donde $f_s$ es la frecuencia de muestreo).

El resultado de `fftfreq(N, T)` es un vector con $N$ valores de frecuencia. Nos dice qué frecuencia (en Hz) corresponde a cada uno de los $N$ puntos que calculó la `fft`.

Primero importaremos las funciones y librerías necesarias.

%% code prov-09
import numpy as np
from scipy.fft import fftfreq
import matplotlib.pyplot as plt

%% md prov-10
Como ejemplo vamos a graficar una señal senoidal de frecuencia de 50 Hz.

Crearemos un vector que llamaremos `t` que representará el tiempo y otro vector `x` que representará la señal senoidal.

Para definir nuestra señal, necesitamos establecer:
1.  **`N` (Número de muestras):** Cuántos puntos tomaremos. Usaremos 4000.
2.  **`T` (Período de muestreo):** El tiempo entre un punto y el siguiente. Usaremos 0.0001 segundos (0.1 ms).
3.  **`fs` (Frecuencia de muestreo):** Es la inversa de T ($f_s = 1/T$). En nuestro caso, $f_s = 1 / 0.0001 = 10000 Hz$. (Esto cumple sobradamente el Teorema de Nyquist, que exigiría $f_s > 2 \times 50 Hz = 100 Hz$).
4.  **`t` (Vector de tiempo):** Usando `linspace`, creamos 4000 puntos desde `0.0` hasta `N*T` (0.4 segundos).

%% code prov-11
# Constantes de la señal
N = 4000  # Número de muestras de la señal
T = 0.0001  # Intervalo de muestreo (fs = 1/T = 10000 Hz)
t = np.linspace(0.0, N*T, N)  # Vector de tiempo (Duración total = N*T = 0.4s)
x = np.sin(50.0 * 2.0*np.pi * t)   # Señal sinusoide de frecuencia f = 50 Hz

%% md prov-12
Ahora que tenemos nuestra señal `x` en el tiempo, calcularemos su FFT.

%% code prov-13
# 1. Transformada de Fourier de la señal
x_fft = fft(x)

# 2. Vector de frecuencias correspondientes
frecuencias = fftfreq(N, T)

%% md prov-14
###  Una explicación clave: Normalización de la Amplitud

Si inspeccionamos `x_fft`, veremos números complejos muy grandes. La salida de la FFT de `scipy` está escalada por un factor de $N$ (el número de muestras). Para obtener la amplitud real de la señal, debemos "normalizar" este resultado.

Hay dos cosas que considerar:

1.  **Escalado por $N$:** Para revertir el escalado del algoritmo, debemos dividir la salida de la FFT por $N$. ( `np.abs(x_fft) / N` ).
2.  **Simetría de Señales Reales:** Nuestra señal `x` es "real" (no tiene números imaginarios). Una propiedad fundamental de las señales reales es que su espectro de Fourier es simétrico. La energía de nuestra senoide de 50 Hz se divide por igual: la mitad va al pico de $+50 Hz$ y la otra mitad al pico de $-50 Hz$.

Si dividimos `np.abs(x_fft) / N`, y la amplitud de nuestra senoide era 1.0, los picos en la gráfica de FFT tendrían un valor de 0.5 cada uno.

**¿Cómo hacemos para que el pico en la gráfica muestre la amplitud original (1.0)?**

Simple: tomamos la amplitud escalada por $N$ (`np.abs(x_fft) / N`) y la multiplicamos por 2 para "recuperar" la energía del pico negativo y sumarla al positivo.

Esto nos da la fórmula: `Amplitud = (np.abs(x_fft) / N) * 2` , que es lo mismo que: `Amplitud = np.abs(x_fft) / (N / 2)`

*Nota: Esta normalización por `N/2` se aplica a todas las frecuencias excepto a la componente de DC (frecuencia 0), que solo se divide por `N` porque no tiene una contraparte negativa.*

%% code prov-15
# 3. Normalización de la amplitud (para un espectro de "una cara")
amplitud_normalizada = np.abs(x_fft) / (N / 2)

%% md prov-16
Finalmente, graficamos la señal original y su espectro de frecuencia.

%% code prov-17
# Graficamos la señal original y su espectro de frecuencia (versión mejorada con zoom)

# Definimos fs para usarla en el límite del gráfico
fs = 1/T

# Ajustamos el tamaño de la figura para que quepan tres gráficos
plt.figure(figsize=(10, 6))

# --- Gráfico 1: Señal en el Dominio del Tiempo ---
plt.subplot(3, 1, 1) # Cambiamos a 3 filas, 1 columna, gráfico 1
plt.plot(t[0:1000], x[0:1000])
plt.title('Señal Original (primeros 0.1s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# --- Gráfico 2: Espectro de Frecuencia Completo ---
plt.subplot(3, 1, 2) # Cambiamos a 3 filas, 1 columna, gráfico 2
# Graficamos el vector de frecuencias contra la amplitud normalizada
plt.plot(frecuencias, amplitud_normalizada)
plt.title('Espectro de Amplitud (Doble Cara - Completo)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud Normalizada')
# Mostramos el espectro completo hasta la frecuencia de Nyquist (fs/2)
plt.xlim(-fs/2, fs/2)
plt.grid(True)

# --- Gráfico 3: Zoom en el Espectro ---
# Este es el nuevo gráfico que solicitaste
plt.subplot(3, 1, 3) # Cambiamos a 3 filas, 1 columna, gráfico 3
plt.plot(frecuencias, amplitud_normalizada)
plt.title('Espectro de Amplitud (Zoom en ±50 Hz)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud Normalizada')
# Aplicamos el ZOOM: Limitamos el eje x de -100 Hz a 100 Hz
plt.xlim(-100, 100)
plt.grid(True)

# Ajusta los gráficos para que no se superpongan
plt.tight_layout()
plt.show()

%% md prov-18
Podemos ver un espectro de amplitud simétrico con componentes (picos) exactamente en $50Hz$ y $-50Hz$. Gracias a nuestra normalización por `N/2`, la amplitud de estos picos es 1.0, que coincide con la amplitud de nuestra señal original `x = 1.0 * np.sin(...)`.

%% md enu-01
### 🎯 Ejercicio 1: Suma de Senoidales

Ahora que entendemos el proceso, vamos a aplicar el principio de superposición. La Transformada de Fourier es lineal, lo que significa que la transformada de una suma de señales es igual a la suma de sus transformadas.

**Objetivo:** Añadir una segunda señal senoidal a `x` y observar cómo cambia el espectro.

**Pasos:**
1.  Crear una nueva señal `x2` que sea una senoidal con frecuencia $f2 = 80Hz$ y amplitud 0.5. (Usar el mismo vector de tiempo `t`).
2.  Crear una señal compuesta `y` que sea la suma de `x` (la de 50 Hz) y `x2` (la de 80 Hz).
3.  Calcular la FFT de la señal `y` ( `y_fft = fft(y)` ).
4.  Normalizar la amplitud de `y_fft` usando el método de `N/2` que aprendimos.
5.  Graficar el espectro de amplitud de `y` ( `frecuencias` vs. `amplitud_normalizada_y` ).
6.  Graficar la señal `y` en el tiempo para ver cómo se ve la onda compuesta.*

Agregue todas las celdas de texto y código que necesite para realizar el ejercicio.

%% md enu-02
###  Ejercicio 2: Espectro de una Onda Cuadrada

Las ondas senoidales son simples (solo tienen un pico en la frecuencia), pero otras formas de onda, como las cuadradas o triangulares, están compuestas por una **suma infinita de senoidales** (armónicos).

**Objetivo:** Calcular y visualizar el espectro de una onda cuadrada.

**Pasos:**
1.  Importar `signal` desde `scipy` ( `from scipy import signal` ).
2.  Crear una señal `x_cuadrada` usando `signal.square(2.0 * np.pi * f * t)`. Usa una frecuencia `f = 25Hz`.
3.  Calcular la FFT de `x_cuadrada`.
4.  Normalizar la amplitud.
5.  Graficar el espectro. ¿Qué observas? Deberías ver un pico en la frecuencia fundamental (25 Hz) y luego picos más pequeños en sus armónicos impares (75 Hz, 125 Hz, 175 Hz, etc.).

Agregue todas las celdas de texto y código que necesite para realizar el ejercicio.

%% code act-01


%% md prov-19
## Construyendo Intuición: FFT Interactiva

Hasta ahora hemos analizado señales "estáticas". Para desarrollar una mejor intuición de cómo los cambios en el tiempo afectan a la frecuencia, crearemos una figura interactiva usando `ipywidgets`.

%% code prov-20
from ipywidgets import interactive
import ipywidgets as widgets

%% md prov-21
Primero, definimos los parámetros fijos de nuestro entorno de prueba.
Usaremos una frecuencia de muestreo $f_s = 1000 Hz$, por lo que $T = 0.001 s$.

%% code prov-22
# Parámetros fijos de la señal
fs = 1000  # Frecuencia de muestreo (fs = 1000 Hz)
N = 4000  # Número de muestras de la señal
T = 1.0 / fs  # Intervalo de muestreo (T = 0.001 s)
t = np.linspace(0.0, N * T, N)  # Vector de tiempo de 4 segundos (4000 muestras en total)

%% md prov-23
Ahora, definimos una función que recalcula y redibuja las gráficas cada vez que movemos un *slider*.

Nota sobre la normalización en este gráfico:
Observa que aquí dividimos por `N` y no por `N/2`. Esto es una elección de visualización. Al dividir solo por `N`, mostramos el espectro de "doble cara" donde la amplitud original (ej: 1.0) se divide entre el pico positivo (0.5) y el negativo (0.5). Esto es útil para ver la simetría claramente.

%% code prov-24
# Función para actualizar la señal y su FFT
def actualizar_grafico(frecuencia=50.0, amplitud=1.0):
    # Generación de la señal sinusoidal con los parámetros variables
    x = amplitud * np.sin(frecuencia * 2.0 * np.pi * t)

    # Cálculo de la FFT
    x_fft = fft(x)
    frecuencias = fftfreq(N, T)

    # Crear las figuras
    plt.figure(figsize=(9, 4))

    # Subplot de la señal en el dominio del tiempo (mostrando solo el primer segundo)
    plt.subplot(2, 1, 1)
    plt.plot(t[:fs], x[:fs])  # Mostrar solo el primer segundo de la señal (primeras 1000 muestras)
    plt.title('Señal en el Tiempo (Primer Segundo)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.ylim(-2, 2)  # Fija la amplitud en el eje y
    plt.grid()

    # Subplot del espectro de frecuencias
    plt.subplot(2, 1, 2)
    # Normalización por N (picos de amplitud/2)
    plt.plot(frecuencias, np.abs(x_fft) / N)
    plt.title('Espectro de amplitud (Doble Cara, pico = Amplitud/2)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud Normalizada')
    # Hacemos zoom de -100 a 100 Hz
    plt.xlim(-100, 100)
    plt.ylim(0, 1)  # Eje de amplitudes fijo
    plt.grid()

    plt.tight_layout()
    plt.show()

%% md prov-25
Finalmente, usamos la función `interactive` para conectar nuestra función `actualizar_grafico` a dos *sliders* (deslizadores): uno para la frecuencia y otro para la amplitud.

%% code prov-26
# Crear la interacción
interactive_plot = interactive(
    actualizar_grafico,
    frecuencia=(1, 100, 1),  # Slider de Frecuencia: de 1 a 100 Hz, en pasos de 1 Hz
    amplitud=(0.1, 2, 0.1)      # Slider de Amplitud: de 0.1 a 2.0, en pasos de 0.1
)
display(interactive_plot)

%% md prov-27
## Transición: De Señales a Sistemas

Hemos explorado el **Análisis de Fourier** (DFT/FFT), que es la herramienta que nos permite ver *de qué* está compuesta una señal (su espectro).

Ahora, cambiaremos nuestro enfoque para analizar los **Sistemas LTI** (Lineales e Invariantes en el Tiempo). Estos sistemas son los "procesadores" de señales: toman una señal de entrada $x(t)$ y entregan una señal de salida $y(t)$.

Usaremos `scipy.signal` para analizar cómo estos sistemas (definidos por sus ecuaciones diferenciales o funciones de transferencia) responden a diferentes estímulos.

%% md prov-28
## Segunda parte: Utilidades de python Para sistemas LTI descrito por su función de transferencia

%% md prov-29
## Sistemas LTI continuos

En esta sección, exploraremos cómo la biblioteca `scipy.signal` de Python nos permite modelar y analizar sistemas **LTI (Lineales e Invariantes en el Tiempo)** en el dominio continuo.

Un sistema LTI es un "bloque" que procesa una señal de entrada $x(t)$ para producir una señal de salida $y(t)$. Lo que lo hace especial es que obedece a dos principios:
1.  **Linealidad:** Si la entrada es una suma de señales ($a \cdot x_1(t) + b \cdot x_2(t)$), la salida es la suma de sus respuestas ($a \cdot y_1(t) + b \cdot y_2(t)$).
2.  **Invariancia en el Tiempo:** Si retardas la entrada en el tiempo, la salida se retarda exactamente la misma cantidad, sin cambiar su forma.

Estos sistemas se describen matemáticamente mediante ecuaciones diferenciales, o más comúnmente en nuestro campo, mediante su **Función de Transferencia** $H(s)$ en el dominio de Laplace.

### Uso Básico de lti

La función `lti` (`scipy.signal.lti`) nos permite crear un objeto que representa al sistema a partir de los coeficientes de su función de transferencia $H(s)$.

Recordemos que $H(s)$ es la relación entre la transformada de Laplace de la salida $Y(s)$ y la transformada de Laplace de la entrada $X(s)$:

$$
H(s) = \frac{Y(s)}{X(s)} = \frac{\text{polinomio del numerador}}{\text{polinomio del denominador}}
$$

Para usar `lti`, le pasamos dos listas (o arrays de numpy) que contienen los coeficientes de estos polinomios, en orden de potencia **decreciente** de $s$.

%% md prov-30
Definamos un sistema de ejemplo:
$$
H(s) = \frac{s+5}{s^2 + 3s + 2}
$$

%% code prov-31
from scipy.signal import lti

# H(s) = (1*s + 5) / (1*s^2 + 3*s + 2)

# Coeficientes del numerador (s + 5)
numerador = [1, 5]
# Coeficientes del denominador (s^2 + 3s + 2)
denominador = [1, 3, 2]

# Crear el objeto 'sistema' LTI
sistema = lti(numerador, denominador)

print(sistema)

%% md prov-32
Este objeto `sistema` que acabamos de crear contiene toda la información de la ecuación diferencial asociada:
$$
\frac{d^2y(t)}{dt^2} + 3\frac{dy(t)}{dt} + 2y(t) = \frac{dx(t)}{dt} + 5x(t)
$$

%% md prov-33
### Operaciones Comunes con `lti`

Una vez definido el objeto `sistema`, podemos analizarlo de varias maneras para entender su comportamiento.

%% md prov-34
#### 1. Respuesta al impulso

**¿Qué es?** La **respuesta al impulso**, $h(t)$, es la salida teórica del sistema cuando la entrada es un "impulso" perfecto (conocido como Delta de Dirac, $\delta(t)$).

**¿Por qué es importante?** Esta respuesta es como la "huella dactilar" del sistema. Define completamente su comportamiento. De hecho, la respuesta al impulso $h(t)$ es la Transformada Inversa de Laplace de la propia función de transferencia $H(s)$.

**En Python:** Usamos el método `.impulse()` del objeto `sistema`. Este nos devuelve dos vectores: `t` (el vector de tiempo) y `y_impulso` (la respuesta $h(t)$).

%% code prov-35
# Calcular la respuesta al impulso
t_imp, y_impulso = sistema.impulse()

# Graficar
plt.figure(figsize=(8, 4))
plt.plot(t_imp, y_impulso)
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida h(t)')
plt.title('Respuesta al Impulso')
plt.grid(True)
plt.show()

%% md prov-36
#### 2. Respuesta al escalón

**¿Qué es?** La **respuesta al escalón** es la salida del sistema cuando la entrada es un "escalón" unitario, $u(t)$ (una señal que es 0 para $t<0$ y 1 para $t \ge 0$).

**¿Por qué es importante?** Es la prueba más común para caracterizar un sistema. Nos permite ver visualmente:
-   **Ganancia en estado estacionario:** El valor final al que se estabiliza la salida.
-   **Tiempo de subida (Rise time):** Cuánto tarda en ir del 10% al 90% del valor final.
-   **Sobreoscilación (Overshoot):** Cuánto "se pasa" del valor final antes de estabilizarse.
-   **Tiempo de estabilización (Settling time):** Cuánto tarda en quedarse cerca del valor final.

**En Python:** Usamos el método `.step()`. Devuelve `t` (tiempo) y `y_escalon` (la respuesta).

%% code prov-37
# Calcular la respuesta al escalón
t_esc, y_escalon = sistema.step()

# Graficar
plt.figure(figsize=(8, 4))
plt.plot(t_esc, y_escalon)
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida y(t)')
plt.title('Respuesta al Escalón')
plt.axhline(y=2.5, color='r', linestyle='--', label='Valor Estacionario (Ganancia DC = 5/2 = 2.5)') # Ganancia DC = H(s=0)
plt.legend()
plt.grid(True)
plt.show()

%% md prov-38
#### 3. Respuesta a una entrada arbitraria (respuesta temporal)

**¿Qué es?** Esta es la simulación más general. La función `lsim` (simulación lineal) calcula la respuesta del sistema $y(t)$ a *cualquier* señal de entrada arbitraria $x(t)$ que le proporcionemos.

**En Python:** Usamos `lsim` de `scipy.signal`.
-   **Parámetros:** `lsim(sistema, U, T)`
    -   `sistema`: Nuestro objeto `lti`.
    -   `U`: El vector con los valores de nuestra señal de entrada, que llamaremos `x_in`.
    -   `T`: El vector de tiempo correspondiente a la entrada `x_in`.
-   **Salida:** Devuelve `t_out` (tiempo de salida), `y_out` (la respuesta $y(t)$), y `x_out` (el estado interno del sistema, que por ahora ignoraremos).

**Objetivo del gráfico:** Para que sea más didáctico, graficaremos la señal de entrada $x(t)$ y la señal de salida $y(t)$ una encima de la otra. Esto nos permite comparar visualmente cómo el sistema "transforma" la entrada (por ejemplo, si la amplifica, la atenúa o la desfasa).

%% code prov-39
from scipy.signal import lsim

# 1. Definir el vector de tiempo sobre el cual simularemos
# Creamos 100 puntos espaciados linealmente entre 0 y 10 segundos.
t_in = np.linspace(0, 10, 100)

# 2. Definir la señal de entrada arbitraria 'x_in'
# Usaremos una onda senoidal con frecuencia angular 1 rad/s.
x_in = np.sin(t_in)

%% md prov-40
Ahora, simulamos el sistema con esa entrada y graficamos los resultados.

%% code prov-41
# 3. Simular la respuesta del sistema
# Le pasamos el sistema, nuestra señal de entrada 'x_in' y su vector de tiempo 't_in'
t_out, y_out, _ = lsim(sistema, U=x_in, T=t_in) # El guion bajo ignora el estado 'x_out'

# 4. Graficar la entrada y la salida
plt.figure(figsize=(9, 5))

# Subplot 1: La entrada
plt.subplot(2, 1, 1)
plt.plot(t_in, x_in, 'b-', label='Entrada x(t) = sin(t)')
plt.title('Señal de Entrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

# Subplot 2: La salida
plt.subplot(2, 1, 2)
plt.plot(t_out, y_out, 'r-', label='Salida y(t)')
plt.title('Señal de Salida (Respuesta del Sistema)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout() # Ajusta los gráficos para que no se superpongan
plt.show()

%% md prov-42
#### 4. Análisis en frecuencia

**¿Qué es?** La **respuesta en frecuencia** describe cómo responde el sistema a entradas senoidales de *diferentes* frecuencias (esto es el Diagrama de Bode).
Se obtiene evaluando la función de transferencia $H(s)$ en el eje imaginario, es decir, sustituyendo $s = j\omega$ (donde $\omega$ es la frecuencia angular en rad/s).

El resultado $H(j\omega)$ es un número complejo:
-   **$|H(j\omega)|$ (Magnitud):** Representa la ganancia (amplificación o atenuación) del sistema a esa frecuencia.
-   **$\angle H(j\omega)$ (Fase):** Representa el desfasaje que introduce el sistema a esa frecuencia.

**En Python:** Usamos el método `.freqresp()` (frequency response).

%% code prov-43
# 1. Definir el rango de frecuencias angulares (omega, ω) a analizar
# Creamos 100 puntos espaciados linealmente entre 0.1 y 10 rad/s
w_in = np.linspace(0.1, 10, 100)

# 2. Calcular la respuesta en frecuencia
# 'freqresp' evalúa H(jω) para cada ω en 'w_in'
# Devuelve las frecuencias (w_out) y la respuesta compleja (H_out)
w_out, H_out = sistema.freqresp(w=w_in)

# 3. Graficar la magnitud
# Usamos np.abs() para obtener la magnitud de la respuesta compleja H_out
plt.figure(figsize=(8, 4))
plt.plot(w_out, np.abs(H_out))
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Magnitud (Ganancia)')
plt.title('Respuesta en Frecuencia (Diagrama de Bode - Magnitud)')
plt.grid(True)
plt.show()

%% md prov-44
#### 5. Polos y Ceros

**¿Qué son?** Los polos y ceros son las "huellas dactilares" del sistema en el plano complejo $s$.

-   **Ceros:** Son las raíces (los valores de $s$) que hacen que el **numerador** de $H(s)$ sea cero. Son las frecuencias para las cuales la respuesta del sistema es cero ($H(s) = 0$).
-   **Polos:** Son las raíces (los valores de $s$) que hacen que el **denominador** de $H(s)$ sea cero. Son las frecuencias para las cuales la respuesta del sistema tiende a infinito ($H(s) \to \infty$).

**¿Por qué son importantes?**
-   Los **polos** determinan la **estabilidad** del sistema. Un sistema es estable si todos sus polos tienen parte real negativa (están en el semiplano izquierdo del plano $s$).
-   Los **ceros** se utilizan para diseñar filtros, ya que pueden "anular" o atenuar fuertemente frecuencias específicas no deseadas.

**En Python:** El objeto `lti` ya los tiene calculados como propiedades: `.poles` y `.zeros`.

%% code prov-45
# Acceder a las propiedades de polos y ceros del objeto 'sistema'
polos = sistema.poles
ceros = sistema.zeros

print(f'Polos del sistema: {polos}')
print(f'Ceros del sistema: {ceros}')

# Verificamos la estabilidad
if np.all(np.real(polos) < 0):
    print("El sistema es ESTABLE (todos los polos tienen parte real negativa).")
else:
    print("El sistema es INESTABLE (al menos un polo tiene parte real no negativa).")

%% md enu-03
###  Ejercicio 3: Análisis de un Sistema LTI

**Objetivo:** Aplicar todo lo aprendido para analizar el sistema del ejercicio de gabinete 5b. del Trabajo práctico n° 7: Transformada de Laplace.

**Pasos:**
1.  **Definir el Sistema:**
    * Identifica los coeficientes del **numerador** y **denominador** de la función de transferencia $H(s)$ del ejercicio 5b.
    * Crea el objeto `sistema_e5b` usando `lti(numerador, denominador)`.
2.  **Analizar la Respuesta al Impulso:**
    * Calcula la respuesta al impulso usando `sistema_e5b.impulse()`.
    * Grafica $h(t)$.
    * Compara esta gráfica con la respuesta analítica $h(t)$ que calculaste a mano en el gabinete. ¿Coinciden?
3.  **Analizar Polos y Ceros:**
    * Imprime los `sistema_e5b.poles` y `sistema_e5b.zeros`.
    * Basándote en la ubicación de los polos, ¿el sistema es estable?
4.  **Analizar la Respuesta en Frecuencia:**
    * Calcula y grafica la magnitud de la respuesta en frecuencia usando `sistema_e5b.freqresp()`.
    * *Sugerencia:* Para un Diagrama de Bode estándar, usa `plt.xscale('log')` en tu gráfico.

%% code act-02


%% md prov-46
### Animación Interactiva: Sistema LTI bajo entrada Senoidal

**Objetivo:** Visualizar cómo un sistema LTI responde a una señal de entrada senoidal a medida que cambiamos su frecuencia.

**Pasos:**
1.  **Importar librerías:** Importaremos `numpy`, `matplotlib.pyplot`, `scipy.signal` (para `lti` y `freqresp`) e `ipywidgets` (para la interactividad).
2.  **Definir el Sistema:** Crearemos el mismo objeto `sistema` $H(s) = \frac{s+5}{s^2 + 3s + 2}$ que hemos estado usando.
3.  **Calcular el Espectro (Estático):** La respuesta en frecuencia (Diagrama de Bode) del sistema es una característica *fija* del mismo. No cambia con la entrada. Para que la animación sea rápida, calcularemos este gráfico **una sola vez** al principio.
4.  **Definir la Función Interactiva:** Crearemos una función (`actualizar_grafico_lti`) que tome la frecuencia de entrada ($\omega$) como argumento.
5.  **Dentro de la función:**
    * Calcularemos el vector de tiempo `t` (adaptado para mostrar 5 ciclos de la $\omega$ seleccionada).
    * Calcularemos la señal de entrada $x(t) = \sin(\omega t)$.
    * Calcularemos la respuesta en **régimen permanente** $y(t)$.
    * Dibujaremos los tres gráficos: $x(t)$, $y(t)$, y el espectro $|H(j\omega)|$ con un punto en la $\omega$ seleccionada.
6.  **Crear el Widget:** Usaremos `interactive` para conectar un *slider* (deslizador) a nuestra función.

%% md prov-47
#### Paso 1 y 2: Importar librerías y Definir el Sistema

%% code prov-48
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, freqresp
from ipywidgets import interactive, widgets
from IPython.display import display

# 2. Definir el sistema H(s) = (s+5) / (s^2 + 3s + 2)
numerador = [1, 5]
denominador = [1, 3, 2]
sistema = lti(numerador, denominador)

%% md prov-49
#### Paso 3: Pre-calcular el Diagrama de Bode

Calculamos la respuesta en frecuencia del sistema en un rango amplio de frecuencias (de 0.1 a 100 rad/s). Estos vectores (`w_bode` y `mag_bode`) no cambiarán y los usaremos como "fondo" en nuestro gráfico de espectro.

%% code prov-50
# 3. Calcular la respuesta en frecuencia (Bode) una sola vez
# Definimos un rango amplio de frecuencias angulares (ω) para el gráfico de fondo
w_bode = np.logspace(-1, 2, 200) # 200 puntos entre 10^-1 (0.1) y 10^2 (100) rad/s

# Calculamos la respuesta en frecuencia compleja
w_out, H_complex = sistema.freqresp(w=w_bode)

# Calculamos la magnitud (en valores absolutos, no en dB)
mag_bode = np.abs(H_complex)

%% md prov-51
#### Paso 4 y 5: Definir la Función Interactiva

Esta es la función principal. Para la salida en régimen permanente $y(t)$, recordamos que para una entrada $x(t) = A \cdot \sin(\omega t)$, la salida será $y(t) = A \cdot |H(j\omega)| \cdot \sin(\omega t + \angle H(j\omega))$.

Usaremos `sistema.freqresp(w=[w_entrada])` para obtener la magnitud $|H(j\omega)|$ y la fase $\angle H(j\omega)$ en la frecuencia específica que elija el slider.

%% code prov-52
def actualizar_grafico_lti(w_entrada=1.0):

    # --- Cálculo de la Entrada y Salida en el Tiempo ---

    # 1. Definir un vector de tiempo 't' FIJO de 0 a 10 segundos
    t = np.linspace(0, 10, 500) # 500 puntos para una buena resolución

    # 2. Señal de entrada (Amplitud 1)
    x_in = np.sin(w_entrada * t)

    # 3. Calcular la respuesta en régimen permanente (Magnitud y Fase)
    w_ss, H_ss = sistema.freqresp(w=[w_entrada])
    magnitud_ss = np.abs(H_ss[0]) # Magnitud |H(jω)|
    fase_ss = np.angle(H_ss[0])     # Fase ∠H(jω)

    # 4. Señal de salida en régimen permanente
    y_ss = magnitud_ss * np.sin(w_entrada * t + fase_ss)

    # --- Creación de los Gráficos ---

    # 1. Tamaño de figura compacto
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 5.5))

    # Ajuste dinámico de los límites Y
    max_amp = max(1.0, magnitud_ss) * 1.2

    # --- Gráfico 1: Entrada x(t) ---
    ax1.plot(t, x_in, 'b-', label='Entrada x(t) = sin(t)')
    ax1.set_title(f'Entrada: $x(t) = \sin({w_entrada:.2f} \cdot t)$')
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Amplitud')
    ax1.set_ylim(-max_amp, max_amp)
    ax1.set_xlim(0, 10) # Eje de tiempo FIJO
    ax1.legend()
    ax1.grid(True)

    # --- Gráfico 2: Salida y(t) ---
    ax2.plot(t, y_ss, 'r-', label='Salida y(t)')
    ax2.set_title(f'Salida Est. Estacionario: $y(t) = {magnitud_ss:.2f} \cdot \sin({w_entrada:.2f} \cdot t + {fase_ss:.2f})$')
    ax2.set_xlabel('Tiempo (s)')
    ax2.set_ylabel('Amplitud')
    ax2.set_ylim(-max_amp, max_amp)
    ax2.set_xlim(0, 10) # Eje de tiempo FIJO
    ax2.legend()
    ax2.grid(True)

    # --- Gráfico 3: Espectro de Amplitud (Bode) ---
    ax3.plot(w_bode, mag_bode, label='Magnitud $|H(j\omega)|$')
    ax3.plot(w_entrada, magnitud_ss, 'ro', markersize=10,
             label=f'Ganancia @ {w_entrada:.2f} rad/s = {magnitud_ss:.2f}')

    ax3.set_title('Respuesta en Frecuencia (Magnitud Lineal)')
    ax3.set_xlabel('Frecuencia (rad/s)')
    ax3.set_ylabel('Magnitud (Ganancia)')
    ax3.set_xscale('log') # Mantenemos el eje X logarítmico

    # *** ESTE ES EL CAMBIO SOLICITADO ***
    # Se cambia la escala Y a lineal (linear) en lugar de logarítmica (log)
    ax3.set_yscale('linear')

    # Ajustamos el grid para la nueva escala (solo 'major' en Y)
    ax3.grid(True, which='major', axis='y')
    ax3.grid(True, which='both', axis='x')

    ax3.legend()

    plt.tight_layout()
    plt.show()

%% md prov-53
#### Paso 6: Crear y Mostrar el Widget Interactivo

Finalmente, creamos el *slider* y lo conectamos a nuestra función.

%% code prov-54
# Creamos un slider para la frecuencia angular 'w_entrada'
# Rango de 0.1 a 20 rad/s (en pasos de 0.1)
w_slider = widgets.FloatSlider(
    value=1.0,
    min=0.1,
    max=20.0,
    step=0.1,
    description='Frecuencia $\omega$ (rad/s):',
    continuous_update=False, # Solo actualiza al soltar el mouse (más rápido)
    readout_format='.1f',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='80%')
)

# Creamos la visualización interactiva
interactive_plot_lti = interactive(
    actualizar_grafico_lti,
    w_entrada=w_slider
)

# Mostramos el widget
display(interactive_plot_lti)

%% md prov-55
### 🔎 ¿Qué observar en el gráfico interactivo?

Esta simulación conecta los tres conceptos clave: la **entrada**, la **salida** y la **respuesta en frecuencia** (Bode) del sistema.

**¡Prueba esto!**

1.  **Mueve el slider de frecuencia $\omega$ lentamente de 0.1 a 20 rad/s.**
2.  **Observa los Gráficos 1 y 2 (Tiempo):**  verás cómo las ondas de entrada y salida "se comprimen" (su frecuencia aumenta) a medida que mueves el *slider* hacia la derecha.
3.  **Observa el Gráfico 3 (Bode):** Verás el punto rojo deslizarse a lo largo de la curva de magnitud. Fíjate que para este sistema (un filtro pasa-bajos), la ganancia es alta a bajas frecuencias (cercana a 2.5) y "cae" (se atenúa) a altas frecuencias.
4.  **Conecta los gráficos:**
    * **Amplitud:** Compara la amplitud de la señal de salida $y(t)$ con la de entrada $x(t)$ (que siempre es 1). Verás que cuando el punto rojo en el gráfico de Bode está alto (alta ganancia, $\omega$ baja), la amplitud de $y(t)$ es grande (ej: ganancia $\approx 2.5$). A medida que mueves el *slider* y el punto rojo "cae", la amplitud de $y(t)$ se hace cada vez más pequeña. ¡El sistema está atenuando esas frecuencias!
    * **Fase:** Observa el desfasaje (el "retraso") entre la onda de entrada (azul) y la de salida (roja). Verás que este desfasaje (indicado como $\angle H(j\omega)$ en el título del gráfico 2) también cambia a medida que cambia la frecuencia.
