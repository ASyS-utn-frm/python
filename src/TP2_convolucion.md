---
prefix: TP2_convolucion
source: TP2_convolucion.ipynb
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
# Trabajo práctico n° 3. Convolución con Python

La convolución es una operación clave en el análisis de sistemas lineales e invariantes en el tiempo (LTI), que nos permite calcular la salida de un sistema cuando conocemos su respuesta al impulso y la señal de entrada.

En este notebook, exploraremos la convolución en el contexto de un sistema acústico. Un sistema acústico se refiere a un conjunto de elementos físicos y materiales que influyen en cómo el sonido se propaga y se comporta dentro de un entorno. En términos simples, es el ambiente o espacio donde el sonido viaja, interactúa con superficies, se refleja, se absorbe, se dispersa y, finalmente, llega a nuestros oídos.

Principales características de un sistema acústico:

- Medio de propagación: El sonido siempre necesita un medio para propagarse. Normalmente, este medio es el aire, pero también puede ser agua o sólidos, como las paredes de un edificio.

- Reflexión: Cuando una onda sonora choca contra una superficie, parte de la onda se refleja, generando efectos como ecos o reverberaciones. La cantidad y calidad de estas reflexiones dependen del tamaño, la forma y los materiales del entorno acústico.

- Absorción: Algunas superficies absorben parte de la energía sonora, transformándola en calor. Materiales como alfombras, cortinas y paneles acústicos suelen absorber frecuencias medias y altas, lo que reduce el eco y la reverberación en un espacio.

- Difracción y difusión: El sonido también puede difractarse (curvarse alrededor de objetos) o dispersarse en múltiples direcciones, dependiendo de las características físicas del entorno.

Imaginemos una sala de conciertos. El sonido que percibimos en este espacio depende de las dimensiones, las superficies (paredes, techo, suelo) y los materiales utilizados. Si las paredes son muy reflectantes y el espacio es amplio, habrá una mayor reverberación, lo que hará que el sonido se perciba como más "lleno". En contraste, si las paredes están cubiertas con materiales absorbentes, el sonido será más seco y claro debido a la reducción de las reflexiones.

En el contexto de la convolución, trabajamos con la respuesta al impulso de un sistema acústico. Esto se refiere a cómo reacciona un espacio (el sistema acústico) ante un sonido breve y fuerte, como el disparo de un arma o la explosión de un globo. La respuesta al impulso nos proporciona información sobre las características acústicas del lugar. Como los sistemas acústicos son generalmente aproximables como LTI (aunque no del todo, esta suposición es válida para la mayoría de las aplicaciones), podemos utilizar esta respuesta para predecir cómo el sistema respondería a otra señal, como una grabación de violín, simulando así cómo sonaría en ese ambiente.

%% md prov-02
Comenzaremos ejecutaremos la siguiente celda que importa las libríeras numpy y matplotlib.

%% code prov-03
import matplotlib.pyplot as plt
import numpy as np

%% md prov-04
Al ejecutar la siguiente celda, utilizaremos el comando de linux `gdown` para descargar una carpeta llamada "audios" desde Google Drive, donde los archivos fueron cargados previamente. Esta carpeta contiene dos archivos de audio en formato `.wav`: uno llamado `violín.wav` y otro llamado `disparo.wav`. El signo de exclamación previo a `gdown` es para ejecutar comandos de linux desde la celda.

La carpeta "audios" se descargará en la máquina virtual de Google donde se está ejecutando este notebook. Para visualizar o explorar los archivos descargados, puedes hacer clic en el icono de la carpeta ubicado cerca del centro de la barra lateral izquierda. Encontraremos los audios en la carpeta `/content/audios`. En sistemas Linux (como el que usa esta máquina virtual), el directorio / es conocido como el directorio raíz o root, y contiene todos los archivos y directorios del sistema.


%% code prov-05
#Descarga librerias y archivos externos necesarios del drive en asys_tp6/resources a content/resources
!gdown --folder https://drive.google.com/drive/folders/1EeJRHYMAYyxlgaCqXjr0SCXVWXbRT66s?usp=sharing

%% md prov-06
Podemos verificar que los audios están en el directorio "audios" ejecutando el comando de linux `ls` que devuelve una lista de archivos que contiene un directorio. Para ejecutar comandos de linux recordemos que simplemente debemos antecederlo con un signo de exclamación para que la celda lo ejecute.

%% code prov-07
!ls /content/audios

%% md prov-08

El archivo `impulsiva.wav` es la grabación de un disparo de arma de fuego realizado dentro de un espacio cerrado de gran tamaño, como un galpón. Esta señal no solo capta el sonido directo del disparo, sino también todas las reflexiones en las paredes y el techo, registrando cómo se comportan estos fenómenos en el lugar donde se ubicó el micrófono.

