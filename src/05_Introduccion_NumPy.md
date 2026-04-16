---
prefix: 05_Introduccion_NumPy
source: 05_Introduccion_NumPy.ipynb
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

%% md prov-01
#1. Introducción a Librerías en Python

Las librerías en Python son colecciones de módulos que contienen funciones y métodos que pueden ser utilizados en nuestros programas para realizar tareas específicas. Estas librerías nos permiten reutilizar código y simplificar el desarrollo, ya que no necesitamos escribir todo desde cero.

Como vimos previamente con `cmath` (librería para trabajar con números complejos) para utilizar una librería en Python, primero necesitamos importarla utilizando la palabra clave `import`. Una vez importada, podemos acceder a todas sus funciones y métodos.

**Ejemplo de Importación**


%% code prov-02
import numpy as np  # Importamos la librería NumPy con el alias np


%% md prov-03
En este ejemplo, estamos importando la librería NumPy y asignándole el alias `np` para facilitar su uso.

%% md prov-04
# 2. Introducción a NumPy

%% md prov-05
NumPy es una librería fundamental para la computación científica en Python. Proporciona soporte para arreglos (arrays) lo que comprende vectores y matrices multidimensionales, junto con una colección de funciones matemáticas para operar con estos arreglos.

%% md prov-06
## 2.1 Introducción a arreglos (Arrays)

Un array (o arreglo) es una estructura de datos que contiene una colección de elementos, todos del mismo tipo, almacenados en posiciones contiguas de memoria. Los arrays permiten almacenar múltiples valores en una sola variable, lo que facilita la organización y manipulación de grandes conjuntos de datos.

**Características de los Arrays**

- Homogeneidad: Todos los elementos de un array son del mismo tipo. Por ejemplo, todos los elementos pueden ser enteros, flotantes, cadenas de texto, etc; pero no una mezcla de ellos

- Acceso Directo: Los elementos de un array pueden ser accedidos directamente utilizando un índice, lo que permite operaciones rápidas de lectura y escritura.

- Dimensionalidad: Los arrays pueden ser unidimensionales (vectores), bidimensionales (matrices) o multidimensionales, lo que permite representar datos complejos como tablas, imágenes, y más.

- Eficiencia: Los arrays son eficientes en términos de uso de memoria y velocidad de acceso, lo que los hace ideales para operaciones numéricas y científicas.

Un array unidimensional es una lista de elementos. En Python, podemos crear un array utilizando la librería NumPy:

%% code prov-07
import numpy as np

# Creando un array unidimensional (vector)
arr = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", arr)

%% md prov-08
Un array bidimensional es similar a una tabla de elementos, con filas y columnas. En NumPy, podemos crear un array bidimensional de la siguiente manera:

%% code prov-09
import numpy as np

# Creando un array bidimensional (matriz)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array bidimensional:\n", arr_2d)

%% md prov-10
**Aplicaciones de los Arrays**

- Cálculos Matemáticos: Los arrays son fundamentales para realizar operaciones matemáticas y científicas, como álgebra lineal, cálculo vectorial y transformadas.

- Procesamiento de Imágenes: Las imágenes digitales pueden ser representadas como arrays bidimensionales (para imágenes en escala de grises) o tridimensionales (para imágenes en color).

- Análisis de Datos: Los arrays permiten almacenar y manipular grandes conjuntos de datos de manera eficiente, siendo una base para herramientas de análisis y visualización de datos.

- Simulaciones: En simulaciones numéricas y modelos científicos, los arrays se utilizan para representar y calcular estados y variaciones en sistemas complejos.

- Inteligencia Artificial: Los arrays son una pieza elemental de funcionamiento de las redes neuronales y particularmente del aprendizaje profundo (Deep Learning) ya que para estos campos es fundamental trabajar con arreglos de múltiples dimensiones, comunmente llamados tensores.

