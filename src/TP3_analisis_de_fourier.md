---
prefix: TP3_analisis_de_fourier
source: TP3_analisis_de_fourier.ipynb
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
        </p>
                <!--<p><em>Profesor Mg. Ing. Javier Velez</em></p>-->
    </div>
</center>

%% md prov-01
# Trabajo Práctico $N^{\circ}2$: Análisis de Fourier

%% md prov-02
Celda a ejecutar para importar las librerías necesarias:

%% code prov-03
import sympy as sym
import numpy as np
import cmath
import matplotlib.pyplot as plt
from IPython.display import  Math

%% md prov-04
# 1.  Serie trigonométrica de Fourier

%% md prov-05
La serie trigonométrica de Fourier de una función **periódica** $f(t)$ se define como:

$$ f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n \cos(nw_0t) + b_n \sin(nw_0t)] \tag{1}$$

Donde $w_0$ es la frecuencia angular fundamental de la función $f(t)$, y los coeficientes $a_n$ y $b_n$ están definidos por:
$$ a_0 = \frac{2}{T} \int_{T} f(t)  dt$$
$$ a_n = \frac{2}{T} \int_{T} f(t) \cos(nw_0t) dt$$
$$ b_n = \frac{2}{T} \int_{T} f(t) \sin(nw_0t) dt$$

Aquí, $T$ es el período fundamental de la función $f(t)$, y los límites de integración son un período de la función.


%% md prov-06
## 1.1
Obtención de la serie trigonométrica con python

%% md prov-07
Supongamos una señal pulsante rectangular de amplitud $1$ con periodo $T=4s$ y ancho de pulso de $2s$.  

%% md prov-08
Matemáticamente, un período se describe como:

$f(t) =
\begin{cases}
0 & \text{si} -2 \leq t < -1 \\
1 & \text{si } -1 \leq t < 1 \\
0 & \text{si }  1 \leq t < 2 \\
\end{cases}$

%% md prov-09
Primero definiremos el símbolo `t` que representará nuestra variable tiempo.

%% code prov-10
t = sym.Symbol('t', real=True) # símbolo que representará el tiempo, que es una variable real

# Definimos el periodo fundamental y la frecuencia de la señal

T0  = 4

w0 = 2*sym.pi/T0 # sym.pi representa al número pi de manera simbólica


%% md prov-11
Utilizaremos la función `Piecewise()` de la librería `SymPy`  para representar la función sobre un período:

%% code prov-12
f = sym.Piecewise(
    (0, (t < -1) | (t > 1) ),
    (1, (t >= -1) & (t <= 1)),
)

%% md prov-13
La definimos sobre un período porque solo necesitamos integrar sobre un período para obtener los coeficientes de la serie trigonométrica de Fourier.

%% md prov-14
Ahora podemos graficar la función `f` usando `sym.plot()`

%% code prov-15
sym.plot(f, (t, -2, 2))

%% md prov-16
Procedemos entonces a calcular los coeficientes de la serie trigonométrica de Fourier.

%% md prov-17
Primero calcularemos los coeficientes $a_0$: $$ a_0 = \frac{2}{T} \int_{T} f(t)  dt = \frac{2}{T} \int_{-1}^{1} 1  dt $$



%% code prov-18
a0 =  (2/T0) * sym.integrate(1, (t, -1, 1))
display(a0)

%% md prov-19
Ahora calcularemos los coeficientes $a_n$: $$ a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(nw_0t) dt$$

Para esto definiremos el índice de nuestra serie `n` como una variable simbólica entera positiva, ya que ya calculamos el $a_0$ y las sumatorias sobre senos y cosenos comienzan en 1.

%% code prov-20
# Primero definimos el índice discreto n como variable simbólica entera positiva.
n = sym.symbols('n', integer=True, positive=True)

# Luego definimos una variable que represente el argumento de la integral
arg_integral  = f * sym.cos(n * w0 * t)

# Ahora calculamos la integral
integral = sym.integrate(arg_integral,(t, -2, -2+T0))

# Por último multiplicamos pot (2/T0)
an = (2/T0) * integral

display(an)



%% md prov-21
Ahora utilizaremos el método `.subs(simbolo, valor)` para evaluar sobre los distintos n.

%% md prov-22
Definimos un número N de coeficientes $a_n$ que calcularemos:

%% code prov-23
N = 10
for k in range(1, N+1):
  # La función Math y display se utilizan para que se visualice en un formato más agradable (LaTEX)
    coef = an.subs(n, k).simplify()

    display(Math(f'a_{{{k}}}: {coef}'))