Dado que el disparo es un sonido de alta energía y corta duración, tiene una gran similitud con un impulso unitario, por lo que podemos considerarlo una buena aproximación. Por ello, la grabación de ese disparo en una posición determinada del galpón es una buena aproximación de la respuesta impulsiva $h(t)$ del sistema acústico.

En el siguiente código, utilizaremos la función `read`, que se encuentra en la librería `scipy.io.wavfile`, para cargar archivos `.wav` en memoria.

%% code prov-09
from scipy.io.wavfile import read

framerate, h = read('/content/audios/impulsiva.wav')  # Cambia la ruta a la correcta



%% md prov-10
La función `read` devuelve dos variables. La primera es la tasa o frecuencia de muestreo (en Hertz), conocida en inglés como `framerate`. Este valor nos indica cuántas muestras por segundo se tomaron al digitalizar la señal captada por el micrófono.

El mensaje que aparece al ejecutar la celda se debe a que el archivo `.wav` contiene información adicional que la función read está ignorando. Esta información extra no es relevante para nuestra tarea, por lo que podemos omitirla sin problemas.


%% code prov-11
print(framerate)

%% md prov-12
Es interesante notar que se tomaron $44.100$ muestras por segundo. Sabemos que la frecuencia máxima audible por el ser humano es aproximadamente de $20$ $kHz$. Si elegimos una frecuencia de muestreo que sea $2,205$ veces la frecuencia máxima, obtenemos una frecuencia de muestreo de $44.100$ $Hz$. De este modo, podemos ver que la discretización de la señal cumple con el teorema del muestreo (Unidad 6).

%% md prov-13
La segunda variable que devuelve la función `read` contiene las muestras de la señal capturada. En nuestro caso, hemos llamado `h` a esta señal, ya que representará nuestra respuesta impulsiva. La señal puede estar codificada de dos maneras:

1. Como un vector columna si fue grabada con un micrófono mono (un micrófono con un único sensor).

2. Como una matriz con dos columnas si la señal fue capturada con un micrófono estéreo (que tiene dos sensores). Cada columna corresponderá a lo que registró cada uno de los sensores del micrófono, comúnmente denominados "canal derecho" y "canal izquierdo".

Verificaremos con qué tipo de micrófono se grabó nuestra respuesta al impulso unitario.

%% code prov-14
# Verificar las dimensiones del arreglo 'h'
print("forma de los datos de audio:", h.shape)

%% md prov-15
Observamos que $h$ tiene $94.398$ filas (la cantidad de muestras) y 2 columnas, lo que indica que la grabación fue realizada con un micrófono estéreo. Si se tomaron $94.398$ muestras a una tasa de $44.100$ muestras por segundo, la duración de la señal es de $\frac{94398}{44100} = 2.14 $ segundos.

Para el trabajo que realizaremos en esta ocasión, no es necesario utilizar ambos canales. El sonido captado por uno de los sensores del micrófono será suficiente para aproximar la respuesta impulsiva del sistema. Por lo tanto, procederemos a quedarnos con solo un canal.

%% code prov-16
h = h[:, 0]
print(h.shape)

%% md prov-17
con la línea `h = h[:, 0]`  indicamos que queremos todas las filas (usando el signo `:`) de la columna $0$. Si no tienes claro cómo funciona, repasa el apartado de `slicing` del tutorial de `numpy`.


A continuación, importaremos un objeto$^1$ llamado `Audio` que nos permite reproducir audios directamente en un notebook de Jupyter. Solo necesitamos proporcionarle la señal que queremos reproducir y la frecuencia de muestreo con la que fue discretizada.

%% code prov-18
from IPython.display import Audio
Audio(h, rate=framerate)

%% md prov-19
$^1$: Un objeto en Python es una entidad que representa datos y las funciones que pueden operar sobre esos datos. Todo en Python es un objeto, desde números hasta funciones y estructuras de datos. Cada objeto tiene un tipo (por ejemplo, entero, cadena, lista) que determina qué operaciones se pueden realizar sobre él. Los objetos se crean a partir de clases, que son como plantillas para crear objetos con características específicas. La programación orientada a objetos es un tópico avanzado en python que omitiremos en este curso de Señales y Sistemas.

%% md prov-20
Ahora vamos a graficar la señal utilizando `matplotlib`. Primero, necesitamos crear el vector que representará el tiempo. Para ello, generamos un vector de la misma longitud que `h`, y dividimos cada valor por la frecuencia de muestreo para obtener un vector que indique a qué instante de tiempo corresponde cada muestra.