- La forma de manipular la información en NumPy es muy similar a cómo se manipula la información en Matlab, el cual es un software muy utilizado en análisis científico y diseño de sistemas de control electromecánicos.


**Propiedad shape**

La propiedad `shape` de un arreglo NumPy nos dice las dimensiones del arreglo. Es una tupla de enteros que indican el tamaño del arreglo en cada dimensión. Esto es muy útil para entender la estructura del arreglo y para realizar operaciones que requieren conocimiento de su forma.



%% code prov-11
# Ejemplo de uso de shape
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Forma del arreglo:", arr_2d.shape)  # Muestra (2, 3)


%% md prov-12
En este ejemplo, shape devuelve (2, 3), indicando que el arreglo tiene 2 filas y 3 columnas.



## 2.2. Arreglos rellenos de Ceros y Unos

NumPy proporciona funciones para crear arreglos llenos de ceros o unos.

%% code prov-13
# matriz de 3x3 llena de ceros
arr_zeros = np.zeros((3, 3))
print("Arreglo de ceros:\n", arr_zeros)

# matriz de 2x4 llena de unos
arr_ones = np.ones((2, 4))
print("Arreglo de unos:\n", arr_ones)

%% md prov-14
## 2.3. Arreglos con Rangos

NumPy ofrece funciones muy útiles para crear arreglos con secuencias de números. Las dos funciones principales que utilizamos para esto son `np.arange` y `np.linspace`.

### 2.3.1. `np.arange`

La función np.arange es similar a la función range de Python y se utiliza para crear arreglos con secuencias de números equidistantes. La sintaxis es:

~~~python
np.arange(inicio, fin, paso)
~~~

- `inicio` (opcional): El valor inicial de la secuencia (incluido). Si se omite, por defecto es 0.

- `fin`: El valor final de la secuencia (excluido).

- `paso` (opcional): El tamaño del paso entre valores sucesivos en la secuencia. Si se omite, por defecto es 1.

**Ejemplo Básico de np.arange**

%% code prov-15
import numpy as np

# Crear un arreglo de 0 a 9
arr_arange = np.arange(10)
print("Arreglo de 0 a 9:", arr_arange)


%% md prov-16
**Ejemplo con Paso Específico**

%% code prov-17
# Crear un arreglo de 0 a 9 con un paso de 2
arr_arange_paso = np.arange(0, 10, 2)
print("Arreglo de 0 a 9 con paso de 2:", arr_arange_paso)

%% md prov-18
**Ejemplo con Valores Flotantes**


%% code prov-19
# Crear un arreglo de 0 a 1 con un paso de 0.2
arr_arange_float = np.arange(0, 1, 0.2)
print("Arreglo de 0 a 1 con paso de 0.2:", arr_arange_float)

%% md prov-20
## 2.3.2. `np.linspace`

La función `np.linspace` se utiliza para crear un arreglo con un número específico de valores equidistantes entre un intervalo. La sintaxis es:

~~~
np.linspace(inicio, fin, num)
~~~

- `inicio`: El valor inicial de la secuencia (incluido).
- `fin`: El valor final de la secuencia (incluido).
- `num`: El número de valores a generar en la secuencia.

**Ejemplo Básico de ´np.linspace´**

%% code prov-21
# Crear un arreglo de 5 valores equidistantes entre 0 y 1
arr_linspace = np.linspace(0, 1, 5)
print("Arreglo con 5 valores entre 0 y 1:", arr_linspace)


%% md prov-22
**Ejemplo con más valores**

%% code prov-23
# Crear un arreglo de 10 valores equidistantes entre 0 y 2
arr_linspace_mas = np.linspace(0, 2, 10)
print("Arreglo con 10 valores entre 0 y 2:", arr_linspace_mas)

%% md hdr-02
Estas funciones son muy útiles en el análisis de señales y sistemas, ya que permiten crear fácilmente secuencias de valores para representar tiempos, frecuencias, y otras variables continuas.

