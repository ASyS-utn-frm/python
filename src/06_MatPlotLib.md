---
prefix: 06_MatPlotLib
source: 06_MatPlotLib.ipynb
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
        <!--<p><em>Profesor Mg. Ing. Javier Velez</em></p>-->
    </div>
</center>

%% md hdr-02
# Introducción a Matplotlib

Matplotlib es una biblioteca de Python utilizada para crear visualizaciones de datos. Es especialmente útil para graficar datos y señales en el análisis de señales y sistemas. En este tutorial, aprenderemos los conceptos básicos de Matplotlib y cómo aplicarlos para visualizar datos de manera efectiva.

## 1. Importando Matplotlib

Para utilizar Matplotlib, primero debemos importarlo. Es una convención común importarlo con el alias plt.

%% code prov-01
import matplotlib.pyplot as plt

%% md prov-02
También importaremos NumPy para crear arreglos que representen nuestras señales.

%% code prov-03
import numpy as np

%% md hdr-03
## 2. Creando Gráficos Simples

### 2.1. Gráfico de una Función Continua

Los gráficos de funciones continuas son una de las formas más comunes de visualizar datos en el análisis de señales. Este tipo de gráfico es ideal para representar funciones matemáticas y señales continuas en el tiempo.

%% code prov-04
# Crear datos de ejemplo
x = np.linspace(0, 10, 100)  # Vector de tiempo con 100 puntos entre 0 y 10
y = np.sin(x)  # Señal senoidal

# Crear un gráfico de funciones continuas
plt.plot(x, y)
plt.title("Gráfico de Función Continua")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()


%% md prov-05
En este ejemplo:

- `x` es un vector de tiempo creado usando `np.linspace` que genera 100 puntos equidistantes entre 0 y 10.

- `y` es una señal senoidal calculada como `np.sin(x)`.
`plt.plot(x, y)` crea un gráfico de línea de `y` en función de `x`.

- `plt.title`, `plt.xlabel`, y `plt.ylabel` añaden el título y las etiquetas de los ejes al gráfico.

- `plt.grid(True)` añade una cuadrícula al gráfico.

**Nota sobre la Interpolación de Señales Discreta**

Aunque la función que graficamos parece continua, lo que realmente estamos haciendo es utilizar una señal discreta interpolada. En el ejemplo anterior, `x` tiene 100 puntos discretos entre 0 y 10, y `y` calcula los valores de la función senoidal en esos puntos discretos. `Matplotlib` conecta estos puntos con líneas para dar la apariencia de una señal continua.

#### 2.2.1 Frecuencia de Muestreo y Construcción de Señales en Python

**Frecuencia de Muestreo**

La frecuencia de muestreo, denotada como `fs`, es el número de muestras por segundo que se toman de una señal continua para convertirla en una señal discreta. Se mide en Hertz (Hz).

Una frecuencia de muestreo adecuada es crucial para capturar con precisión la señal original. Según el Teorema de Nyquist, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta presente en la señal para evitar el aliasing. Esto lo explicaremos en profundidad durante el curso por lo que no te debe preocupar por ahora.

**Construcción de Señales de Determinadas Duraciones**

Para construir una señal de una duración específica utilizando una frecuencia de muestreo determinada, primero creamos un vector de tiempo que representa los instantes de tiempo en los que se toman las muestras.

**Ejemplo de Construcción de una Señal**

Supongamos que queremos generar una señal de 1 segundo de duración con una frecuencia de muestreo de 500 Hz.

%% code prov-06
# Definir parámetros
duración = 1  # Duración en segundos
fs = 500  # Frecuencia de muestreo en Hz

# Crear el vector de tiempo
t = np.linspace(0, duración, int(fs * duración))


%% md prov-07
- `duración = 1`: Especifica que la señal durará 1 segundo.
- `fs = 500`: Especifica que se tomarán 500 muestras por segundo.

La función `np.linspace` se utiliza para generar un array de valores equidistantes entre dos puntos. En este caso, se generan valores de tiempo desde 0 hasta duración (1 segundo), con un total de int(fs * duración) muestras.