%% md prov-24
Ahora calculemos los coeficientes $b_n$  $$ b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(nw_0t) dt$$

%% code prov-25
# Definimos una variable que represente el argumento de la integral
arg_integral  = f * sym.sin(n * w0 * t)

# Ahora calculamos la integral
integral = sym.integrate(arg_integral,(t, -2, -2+T0))

# Por último multiplicamos por 2/T0
bn = (2/T0) * integral
bn = sym.simplify(bn)

bn


%% md prov-26
Vemos que todos los coeficientes $b_n$ son cero, lo que es esperable ya que la señal es par. Habiendo calculados los coeficientes $a_n$ y $b_n$ ya podemos expresar la serie con: $$ f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} [a_n \cos(nw_0t) + b_n \sin(nw_0t)]$$

$$ f(t) = \frac{1}{2} + \sum_{n=1}^{\infty} \frac{2 \sin(n \frac{\pi}{2})}{n\pi} \cos(n \frac{\pi}{2}t) = \frac{1}{2} + \sum_{n=1}^{\infty} \operatorname{sinc}(n \frac{\pi}{2})  \cos(n \frac{\pi}{2}t) $$

%% md prov-27
Hasta aquí utilizamos la definición de la serie trigonométrica de Fourier. Para simplificar el procedimiento `SymPy` tiene desarrollada el método `fourier_series()` que nos ahorrará este trabajo:

%% code prov-28
# Definimos el número de términos a visualizar
N = 5


# Utilizamos la función fourier_series
s = sym.fourier_series(f, (t, -2, -2+T0))


%% md prov-29
El primer parámetro es la expresión sobre la cual queremos calcular la serie de Fourier, y el segundo parámetro es una tupla que contiene la variabla sobre la cual la calcularemos y el intervalo de la funcíon que representa el preríodo a analizar.

La serie de Fourier calculada de esta manera nos permite utilizar el método `.truncate(N)` que nos permite definir la cantidad de terminos a truncar.

%% code prov-30
# Definimos la cantidad de términos a utilizar
N=5
s.truncate(n=N)

%% md prov-31
Ahora graficaremos los resultados de la serie variando la cantidad de términos utilizados:

%% code prov-32
# Definimos la cantidad de términos a utilizar
N=4

# Graficamos la serie truncada en N términos y un
# periodo de la función  para poder comparar
sym.plot(s.truncate(n=N), f)

%% md prov-33
Podemos graficar las componentes por separado:

%% code prov-34
N=4
s_truncada = s.truncate(n=N)

#Convertimos las la serie en una lista de expresiones (términos de la SF)
s_truncada_list = [s_truncada.args[i] for i in range(len(s_truncada.args))]


sym.plot(*s_truncada_list) #El * sirve para desempaquetar la lista.

%% md prov-35
Podemos ver en la imagen, los diferentes armónicos con sus respectivas amplitudes y desfasajes que componen a la señal periódica. Identidicar qué número de armónico se corresponde con cada una de las curvas.


Notar que este desarrollo es equivalente al ejercicio $3a$ de gabinete (TP5) para $T=4$ y $\tau = 2$. Comparar los resultados.

%% md enu-01
## Ejercicio 1

Resolver el ejercicio $3e$ del trabajo práctico de gabinete utilizando ambas metodologías vistas en el ejercicio 1, por definición y utilizando la función `sym.fourier_series()`. Graficar los espectros y la señal a través de la serie truncando en 20 componentes
$$x(t)=
\begin{cases}
t, & 0 \leq t<1, \\
2-t, & 1 \leq t<2,
\end{cases}$$

siendo $T=2.$

%% md prov-36
Analizar los resultados respecto a la paridad de la señal y dejarlos por escrito en el notebook.

%% code act-01


%% md prov-37
# 2. Serie exponencial compleja de Fourier.

La serie exponencial compleja se expresa como:

$$f(t)=\sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}$$

Donde calcularemos:

$$c_0=\frac{1}{T}\int_{T} f(t)dt$$

$$c_n = \frac{1}{T}\int_{T} f(t) e^{-jn\omega_0 t}dt \ \ \text{ para } \ \ n \neq 0 $$


Analizaremos cómo obtener la serie exponencial de Fourier de la señal presentada en el ejercicio $4a$ del práctico de gabinete.

El período central de la señal se defie como:

$$x(t)=
\begin{cases}
1, & -\frac{1}{4} \lt t\leq \frac{1}{4}, \\
0, &   t\lt -\frac{1}{4} \ \lor  \ t\gt \frac{1}{4}
\end{cases}$$

$$T=1$$
No existe función en `SymPy` para calcular la serie exponencial  directamente, se debe realizar de manera analítica. Para esto debemos tener en cuenta que la forma de expresar la exponencial compleja $e^i$  en sympy es `sym.exp(sym.I)`

%% code prov-38
sym.exp(sym.I)

%% md prov-39
Primero obtendremos la expresión de la señal para un período:

%% code prov-40
# Definimos el periodo fundamental y la frecuencia de la señal
T0  = 1
w0 = 2*sym.pi/T0 # sym.pi representa al número pi de manera simbólica

# Creamos la función
f = sym.Piecewise(
    (0, (t < -0.25) | (t > 0.25)),
    (1, (t >= -0.25) & (t <= 0.25))
)

f

%% md prov-41
Graficamos el período que utilizaremos de la señal.

%% code prov-42
sym.plot(f, (t, -0.5, 0.5))

%% md prov-43
Calcularemos ahora los coeficientes $C_n=\frac{1}{T}\int_{T} x(t) e^{-inw_0t} dt$

%% code prov-44
# Primero definimos el índice discreto n como variable simbólica
n = sym.symbols('n', integer=True)

# Luego definimos una variable que represente el argumento de la integral
arg_integral  = f * sym.exp(-sym.I * n * w0 * t)

# Ahora calculamos la integral en un período
integral = sym.integrate(arg_integral,(t,-0.5, -0.5+T0))

# Por último multiplicamos por (1/T0)
cn = (1/T0) * integral
cn

%% md prov-45
Vemos que quedó expresado en forma compleja. Convirtiendo las exponenciales a suma de senos y cosenos mediante la identidad de Euler podemos encontrar una expresión más simple.

%% code prov-46
cn=cn.rewrite(sym.cos).simplify()

%% md prov-47
Hacer esto no es necesario pero puede ser útil para visualizar las expresiones de manera más sencilla.


La serie queda expresada como:

$$f(t)= 0.5 + \sum_{n=-\infty}^{-1} \frac{1}{2} \operatorname{sinc}(n \frac{\pi}{2}) e^{jn 2\pi t} + \sum_{n=1}^{\infty} \frac{1}{2} \operatorname{sinc}(n \frac{\pi}{2}) e^{j n 2\pi t}$$



Ahora encontraremos el valor de algunos de los coeficientes $c_n$ usando la función :

%% code prov-48
N=10
# Presentamos resultados por pantalla
for k in range(-N, N): #usamos k porque n ya lo estamos usando como variable simbólica
  #display(Math(f'C_{{{k}}}: {cn.subs(n, k).evalf()}'))
  print(f"c_{k}: ", cn.subs(n, k).evalf())

%% md prov-49
Graficaremos ahora el espectro de amplitud, para esto calcularemos el módulo de  los coeficientes calculados en el paso anterior y lo guardaremos en la lista que llamaremos `amp`

%% code prov-50
amp = []
k = range(-N, N) #usamos k porque n ya lo estamos usando como variable simbólica
for i in k:
  amp.append(abs(cn.subs(n, i).evalf()))


plt.stem(k, amp)
_ = plt.xticks(np.arange(np.min(k), np.max(k)+1, 1))

%% md prov-51
Espectro de fase:

%% code prov-52
fase = []
k = range(-N, N)


for i in k:
    fase.append(cmath.phase(cn.subs(n, i).evalf()))


plt.stem(k, fase)
_=plt.xticks(np.arange(np.min(k), np.max(k)+1, 1)) #para mejorar la visualización

%% md enu-02
## Ejercicio 2

Resolver el ejercicio $4b$ del práctico de gabinete. Graficar los espectros y la señal a partir de la serie truncando en 30 términos.

%% md prov-53
# 3. Transformada de Fourier de tiempo continuo

%% md prov-54

La Transformada de Fourier es una herramienta que nos permite representar señales en el dominio de la frecuencia. Esta representación es especialmente útil porque muchas veces es más sencillo analizar y manipular señales en el dominio de la frecuencia que en el dominio del tiempo. La Transformada de Fourier es aplicable tanto a señales continuas como discretas, aunque la formulación matemática varía ligeramente.