## 2.4. Operaciones Básicas con Arreglos

NumPy permite realizar operaciones matemáticas y lógicas de manera eficiente sobre arreglos. Las operaciones básicas incluyen aritmética de elementos, funciones matemáticas, y operaciones de agregación. Estas operaciones se aplican elemento a elemento y son extremadamente rápidas debido a la optimización interna de NumPy.

### 2.4.1 Operaciones Aritméticas

Las operaciones aritméticas básicas (suma, resta, multiplicación, y división) pueden realizarse directamente sobre arreglos de NumPy.

Ejemplo de Operaciones Aritméticas

%% code prov-24
import numpy as np

# Crear un arreglo
arr = np.array([1, 2, 3, 4])
print("Arreglo original:", arr)

# Suma
print("Suma 2 a cada elemento:", arr + 2)

# Resta
print("Resta 1 a cada elemento:", arr - 1)

# Multiplicación
print("Multiplica cada elemento por 3:", arr * 3)

# División
print("Divide cada elemento por 2:", arr / 2)

# Potencia
print("Cuadrado de cada elemento:", arr ** 2)


%% md prov-25
En este ejemplo, cada operación aritmética se aplica a cada elemento del arreglo individualmente. NumPy maneja automáticamente la difusión de valores escalares para aplicar la operación a todos los elementos del arreglo.

### 2.4.2 Operaciones entre Arreglos

Puedes realizar operaciones aritméticas entre dos arreglos de NumPy de la misma forma que con números escalares. Los arreglos deben tener la misma forma (shape).

**Ejemplo de Operaciones entre Arreglos**

%% code prov-26
# Crear dos arreglos
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# Suma
print("Suma de dos arreglos:", arr1 + arr2)

# Resta
print("Resta de dos arreglos:", arr1 - arr2)

# Multiplicación
print("Multiplicación de dos arreglos:", arr1 * arr2)

# División
print("División de dos arreglos:", arr1 / arr2)


%% md prov-27
En este ejemplo, cada operación se realiza elemento a elemento entre los dos arreglos.

### 2.4.3 Funciones Matemáticas

NumPy proporciona una amplia variedad de funciones matemáticas para realizar operaciones avanzadas en arreglos. Algunas de estas funciones incluyen np.sin, np.cos, np.exp, np.sqrt, y np.log.

**Ejemplo de Funciones Matemáticas**

%% code prov-28
# Crear un arreglo
arr = np.array([0, np.pi/2, np.pi])

# Seno
print("Seno de los elementos:", np.sin(arr))

# Coseno
print("Coseno de los elementos:", np.cos(arr))

# Exponencial
print("Exponencial de los elementos:", np.exp(arr))

# Raíz cuadrada
print("Raíz cuadrada de los elementos:", np.sqrt(np.array([1, 4, 9, 16])))

# Logaritmo natural
print("Logaritmo natural de los elementos:", np.log(np.array([1, np.e, np.e**2])))


%% md prov-29
En este ejemplo, cada función matemática se aplica a cada elemento del arreglo, devolviendo un nuevo arreglo con los resultados.

### 2.4.4 Operaciones de Agregación

Las operaciones de agregación calculan un solo valor a partir de un arreglo de valores como cuando calculamos un promedio de numeros o un producto escalar. NumPy proporciona funciones como `np.sum`, `np.mean`, `np.std`, `np.min`, y `np.max` para realizar estas operaciones.

**Ejemplo de Operaciones de Agregación**

%% code prov-30
# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5])

# Suma
print("Suma de los elementos:", np.sum(arr))

# Promedio
print("Promedio de los elementos:", np.mean(arr))

# Desviación estándar
print("Desviación estándar de los elementos:", np.std(arr))

# Mínimo
print("Valor mínimo:", np.min(arr))

# Máximo
print("Valor máximo:", np.max(arr))


%% md prov-31
### 2.5 Constantes de NumPy