- np.linspace(0, duración, int(fs * duración)):

  - `0`: Punto de inicio del intervalo de tiempo (incluido).
  - `duración`: Punto final del intervalo de tiempo (excluido).
  - `int(fs * duración)`: la función `int()` devuelve un valor entero ya que la función no soporta un número floar para este argumento. `fs*duracion` nos da la cantidad total de muestras que va a tener la señal basado en la duración en segundos de la señal y la fecuencia de muestreo en Hz


**Aplicación: Generación de una Señal Sinusoidal**

Usando el vector de tiempo `t`, podemos generar una señal sinusoidal:

%% code prov-08
frecuencia = 5  # Frecuencia de la señal en Hz

# Generar la señal sinusoidal
senal_sinusoidal = np.sin(2 * np.pi * frecuencia * t)

# Graficar la señal sinusoidal
plt.plot(t, senal_sinusoidal)
plt.title("Señal Sinusoidal")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)


%% md prov-09
Vemos que hemos creado un gráfico que muestra una señal seno con una duración de 1 segundo donde se observa que entran 5 periodos de la señal (5 Hz).

**El Problema de una Frecuencia de Muestreo Baja**

Cuando la frecuencia de muestreo es baja, no se capturan adecuadamente los detalles de la señal original. Esto puede llevar a un fenómeno conocido como aliasing, donde las altas frecuencias de la señal se representan incorrectamente como frecuencias más bajas, distorsionando la señal.

%% code prov-10
# Frecuencia de muestreo baja
fs_baja = 8  # Frecuencia de muestreo baja en Hz (menos del doble de la frecuencia de la señal)

# Vector de tiempo con frecuencia de muestreo baja
t_baja = np.linspace(0, duración, int(fs_baja * duración))

# Generar la señal sinusoidal con frecuencia de muestreo baja
senal_sinusoidal_baja = np.sin(2 * np.pi * frecuencia * t_baja)

# Graficar la señal con frecuencia de muestreo baja
plt.plot(t_baja, senal_sinusoidal_baja, 'o-')  # Usamos 'o-' para mostrar los puntos de muestreo
plt.title("Señal Sinusoidal con Frecuencia de Muestreo Baja")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)




%% md hdr-04
### 2.2. Otras funciones incorporadas en NumPy

Grafiquemos ahora algunas funciones que vienen incorporadas dentro de numPy:

**Función Heaviside (`numpy.heaviside`) o escalón nuitario**

La función Heaviside es una función escalón que se utiliza frecuentemente en análisis de señales. En su forma más básica, esta función es 0 para valores negativos y 1 para cero y valores positivos. Aquí está la forma en que se utiliza en NumPy:

%% code prov-11
# Crear un rango de valores x
x = np.linspace(-10, 10, 100)  # Valores de -10 a 10 en 100 pasos

# Aplicar la función de Heaviside
# El segundo parámetro (h0) es el valor que la función toma cuando x = 0
h0 = 1
y = np.heaviside(x, h0)

# Graficar la función
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('H(x)')
plt.title('Función de Heaviside')
plt.grid()


%% md prov-12
Parámetros de numpy.heaviside:

- `x`: Array de entrada. Estos son los valores en los que quieres evaluar la función de Heaviside.

- `h0`: Valor de la función cuando `x` es exactamente 0. Puede ser 0, 0.5, 1, etc.

**Función por Tramos (`numpy.piecewise`)**

La función `numpy.piecewise` permite definir funciones que cambian su comportamiento en diferentes intervalos. Es muy útil para crear funciones más complejas.

%% code prov-13
# Crear un rango de valores x
x = np.linspace(-10, 10, 100)

# Definir la función por tramos
# la variable y será 0 cuando x < 0 y valdrá 1 cuando x >= 0

condlist = [x < -1,  (x >= -1) & (x < 1.3), x >= 1.3]
funclist = [0.2, -0.5, 0.3]
y = np.piecewise(x, condlist, funclist)

# Graficar la función
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función por Tramos')
plt.grid()
plt.show()