%% code prov-21
ts = np.arange(len(h)) / framerate
plt.plot(ts,h)
plt.xlabel('tiempo [segundos]')
_ = plt.ylabel('respuesta impulsiva $h(t)$')

%% md prov-22
hagamos zoom a la señal visualizando solamente las primeras 300 muestras:

%% code prov-23
plt.plot(ts[:300],h[:300])
plt.xlabel('tiempo [segundos]')
plt.ylabel('respuesta impulsiva $h(t)$')

%% md prov-24
A continuación, vamos a normalizar la señal. La normalización es un paso importante cuando trabajamos con la convolución de señales, ya que las señales originales pueden tener diferentes escalas de amplitud, lo que podría afectar el resultado final si no se ajustan correctamente. Además, la normalización garantiza que el resultado de la convolución se mantenga dentro del rango dinámico esperado, evitando posibles saturaciones digitales por overflow. Para normalizar, simplemente ajustamos los valores de la señal para que se encuentren dentro del rango $[-1,1]$.

%% code prov-25
h = h / np.max(np.abs(h))

%% md prov-26
Bien, ya hemos cargado y reproducido la señal que utilizaremos como respuesta impulsiva. Ahora necesitamos realizar el mismo proceso con la señal que emplearemos como entrada.

Nuestra señal de entrada es una grabación de un violín dentro de un estudio de grabación. El archivo de audio se llama `violin.wav`.

Es tarea del estudiante completar las siguientes celdas para cargar esta señal en una variable llamada `x`, ya que será la entrada de nuestro sistema.

Recuerda que el archivo de la señal de entrada se encuentra en `/content/audios`

%% code act-01
#completar

%% md prov-27
Verificar la frecuencia de muestreo

%% code act-02
#completar

%% md prov-28
Verificar si la señal es mono o estéreo.

%% code act-03
#completar

%% md prov-29
Quedarnos solo con el canal $0$ si es necesario

%% code act-04
#completar

%% md prov-30
Reproducir la señal con el objeto  `Audio`

%% code act-05
#completar

%% md prov-31
Graficar con matplotlib

%% code act-06
#completar

%% md prov-32
Hacer zoom de la señal entre las muestra 44000 y 44300

%% code act-07
#completar

%% md prov-33
Normalizar

%% code act-08
#completar

%% md prov-34
NOTA IMPORTANTE: siempre que estemos trabajando con la librería `numpy`estaremos trabajando con señales muestreadas almacenadas  vectores.  Estamos trabajando en el dominio de tiempo discreto, pero debido a que sabemos que las señales han sido muestreadas con una frecuencia de muestreo apropiada, por comodidad trabajaremos abstrayendónos de estar en tiempo discreto y podemos simular estar en tiempo continuo.


Ahora que ya tenemos cargadas las dos señales $h(t)$ y $x(t)$, es momento de realizar la convolución entre ellas para obtener la salida del sistema $y(t)$. Esto nos dará una aproximación de cómo sonaría el violín dentro del galpón,  teniendo en cuenta que la respuesta impulsiva es aproximada.  

Existen varios métodos para realizar la convolución, pero aquí analizaremos dos. El primero consiste en escribir una función que calcule la convolución entre las señales basándose en su definición:

$$y[n]=\sum_{k=-∞}^{∞} x[k]h[n-k]$$

Podemos implementar esta ecuación usando dos bucles `for` anidados, uno para recorrer `n` y otro para recorrer `k`. Si bien esta solución es funcional, no es recomendable, ya que no aprovecharíamos el hardware dedicado que posee nuestro procesador para realizar este tipo de cálculos.

La manera más eficiente en python es usando las librerías que fueron programadas en bajo nivel como `numpy` o `scipy`  que  aprovechan el hardware específico para realizar estos cálculos de manera eficiente. En nuestro caso, utilizaremos `scipy`.

A continuación, proporcionamos un código que implementa la convolución de manera manual a modo de ejemplo. Si lo ejecutas, notarás que el tiempo de cálculo es excesivo, llegando a superar la media hora.


%% code prov-35
def convolve_signals(x, h):
    """
    Realiza la convolución entre dos señales x y h usando bucles for.

    Parameters:
    x: array_like
        Primer vector de señal.
    h: array_like
        Segundo vector de señal.

    Returns:
    y: ndarray
        El resultado de la convolución entre x y h.
    """
    # Tamaños de las señales
    len_x = len(x)
    len_h = len(h)

    # El tamaño de la señal convolucionada es len_x + len_h - 1
    len_y = len_x + len_h - 1

    # Inicializamos el resultado de la convolución con ceros
    y = np.zeros(len_y)

    # Realizamos la convolución usando bucles for
    for n in range(len_y):
        # Calculamos cada elemento de y[n]
        for k in range(len_x):
            if n - k >= 0 and n - k < len_h:
                y[n] += x[k] * h[n - k]

    return y