NumPy incluye varias constantes matemáticas útiles que pueden ser utilizadas en cálculos científicos y de ingeniería. Aquí están algunas de las más comunes:




%% code prov-32
print("Valor de pi:", np.pi)

print("Valor de e:", np.e)


%% md hdr-03
## 2.6 Slicing en NumPy

El slicing en NumPy nos permite seleccionar y manipular sub-arreglos de un arreglo existente de manera muy eficiente. Esto es especialmente útil en el análisis de señales, donde a menudo necesitamos trabajar con segmentos específicos de una señal.

**Sintaxis Básica de Slicing**

La sintaxis básica para realizar slicing en NumPy es similar a la de las listas en Python:

~~~python
arreglo[inicio:fin:paso]
~~~

%% md prov-33
- `inicio` : El índice del primer elemento del subarreglo (incluido). Si se omite, se asume el valor 0.

- `fin`: El índice del último elemento del subarreglo (excluido). Si se omite, se asume el valor de la longitud del arreglo.

- `paso`: El tamaño del paso entre elementos. Si se omite, se asume el valor 1.

**Ejemplos de Slicing**


Primero, crearemos un vector de ejemplo sobre el que trabajaremos con slicing



%% code prov-34
# Crear un vector de ejemplo
vector = np.arange(1, 101)  # Vector con valores del 1 al 100

# Mostrar los primeros 10 elementos del vector
print("Vector completo (primeros 10 elementos):", vector[:10])


%% md prov-35
**Seleccionar un Subarreglo**

Podemos seleccionar un segmento específico del vector usando slicing.

%% code prov-36
# Seleccionar los primeros 20 elementos del vector
segmento_inicial = vector[:20]

# Mostrar los primeros 10 elementos del segmento seleccionado
print("Segmento inicial del vector (primeros 10 elementos):", segmento_inicial[:10])


%% md prov-37
**Seleccionar un Segmento Central**

Seleccionar una parte central del vector también es sencillo.

%% code prov-38
# Seleccionar los elementos del índice 40 al 60
segmento_central = vector[40:60]

# Mostrar los primeros 10 elementos del segmento central
print("Segmento central del vector (primeros 10 elementos):", segmento_central[:10])


%% md prov-39
**Seleccionar Elementos con un Paso**

Podemos seleccionar elementos a intervalos regulares utilizando el parámetro `paso`.

%% code prov-40
# Seleccionar los primeros 20 elementos del vector
segmento_inicial = vector[:20]

# Mostrar los primeros 10 elementos del segmento seleccionado
print("Segmento inicial del vector (primeros 10 elementos):", segmento_inicial[:10])


%% md prov-41
**Advertencia Importante: Vistas y Copias**

Es importante tener en cuenta que cuando realizamos slicing en un array de NumPy, se crea una vista del array original, no una copia independiente. Esto significa que cualquier modificación realizada en la vista afectará directamente al array original.

%% code prov-42
# Crear una vista usando slicing
vista = vector[:10]

# Modificar un elemento de la vista
vista[0] = 99

# Mostrar el vector original y la vista después de la modificación
print("Vector original después de modificar la vista:", vector[:20])
print("Vista del vector después de la modificación:", vista)


%% md prov-43
Si necesitas trabajar con un subarreglo sin modificar el array original, asegúrate de crear una copia explícita usando el método `copy`.

%% code prov-44
# Crear una copia del vector usando slicing y el método copy
copia = vector[:10].copy()

# Modificar un elemento de la copia
copia[0] = 100

# Mostrar el vector original y la copia después de la modificación
print("Vector original después de modificar la copia:", vector[:20])
print("Copia del vector después de la modificación:", copia)


%% md prov-45
## 3. Trabajando con Arreglos de Números Complejos en NumPy

Puedes crear arreglos de números complejos directamente utilizando `numpy.array` y especificando los números complejos:




%% code prov-46
# Creación de un arreglo de números complejos
arreglo_complejo = np.array([1+2j, 3+4j, 5+6j])