%% md prov-14
Parámetros de numpy.piecewise:

- `x`: Array de entrada.

- `condlist`: Lista de condiciones. Cada condición es una expresión booleana que define un intervalo.

- `funclist`: Lista de valores o funciones correspondientes a cada condición.



%% md hdr-05
**Librería Scipy**

Otra librería que utilizaremos durante el curso sera `SciPy`.

 `SciPy` es una biblioteca fundamental para la computación científica en Python. Proporciona muchas funciones adicionales a las de NumPy, especialmente útiles para el análisis de señales, optimización, álgebra lineal, integración, y más. En este tutorial, aprenderemos a utilizar SciPy para crear otros tipos de señales. En particular usaremos los modulos `signal` que contiene `SciPy`.


%% code prov-15
import scipy.signal as signal

%% md prov-16
**Señal cuadrada**

Vamos a crear una señal cuadrada, que es una onda periódica que alterna entre dos niveles de amplitud. Es muy útil para representar señales digitales.

%% code prov-17
# Crear un vector de tiempo
duracion = 1
fs = 500
t = np.linspace(0, 1, int(fs*duracion))  # 500 puntos en 1 segundo

# Crear una señal cuadrada con una frecuencia de 5 Hz
frecuencia = 5  # Frecuencia en Hz
señal_cuadrada = signal.square(2 * np.pi * frecuencia * t)