La Transformada de Fourier de una señal $ x(t) $ se denota por $ X(f) $ o $ X(j\omega) $, donde $ f $ es la frecuencia en Hertz y $ \omega=2\pi f $ es la frecuencia angular en $rad/s$.

La definición matemática de la Transformada de Fourier es:

$
X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt
$

y su transformada inversa es:

$
x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(j\omega) e^{j\omega t} df
$

A continuación, veremos cómo calcular la Transformada de Fourier utilizando Sympy y algunas de sus propiedades más importantes.


%% md prov-55


Vamos a calcular la Transformada de Fourier de un pulso rectangular definido como:

$x(t) =
\begin{cases}
0 & \text{si } t < -0.5 \\
1 & \text{si } -0.5 \leq t \leq 0.5 \\
0 & \text{si } t > 0.5
\end{cases}
$

%% code prov-56
# Definimos la variables simbólicas
t, f = sym.symbols('t f') # usaremos frecuencia en Hertz ya que la implementación en sympy usa f

# Definimos la señal pulso rectangular
pulso_rectangular = sym.Piecewise(
    (1, (t >= -0.5) & (t <= 0.5)),
    (0, (t < -0.5) | (t > 0.5))
)


sym.plot(pulso_rectangular, (t, -5,5) ,title='Pulso rectangular de 1 segundo de duración', ylabel='Amplitud', xlabel='tiempo [segundos]')

%% md prov-57
Usaremos frecuencia en Hertz ya que es la que utiliza la implementación de la transformada en sympy.



Para calcular la transformada de Fourier utilizaremos la función integrada en `SymPy` llamada `fourier_transform` la cual recibe como argumentos:
1.  la señal a la cual le queremos calcular la transformada de Fourier
2. la variable simbólica que se usa para el tiempo
3. la variable simbólica que usaremos para la frecuencia en Hertz

%% code prov-58
pulso_rectangular_transformado = sym.fourier_transform(pulso_rectangular, t, f)

%% md prov-59
Para graficar el espectro de amplitud usaremos la función de sympy `sym.Abs` que calcula el módulo de la transformada

%% code prov-60
_ = sym.plot(sym.Abs(pulso_rectangular_transformado), title='Espectro de Amplitud', ylabel='Amplitud', xlabel='f [Hertz]')

%% md prov-61
Para graficar el espectro de fase usaremos la función de sympy `sym.arg`, la cual nos devuelve la fase de la transformadal

%% code prov-62
_ = sym.plot(sym.arg(pulso_rectangular_transformado), title='Espectro de fase', ylabel='Fase', xlabel='f [Hertz]')

%% md enu-03
## Ejercicio 3

%% md prov-63
a. Calcular el espectro de fase y amplitud de la misma señal del ejemplo anterior (pulso) con un retraso de 0.2 segundos.

b. Compare los espectros de amplitud y fase obtenidos con los del ejercicio anterior.

c. ¿Cómo explica las diferencias?

%% code act-02


%% md enu-04
## Ejercicio 4

%% md prov-64
Grafique los espectros de amplitud y fase de la rampa finita que vale `t` entre `-0.7` y `0.7` y vale 0 en cualquier otro valor de t.

%% code prov-65
import sympy as sym
# Definimos la variables simbólicas
t, f = sym.symbols('t f') # usaremos frecuencia en Hertz ya que es la implementación en sympy

# Definimos rectangular signal
rampa = sym.Piecewise(
    (t, (t >= -0.7) & (t <= 0.7)),
    (0, (t < -0.7) | (t > 0.7))
)
_ = sym.plot(rampa, (t, -1.2, 1.2) , title='rampa finita', xlabel='tiempo [segundos]')

%% md prov-66
# 4. Respuesta en frecuencia.

%% md prov-67
Analizaremos cómo se comporta un circuito serie pasivo compuesto por un resistor de valor $R$ y una inductancia  de valor $L$. La intensión es exitar el circuito con una señal sinusoidal y encontrar la respuesta del mismo en régimen permanente. Para esto obtendremos la función de transferencia del sistema y a partir de la misma obtendremos la respuesta en frecuencia, la cual utilizaremos para calcular la salida.

%% md hdr-02
![image.png](data:image/png;base64,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)

%% md prov-68


Exitaremos el circuito con tensión en los bornes de la izquierda con un generador que produce la señal $V_{in}(t)$ y la salida será la tensión medida a través de la resistencia y la llamaremos $V_{out}(t)$, aplicamos la Ley de de las tensiones de  Kirchhoff para encontrar la ecuación diferencial que caracteriza al sistema.