print("Arreglo de números complejos:")
print(arreglo_complejo)


%% md prov-47
Puedes acceder a las partes reales e imaginarias de los números complejos en un arreglo utilizando las propiedades `.real` y `.imag`:

%% code prov-48
  # Partes reales del arreglo
partes_reales = arreglo_complejo.real

# Partes imaginarias del arreglo
partes_imaginarias = arreglo_complejo.imag

print("Partes reales del arreglo:")
print(partes_reales)

print("Partes imaginarias del arreglo:")
print(partes_imaginarias)


%% md prov-49
**Operaciones con Arreglos de Números Complejos**

Puedes realizar operaciones matemáticas con arreglos de números complejos de la misma manera que con arreglos de números reales.

### 3.1. Suma y Resta

%% code prov-50
# Suma de arreglos de números complejos
arreglo_suma = arreglo_complejo + np.array([1+1j, 2+2j, 3+3j])

# Resta de arreglos de números complejos
arreglo_resta = arreglo_complejo - np.array([1+1j, 2+2j, 3+3j])

print("Suma de arreglos de números complejos:")
print(arreglo_suma)

print("Resta de arreglos de números complejos:")
print(arreglo_resta)


%% md prov-51
### 3.2. Multiplicación y División


%% code prov-52
# Multiplicación de arreglos de números complejos
arreglo_multiplicacion = arreglo_complejo * np.array([1+1j, 2+2j, 3+3j])

# División de arreglos de números complejos
arreglo_division = arreglo_complejo / np.array([1+1j, 2+2j, 3+3j])

print("Multiplicación de arreglos de números complejos:")
print(arreglo_multiplicacion)

print("División de arreglos de números complejos:")
print(arreglo_division)


%% md prov-53
### 3.3 Magnitud y Fase de Números Complejos

Puedes calcular la magnitud y la fase de cada elemento en un arreglo de números complejos utilizando numpy.abs y numpy.angle respectivamente.

**Magnitud**

%% code prov-54
# Magnitud de los elementos del arreglo de números complejos
magnitudes = np.abs(arreglo_complejo)

print("Magnitudes de los elementos del arreglo:")
print(magnitudes)


%% md prov-55
**Fase**

%% code prov-56
# Fase de los elementos del arreglo de números complejos
fases = np.angle(arreglo_complejo)

print("Fases de los elementos del arreglo:")
print(fases)


%% md prov-57
### 3.4 Funciones Trigonométricas y Exponenciales

`numpy` también proporciona funciones para calcular el seno, coseno y la exponencial de números complejos.

%% code prov-58
# Seno de los elementos del arreglo de números complejos
senos = np.sin(arreglo_complejo)

# Coseno de los elementos del arreglo de números complejos
cosenos = np.cos(arreglo_complejo)

# Exponencial de los elementos del arreglo de números complejos
exponenciales = np.exp(arreglo_complejo)

print("Seno de los elementos del arreglo:")
print(senos)

print("Coseno de los elementos del arreglo:")
print(cosenos)

print("Exponencial de los elementos del arreglo:")
print(exponenciales)


%% md prov-59
----
Con esto llegamos al final de este tutorial! Recuerda que los temas que desarrollamos en los tutoriales de la cátedra son tratados de manera básica y contienen solo lo necesario para poder presentar de forma didáctica los contenidos de la asignatura. Entender Python en profundidad requiere un curso completo dedicado a ello.

En [este link](https://github.com/vinta/awesome-python)  encontrarás una extensa cantidad de librerías de python para trabajar prácticamente sobre cualquier temática que necesites.

En [este link](https://docs.python.org/es/3.9/) encontrarás la documentación completa de Python

En [este link](https://numpy.org/doc/2.0/user/index.html#user) encontrarás la documentación completa de NumPy.


Cualquier comentario no dudes en consultar con los profesores de la cátedra.