# Graficar la señal cuadrada
plt.plot(t, señal_cuadrada)
plt.title("Señal Cuadrada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()


%% md prov-18
Explicación:

- `np.linspace(0, duracion, int(fs*duracion)`: Crea un vector de tiempo `t` que va de 0 a 1 segundo, dividido en 500 puntos.

- `signal.square(2 * np.pi * frecuencia * t)`: Genera una señal cuadrada con una frecuencia de 5 Hz.

- `2 * np.pi * frecuencia * t` : Calcula los puntos en el tiempo multiplicando por 2π para convertir a radianes.

- `signal.square`: Genera la señal cuadrada.

- `plt.plot(t, señal_cuadrada)`: Grafica la señal cuadrada en función del tiempo `t`.

**Señal Triangular/Diente de sierra**

Podemos crear una señal triangular o una señal diente de sierra utilizando la función `signal.sawtooth` de SciPy. Este tipo de señal es una forma de onda periódica que puede subir linealmente y luego bajar bruscamente, o viceversa. La función permite un parámetro opcional llamado `width` que especifica el punto dentro del período en el que la señal alcanza su valor máximo. Debe estar en el rango [0, 1].

Veamos 3 ejemplos:

`width` $=1.0$

%% code prov-19
frecuencia = 5  # Frecuencia en Hz
duración = 1  # Duración en segundos
fs = 500  # Frecuencia de muestreo en Hz

# Vector de tiempo
t = np.linspace(0, duración, int(fs * duración), endpoint=False)

senal_diente_sierra_1 = signal.sawtooth(2 * np.pi * frecuencia * t, width=1.0)
plt.plot(t, senal_diente_sierra_1)
plt.title("Señal Diente de Sierra con width=1.0 (Sube linealmente y cae bruscamente)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)


%% md prov-20
`width` $=0.5$

%% code prov-21
senal_diente_sierra_05 = signal.sawtooth(2 * np.pi * frecuencia * t, width=0.5)
plt.plot(t, senal_diente_sierra_05)
plt.title("Señal Diente de Sierra con width=0.5 (Onda Triangular)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

%% md prov-22
`width` $=0.0$

%% code prov-23
senal_diente_sierra_0 = signal.sawtooth(2 * np.pi * frecuencia * t, width=0.0)

plt.plot(t, senal_diente_sierra_0)
plt.title("Señal Diente de Sierra con width=0.0 (Sube bruscamente y baja linealmente)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

%% md hdr-06
### 2.2 Agregar un Nivel de Continua a una Señal

En el análisis de señales y sistemas, a veces es útil agregar un nivel de continua (también conocido como componente DC) a una señal. La componente DC es un desplazamiento vertical que afecta a toda la señal de manera uniforme. En términos simples, agregar una componente DC significa elevar o bajar toda la señal por un valor constante.

¿Por qué agregar una componente DC?

- Desplazamiento de la Señal: Para asegurar que la señal esté siempre por encima (o por debajo) de un cierto nivel.

- Propósito de Ajuste: En sistemas electrónicos, se puede necesitar para que la señal se ajuste dentro del rango de operación de un dispositivo.

- Análisis y Procesamiento: Puede ser útil para análisis específico donde se necesita ajustar el promedio de la señal a un valor diferente de cero.

**Cómo Agregar una Componente DC**

Para agregar una componente DC a una señal, simplemente sumamos un valor constante a cada muestra de la señal.

%% code prov-24
# Crear un vector de tiempo
t = np.linspace(0, 1, 500)  # 500 puntos en 1 segundo

# Crear una señal cuadrada con una frecuencia de 5 Hz
frecuencia = 5  # Frecuencia en Hz
valor_dc = 2  # Valor de la componente DC

señal_cuadrada_con_dc = signal.square(2 * np.pi * frecuencia * t) + valor_dc

# Graficar la señal cuadrada
plt.plot(t, señal_cuadrada_con_dc)
plt.title("Señal Cuadrada con componente de DC")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

%% md prov-25
### 2.3 Desplazamiento en el tiempo de una Señal

El desplazamiento en el tiempo de una señal significa mover la señal hacia la derecha o hacia la izquierda en el eje del tiempo. Esto se puede lograr sumando (para adelantar) o restando (para retrasar) un valor constante al vector de tiempo antes de generar la señal.

Grafiquemos primero una señal sinusoidal de ejemplo sin desplazar y luego la desplazaremos.

%% code prov-26

# Parámetros de la señal
frecuencia = 5  # Frecuencia en Hz
duración = 1  # Duración en segundos
fs = 500  # Frecuencia de muestreo en Hz

# Vector de tiempo
t = np.linspace(0, duración, int(fs * duración), endpoint=False)

# Generar señal sinusoidal original
senal_sinusoidal = np.sin(2 * np.pi * frecuencia * t)

# Graficar señal sinusoidal original

plt.plot(t, senal_sinusoidal)
plt.title("Señal Sinusoidal Original")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

%% md prov-27
Ahora generaremos y graficaremos la señal sinusoidal desplazada.

%% code prov-28
# Desplazamiento en segundos
desplazamiento = 0.1  # Desplazamiento de 100 ms

# Generar señal sinusoidal desplazada en el tiempo
t_desplazado = t + desplazamiento
senal_sinusoidal_desplazada = np.sin(2 * np.pi * frecuencia * t_desplazado)

# Graficar señal sinusoidal desplazada

plt.plot(t, senal_sinusoidal_desplazada)
plt.title("Señal Sinusoidal Desplazada en el Tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Mostrar el gráfico
plt.show()


%% md prov-29
Vemos que para desplazarla señal debemos operar sobre el vector de tiempo (variable independiente) sumando o restando el valor de desplazamiento para obtener t_desplazado.

%% md prov-30
## 3. Personalización de Gráficos

### 3.1. Títulos y Etiquetas

Puedes agregar títulos y etiquetas a los ejes para hacer el gráfico más informativo.

%% code prov-31
# Crear datos de ejemplo
y2 = np.cos(x)  # Señal cosenoidal

# Crear un gráfico de funciones continuas con títulos y etiquetas
plt.plot(x, y2)
plt.title("Gráfico de Coseno")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

%% md prov-32
En este ejemplo:

- `y2` es una señal cosenoidal calculada como `np.cos(x)`.

- `plt.title("Gráfico de Coseno")` añade un título al gráfico.

- `plt.xlabel("Tiempo [s]")` y `plt.ylabel("Amplitud")` añaden etiquetas a los ejes `X` e `Y`, respectivamente.

### 3.2. Leyendas
Las leyendas ayudan a identificar diferentes series de datos en el mismo gráfico.

%% code prov-33
# Crear datos de ejemplo
y1 = np.sin(x)
y2 = np.cos(x)

# Crear un gráfico de funciones continuas con dos series de datos y una leyenda
plt.plot(x, y1, label="Seno")
plt.plot(x, y2, label="Coseno")
plt.title("Gráfico con Leyenda")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()


%% md prov-34
En este ejemplo:

- `plt.legend()` añade una leyenda que identifica las series "Seno" y "Coseno".


### 3.3 Formato del gráfico

La función `plt.figure()` de matplotlib se utiliza para crear una nueva figura, que es una ventana o marco donde se dibujarán los gráficos. El argumento `figsize` se utiliza para definir el tamaño de la figura en pulgadas.

**Sintaxis**
~~~python
plt.figure(figsize=(width, height))
~~~

Parámetros:
- `figsize`: tupla de dos elementos (opcional), define el tamaño de la figura en pulgadas.
- `width`: Ancho de la figura.
- `height`: Altura de la figura




%% code prov-35

# Parámetros de la señal
frecuencia = 5  # Frecuencia en Hz
duración = 1  # Duración en segundos
fs = 500  # Frecuencia de muestreo en Hz

# Vector de tiempo
t = np.linspace(0, duración, int(fs * duración), endpoint=False)

# Generar señal sinusoidal
senal_sinusoidal = np.sin(2 * np.pi * frecuencia * t)

# Crear una nueva figura con tamaño especificado
plt.figure(figsize=(10, 5))

# Graficar señal sinusoidal
plt.plot(t, senal_sinusoidal)
plt.title("Señal Sinusoidal")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Mostrar el gráfico
plt.show()


%% md prov-36
### 4. Subgráficos

Los subgráficos permiten visualizar múltiples gráficos en una sola figura. Esto es útil cuando queremos comparar diferentes señales o funciones.

%% code prov-37
# Crear datos de ejemplo
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura con dos subgráficos
fig, axs = plt.subplots(2, 1)

axs[0].plot(x, y1)
axs[0].set_title("Seno")
axs[0].set_xlabel("Tiempo [s]")
axs[0].set_ylabel("Amplitud")
axs[0].grid(True)

axs[1].plot(x, y2)
axs[1].set_title("Coseno")
axs[1].set_xlabel("Tiempo [s]")
axs[1].set_ylabel("Amplitud")
axs[1].grid(True)

plt.tight_layout()
plt.show()


%% md prov-38
En este ejemplo:

- `fig, axs = plt.subplots(2, 1)` crea una figura con dos subgráficos (2 filas, 1 columna).

- `axs[0].plot(x, y1)` y `axs[1].plot(x, y2)` grafican `y1` y `y2` en los subgráficos correspondientes.

- `axs[i].set_title`, `axs[i].set_xlabel`, y `axs[i].set_ylabel` añaden títulos y etiquetas a cada subgráfico.

- `plt.tight_layout()` ajusta el diseño para evitar solapamientos.

## 5. Gráficos de Señales Discretas

Una señal discreta es una secuencia de valores definidos en puntos específicos del tiempo. A diferencia de las señales continuas, que están definidas para todos los instantes de tiempo dentro de un intervalo, las señales discretas están definidas solo en instantes de tiempo discretos.

En términos simples, una señal discreta es el resultado de muestrear una señal continua en intervalos de tiempo regulares. Este proceso de muestreo convierte la señal continua en una serie de valores discretos, que pueden ser procesados y analizados digitalmente.

**Características de las Señales Discretas**

- Muestreo: Proceso de convertir una señal continua en una señal discreta al tomar muestras en intervalos de tiempo regulares.

- Espacio de Tiempo Discreto: Los valores de la señal están definidos en puntos discretos del tiempo, normalmente enteros.

- Representación Digital: Las señales discretas se pueden almacenar y procesar utilizando sistemas digitales, como computadoras y microcontroladores.

Para visualizar señales discretas, podemos usar la función `plt.stem` de Matplotlib, que es ideal para mostrar claramente los valores de la función en puntos específicos.

### 5.1. Creación de una Señal Discreta

Vamos a crear una señal discreta utilizando la función `sin` de NumPy y graficarla con `plt.stem`.



%% code prov-39

# Crear datos de ejemplo para una señal discreta
n = np.arange(0, 10, 1)  # Números enteros de 0 a 9
señal_discreta = np.sin(2 * np.pi * n / 10)  # Señal discreta

# Crear un gráfico de la señal discreta
plt.stem(n, señal_discreta)
plt.title("Señal Discreta")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()


%% md prov-40
En este ejemplo:

- `n` es un vector de números enteros de 0 a 9.

- `señal_discreta` es una señal discreta calculada como `np.sin(2 * np.pi * n / 10)`, que representa una señal sinusoidal muestreada.


La función `plt.stem(n, señal_discreta)` crea un gráfico de tallo para la señal discreta.

### 5.2. Ejemplo con Secuencia Arbitraria

Ahora, vamos a crear una señal discreta a partir de una secuencia arbitraria hardcodeada y graficarla



%% code prov-41
import numpy as np
import matplotlib.pyplot as plt

# Crear una secuencia arbitraria
n = np.arange(-10, 10, 1)  # Números enteros de 0 a 9
secuencia_arbitraria = [3, -1, 4, 0, 2, 5, -2, 1, -3, 4, 3, -1, 4, 0, 2, 5, -2, 1, -3, 4]  # Secuencia arbitraria

# Crear un gráfico de la secuencia arbitraria
plt.stem(n, secuencia_arbitraria, use_line_collection=True)

# Configurar las etiquetas del eje x para mostrar todos los números del vector de tiempo como enteros
plt.xticks(n) # Probar como se ve la gráfica cuando se comenta esta línea


plt.title("Secuencia Arbitraria")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()


%% md prov-42
## 6. Graficar Puntos en el Plano

La función `scatter` de `matplotlib` se utiliza para crear gráficos de dispersión, donde los puntos se representan en un plano 2D. Esta función es muy útil para graficar datos bidimensionales, como los números complejos. Los argumentos principales que se utilizan con scatter son:

- `x`: Coordenadas en el eje x (parte real en el caso de números complejos).
- `y`: Coordenadas en el eje y (parte imaginaria en el caso de números complejos).
`color`: Color de los puntos (opcional).

Aquí tienes un ejemplo básico de cómo funciona:


%% code prov-43
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4]
y = [2, 3, 4, 5]

# Crear gráfico de dispersión
plt.scatter(x, y, color='blue')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5) # función que agrega una grilla de color gris y linea discontinua
# Mostrar gráfico
plt.show()


%% md prov-44
Vamos a aplicar esta función para graficar números complejos en el plano complejo.

%% code prov-45

# Crear un conjunto de números complejos
numeros_complejos = np.array([1+2j, 2+3j, -1-1j, -2+2j, 3-3j])

# Obtener las partes reales e imaginarias
partes_reales = numeros_complejos.real
partes_imaginarias = numeros_complejos.imag

# Graficar los puntos en el plano complejo
plt.scatter(partes_reales, partes_imaginarias, color='blue')

# Etiquetas y título
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Números Complejos en el Plano Complejo')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.show()


%% md prov-46
----
Con esto llegamos al final de este tutorial! Recuerda que los temas que desarrollamos en los tutoriales de la cátedra son tratados de manera básica y contienen solo lo necesario para poder presentar de forma didáctica los contenidos de la asignatura. Entender Python en profundidad requiere un curso completo dedicado a ello.

En [este link](https://github.com/vinta/awesome-python)  encontrarás una extensa cantidad de librerías de python para trabajar prácticamente sobre cualquier temática que necesites.

En [este link](https://docs.python.org/es/3.9/) encontrarás la documentación completa de Python

En [este link](https://numpy.org/doc/2.0/user/index.html#user) encontrarás la documentación completa de NumPy.

En [este link](https://matplotlib.org/stable/index.html) encontrarás la documentación completa de MatPlotLib.

Cualquier comentario no dudes en consultar con los profesores de la cátedra.