1. **Ecuación Diferencial:**
   Aplicando ley de Kirchhoff de las tensiones al circuito obtenemos:
   $$ v_{in}(t) = v_R(t) + v_L(t) $$

Utilizando la ley de Ohm en la resistencia y la relación Volt-Ampere en el inductor:

   $$ v_{in}(t) = R \cdot i(t) + L \cdot \frac{di(t)}{dt} $$

2. **Transformada de Laplace:**
   Tomando la transformada de Laplace a ambos lados de la ecuación considerando condiciones iniciales nulas,
   $$ V_{in}(s) = R \cdot I(s) + sL \cdot I(s) $$

3. **Función de Transferencia:**
   La función de transferencia, $H(s)$, es la relación entre la salida y la entrada en el dominio s,
   $$ H(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{R \cdot I(s)}{V_{in}(s)} = \frac{R}{R + sL} $$

Para que quede explícito el valor del polo dividimos numerador y denominador por $L$

   $$H(s) = \frac{\frac{R}{L}}{s + \frac{R}{L}}$$

Vemos que la función de transferencia tiene un polo en $\alpha = - \frac{R}{L}$. Como el valor de la inductancia L y la resistencia R siempre son reales y positiva, polo queda ubicado  siempre en el semiplano izquierdo del plano `s`, por lo que es un sistema estable.


4.**Respuesta en frecuencia**

La respuesta en frecuencia es la transformada de Fourier de la respuesta al impulso. La función de transferencia es la transformada de Laplace de la respuesta al impulso. Sabiendo que la Transformada de Fourier es el caso particular de la transformada de Laplace evauada en $s=j\omega$ podemos obtener la respuesta en frecuencia como:

   $$ H(j\omega) = \frac{R}{R + j\omega L} $$


%% md prov-69
## Gráficas de la salida en función de los valores de los elementos del circuito con Python

A continuación vamos a crear una función que grafica de manera interactiva la salida en función de $L$ $R$ y la frecuencia de la sinusoidal de entrada.

Crearemos una función llamada `plot_signals` para visualizar la relación entre la tensión de entrada y la tensión de salida en un circuito $RL$ serie en el dominio del tiempo. La entrada se ha considerado como una señal sinusoidal y, mediante el uso de la función de transferencia, se calcula la salida correspondiente. A continuación se explica cómo se hace esto paso a paso:


 Expresaremos la señal de entrada matemáticamente:
   $$ V_{in}(t) = \sin(\omega_0 t) $$

Para calcular la salida utilizamos la respuesta en frecuencia según lo visto en clase para régimen permanente:

$$ V_{out}(t) = \left| H(j\omega_0) \right| \cdot \sin\left(\omega_0 t + \text{Arg}\{H(j\omega_0)\} \right) $$




%% code prov-70
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

def plot_signals(R=1000, L=0.1, freq=100): #frecuencia en radianes
    t = np.linspace(0, 65 * (2*np.pi/freq), 10000) #graficamos siempre 5 periodos
    Vin = np.sin(freq * t) # la entrada es un seno

    # Calculamos la función de transferencia H(jω)
    H = R / (R + L*1j*freq)

    # Calculamos Vout usando la fórmula
    Vout = np.abs(H) * np.sin(freq * t + np.angle(H)) #la salida es un seno escalado y desplazado por H(s)

    plt.figure(figsize=(10, 4))
    plt.plot(t, Vin, label='$V_{in}(t)$')
    plt.plot(t, Vout, label='$V_{out}(t)$')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Tensión (V)')
    plt.legend()
    plt.grid(True)
    plt.title('Tensión de Entrada y Salida vs Tiempo')
    plt.xlim(0,0.1)
    plt.show()

_ = interact(plot_signals,freq=(100, 4000) , L=(1, 100, 1.), R=(5, 2000, 10))


%% code prov-71
def plot_frequency_response(R=500, L=0.9):
    freq = np.linspace(0, 4000, 400)
    H = R / (R + L*1j*freq)
    magnitude = np.abs(H)
    plt.figure(figsize=(10, 4))
    plt.plot(freq, magnitude)
    plt.ylim(0, 1.1)
    plt.xlim(0, 4000)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.title('Magnitud de respuesta en Frecuencia')
    plt.grid(True)
    plt.show()

_ = interact(plot_frequency_response, R=(500, 2000, 10),L=(0.1, 9, 0.01))