r = convolve_signals(x, h)

%% md prov-36
Veremos ahora como calcular la convolución de manera eficiente utilizando el módulo `signal`de `scipy`.

%% md prov-37
Primero importaremos el módulo `signal` que se encuentra dentro de la librería `scipy`. Este módulo nos permitirá realizar la convolución ejecutando `signal.convolve`.

%% code prov-38
from scipy import signal

y =  signal.convolve(x, h, mode='full') #el modo full asegura que se calcule la convolución completa

%% md prov-39
Ahora deberán completar el código para reproducir el resultado de la convolución utilizando el objeto `Audio`

%% code act-09
#completar

%% md prov-40
Escuche atentamente y compare el resultado de la convolución con la grabación original del violín.

Ahora deberán graficar la señal resultante de la convolución. Recuerde que la convolución en general tiene como resultado una cantidad igual a $n_c = n_1 +n_2 -1$ donde $n_c$ es la cantidad de muestras del resultado de la convolución y $n_1$ y $n_2$ son la cantidad de muestras que tienen las respectivas señales que se están convolucionando. Esto implica que deben generar un vector de tiempo nuevo para graficar la señal.

%% code act-10
#completar

%% md prov-41
## <u>Ejercicio: </u>

Escriba un programa que permita calcular y gráficar la convolución solicitada en el  ejercicio 10.a de del trabajo práctico nº 6 de gabinete y comparar con el cuadro 1 de la página 11. En este caso graficar utilizando `plt.stem` ya que estamos tratando con señales intrínsecamente discretas y que no provienen de una señal continua muestreada. No olvides colocar las etiquetas correspondientes a cada eje.

%% code act-11
###COMPLETAR

%% md prov-42
## Convolución discreta en 2 dimensiones: Procesamiento de imágenes
Aunque hemos presentado la convolución en una dimensión, el concepto se puede extender a múltiples dimensiones.

La aplicación más común de la convolución discreta en dos dimensiones se encuentra en el procesamiento de imágenes digitales.

Una imagen digital en escala de grises (sin información de color) se representa como una matriz de $n \times m$ píxeles, donde cada posición de la matriz contiene un valor que indica el nivel de brillo o intensidad de gris de cada píxel.

Al trabajar con imágenes en escala de grises, es común utilizar 8 bits para representar el nivel de brillo de cada píxel, lo que permite una escala de 256 posibles valores, desde 0 (negro) hasta 255 (blanco).




### Ejemplo:

Vamos a importar el módulo `data` de la biblioteca `skimage`, que nos provee imágenes de muestra para trabajar.

%% code prov-43
from skimage import data
image = data.camera()
print(image)
print("shape: " ,image.shape)
plt.imshow(image, cmap='gray')
plt.title("Imagen de muestra: Cámara")
plt.axis('off')
_=_

%% md prov-44
# Explicación del código

1. `image = data.camera()`
En esta línea, utilizamos la función `camera()` de la biblioteca `skimage.data` para cargar una imagen de ejemplo. La imagen es en escala de grises y representa una cámara clásica. Esta función devuelve una matriz 2D en la que cada valor representa la intensidad de un píxel (su nivel de brillo) en la imagen.

1. `print(image)`
Esta línea imprime parte de la matriz que representa la imagen en la consola. Cada número corresponde al valor de brillo de un píxel en la imagen (entre 0 y 256), donde los valores bajos representan áreas oscuras y los valores altos áreas claras.

1. `print(image.shape)
Esta línea nos permite ver la forma de la matriz, en este caso vemos que la imagen tiene dimensiones de 512 x 512 píxeles.

1. `plt.imshow(image, cmap='gray')`
Aquí, utilizamos la función `imshow()` de `matplotlib.pyplot` para mostrar la imagen en pantalla. Dado que la imagen está en escala de grises, especificamos el parámetro `cmap='gray'` para que se visualice correctamente como una imagen en blanco y negro. Si no usáramos el `cmap`, podría interpretarse como una imagen en color, lo cual no es correcto.

1. `plt.title("Imagen de muestra: Cámara")`
Agregamos un título a la imagen utilizando la función `title()` para que sea más fácil identificar lo que estamos mostrando.

1. `plt.axis('off')`
Esta línea desactiva los ejes de la imagen. De esta manera, no se muestran los valores de coordenadas alrededor de la imagen, lo que ayuda a que la visualización sea más limpia y clara.



%% md prov-45
La convolución en dos dimensiones se define como:

$$
h[m,n]* I [m, n] = \sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} h(i, j) \cdot I(m-i, n-j)
$$

En este caso, las variables discretas $m$ y $n$ no representan el tiempo, sino las coordenadas de un píxel en una imagen digital.

- $I[m,n]$ representa los píxeles de la imagen que queremos procesar.

- $h[m,n]$ es el kernel o núcleo de la convolución, el equivalente a la respuesta al impulso en 2 dimensiones.



La $h[m,n]$ se elige para modificar alguna característica de la imagen, como eliminar ruido o suavizar una imagen.

###Uso de la convolución en imágenes:

El kernel $h[m,n]$ se elige para modificar ciertas características de la imagen, como suavizarla o eliminar el ruido.



%% md prov-46
## Proceso de convolución en 2D:

La **convolución en 2D** es una operación que se realiza entre una imagen y un kernel (o filtro) para obtener una nueva imagen. Esta técnica es muy utilizada en el procesamiento de imágenes para tareas como suavizado, realce de bordes y eliminación de ruido.

El kernel es una pequeña matriz (generalmente de 3x3 o 5x5) que se desliza sobre cada píxel de la imagen original. En cada paso, se multiplica el valor de los píxeles cubiertos por el kernel por los valores correspondientes en el kernel, y luego se suman estos productos para obtener el valor del nuevo píxel en la imagen resultante.

#### Cómo se aplica el kernel:

1. El kernel se posiciona sobre la imagen original, centrado en un píxel determinado.
2. Cada valor en el kernel se multiplica por el valor correspondiente de la imagen que está cubriendo.
3. Luego, se suman todos los productos.
4. Este valor sumado se asigna al píxel correspondiente en la nueva imagen.
5. El proceso se repite mientras el kernel se desliza por toda la imagen.


Consideremos un kernel pasabajos de 3x3, que es un filtro promedio simple. El siguiente kernel suaviza la imagen al reducir las variaciones bruscas de intensidad:

$$
\begin{bmatrix}
\frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\
\frac{1}{9} & \frac{1}{9} & \frac{1}{9} \\
\frac{1}{9} & \frac{1}{9} & \frac{1}{9}
\end{bmatrix}
$$

Este kernel toma el promedio de los píxeles en la vecindad de 3x3 para suavizar la imagen, reduciendo las altas frecuencias, que corresponden a cambios abruptos de brillo. El resultado es una imagen más suave, con menos detalle.

### Proceso:

1. Cuando el kernel cubre una zona de la imagen donde los valores de los píxeles son similares (como una región de color uniforme), el resultado de la convolución será muy cercano al valor promedio de esos píxeles.
2. En las zonas donde los píxeles cambian abruptamente (bordes o detalles finos), el kernel suaviza el contraste, lo que reduce la nitidez de los bordes.
3. Al final, la imagen convolucionada se verá más borrosa, ya que el filtro pasabajos atenúa las transiciones bruscas de brillo y deja pasar las zonas suaves.


%% md prov-47
A continuación, aplicaremos un filtro pasa bajos a la imagen, que reducirá las altas frecuencias. En términos visuales, esto significa atenuar los cambios bruscos de brillo, suavizando los detalles de la imagen.

Para realizar la convolución discreta en dos dimensiones utilizaremos la función  `convolve2d(image, kernel, mode='same', boundary='wrap')` del módulo `signal`de la librería `scipy`

%% code prov-48
from scipy.signal import convolve2d
# Definir un kernel de filtro pasa bajos de 3x3 (promedio de la vecindad)
kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])

convoluted_image = convolve2d(image, kernel, mode='same', boundary='wrap')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Imagen original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(convoluted_image, cmap='gray')
plt.title("Imagen convolucionada (filtro pasa bajos)")
plt.axis('off')

plt.show()


%% md enu-01
### Ejercicio

Cargue la imagen `coins` de la librería `skimage` (`data.coins()`) y aplique ala imagen un filtro pasa-altos dado por el siguiente kernel.

$$
\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}
$$

Un filtro pasaaltos en procesamiento de imágenes se utiliza para resaltar los bordes y detalles finos en la imagen, atenuando las bajas frecuencias (zonas suaves o uniformes). Un ejemplo común de kernel para un filtro pasaaltos en 2D es aquel que detecta los cambios abruptos en la intensidad de los píxeles, destacando así los bordes.

%% code act-12
#completar

%% md prov-49
Ahora aplique el filtro pasa altos a la imagen `camera`.

%% code act-13
#completar
