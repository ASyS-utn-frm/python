---
prefix: M05_funciones
source: M05_funciones.ipynb
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
# Módulo 5 — Funciones

En los módulos anteriores aprendiste a trabajar con tipos de datos, colecciones y estructuras de control. Con lo que viste ya podés decidir y repetir. Este módulo agrega la tercera herramienta fundamental: **empaquetar** un trozo de código, ponerle un nombre y reutilizarlo cuantas veces haga falta.

Una **función** es una porción de código con nombre propio, que recibe datos de entrada (sus *parámetros*) y devuelve un resultado. Cada vez que la "llamás", Python ejecuta su bloque con los valores que le pasás. La idea está inspirada directamente en las funciones matemáticas — `f(x) = 2x + 1` — pero extendida: una función de Python puede recibir varios parámetros, hacer cualquier cosa por dentro, y devolver cero, uno o varios valores.

Los temas de este módulo son:

| Tema | Para qué sirve |
|------|----------------|
| `def` y `return` | Definir una función y devolver un resultado |
| Parámetros posicionales y con nombre | Distintas formas de pasar argumentos |
| Valores por defecto | Parámetros opcionales |
| Retorno múltiple | Devolver varios resultados de una vez |
| Composición | Una función que llama a otra |
| Alcance (*scope*) | Qué variables "ve" una función |
| Funciones como valores y `lambda` | Usar una función como argumento de otra |

%% md prov-02
## 1. Definición y llamada de una función

Una función se define con la palabra clave `def`, seguida del nombre, los parámetros entre paréntesis y dos puntos. El **cuerpo** va indentado debajo (4 espacios, igual que en los `if` y `for`).

```python
def nombre_de_la_funcion(parametro1, parametro2):
    # cuerpo de la función
    return resultado
```

- `def` le indica a Python que viene una definición de función.
- `parametro1`, `parametro2`: nombres que usás **dentro** del cuerpo para referirte a los valores que te pasen al llamarla.
- `return` devuelve un valor al lugar desde donde se llamó a la función. Si no hay `return`, la función igual funciona, pero devuelve `None`.

%% md prov-03
### Ejemplo: potencia eléctrica

Calcular la potencia disipada en una resistencia se hace con $P = V^2 / R$. Escribamos una función que haga esa cuenta:

%% code prov-04
def potencia(v, r):
    return v**2 / r

# Llamamos a la función pasando valores concretos
print(potencia(5, 100))    # 5 V sobre 100 Ω → 0.25 W
print(potencia(12, 470))   # 12 V sobre 470 Ω → ~0.306 W

%% md prov-05
Separemos bien las dos cosas que pasan:

1. **Definición** (`def potencia(...)`): Python guarda la "receta" con el nombre `potencia`. En este punto **no se ejecuta** ningún cálculo todavía.
2. **Llamada** (`potencia(5, 100)`): Python agarra la receta, le entrega los valores `5` y `100` a los parámetros `v` y `r` respectivamente, ejecuta el cuerpo y devuelve el resultado.

Los nombres `v` y `r` solo existen **dentro** de la función. Afuera podés tener variables con otros nombres:

%% code prov-06
tension = 9.0
resistencia = 220

p = potencia(tension, resistencia)
print(f"P = {p:.4f} W")

%% md enu-01
### Actividad 1: una función para la ley de Ohm

Escribí una función `corriente(v, r)` que, dadas una tensión en volts y una resistencia en ohms, devuelva la corriente en amperes según $I = V / R$.

1. Definí la función.
2. Calculá la corriente para $V = 5$ V y $R = 1000$ Ω; guardala en la variable `i1`.
3. Calculá la corriente para $V = 12$ V y $R = 470$ Ω; guardala en `i2`.
4. Mostrá ambos resultados con un f-string, en miliamperes, con dos decimales. Recordá que 1 A = 1000 mA.

%% code act-01
# TU CÓDIGO AQUÍ

%% md prov-07
## 2. Parámetros posicionales y con nombre

Cuando una función tiene varios parámetros, al llamarla podés pasar los argumentos de dos formas:

- **Por posición**: en el mismo orden en que fueron definidos.
- **Por nombre** (*keyword arguments*): indicando explícitamente a qué parámetro corresponde cada valor.

%% code prov-08
def presentar(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años.")

# Por posición: nombre primero, edad después
presentar("Lucía", 25)

# Por nombre: el orden ya no importa
presentar(edad=30, nombre="Juan")

%% md prov-09
Pasar argumentos con nombre hace el código más legible cuando la función tiene varios parámetros, porque deja claro **qué significa** cada valor. Comparalo:

```python
filtrar(0.5, 1000, 8)      # ¿qué es cada número?
filtrar(umbral=0.5, fs=1000, orden=8)   # mucho más claro
```

También permite pasar los argumentos en cualquier orden.

%% md prov-10
## 3. Valores por defecto

Un parámetro puede tener un **valor por defecto**, que se usa si al llamar a la función no se especifica explícitamente. Así podés tener parámetros opcionales.

%% code prov-11
def saludar(nombre="mundo"):
    print(f"¡Hola, {nombre}!")

saludar()           # Sin argumento: usa el valor por defecto
saludar("Marta")    # Con argumento: usa "Marta"

%% md prov-12
Los parámetros **sin** valor por defecto siempre deben ir **antes** que los que tienen valor por defecto. Es decir, primero los obligatorios, después los opcionales.

Ejemplo útil: una función que calcula la frecuencia de corte de un filtro RC. La resistencia típica en muchos circuitos es 1 kΩ, así que la ponemos como valor por defecto:

%% code prov-13
def frecuencia_corte(c, r=1000):
    """Frecuencia de corte de un filtro RC (en Hz)."""
    return 1 / (2 * 3.14159 * r * c)

# Con resistencia por defecto (1 kΩ):
print(frecuencia_corte(1e-6))         # C = 1 µF
print(frecuencia_corte(c=10e-9))      # C = 10 nF (por nombre)

# Pasando también la resistencia:
print(frecuencia_corte(1e-6, 4700))   # C = 1 µF, R = 4.7 kΩ

%% md prov-13b
> **Nota sobre el *docstring*.** El texto entre triples comillas al principio del cuerpo es una cadena que Python asocia a la función como su *documentación*. No altera el funcionamiento; sirve para que, al escribir `help(frecuencia_corte)` o al pasar el mouse por encima en el editor, aparezca esa explicación breve. Es una buena costumbre ponerlo.

%% md enu-02
### Actividad 2: divisor de tensión

Un divisor de tensión con dos resistencias $R_1$ y $R_2$ y tensión de entrada $V_{in}$ entrega una tensión de salida

$$V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}$$

1. Escribí una función `divisor_tension(v_in, r1, r2)` que devuelva $V_{out}$.
2. Agregale un valor por defecto de `r2=1000` (Ω), de modo que si no se especifica, se use 1 kΩ.
3. Calculá `v_out` para $V_{in} = 12$ V, $R_1 = 4700$ Ω, dejando $R_2$ con su valor por defecto. Mostralo con un f-string.
4. Volvé a calcularlo para los mismos valores de $V_{in}$ y $R_1$, pero con $R_2 = 2200$ Ω, pasando el argumento **por nombre**.

%% code act-02
# TU CÓDIGO AQUÍ

%% md prov-14
## 4. Retornar varios valores

Una función puede devolver **más de un valor** separándolos con comas en el `return`. Python los empaqueta automáticamente en una tupla.

%% code prov-15
def estadisticos(muestras):
    media = sum(muestras) / len(muestras)
    menor = min(muestras)
    mayor = max(muestras)
    return media, menor, mayor

temperaturas = [18.5, 19.0, 20.1, 21.3, 20.8, 19.4]
resultado = estadisticos(temperaturas)
print(resultado)        # es una tupla con los tres valores
print(type(resultado))

%% md prov-16
Lo más cómodo es **desempacar** la tupla directamente en variables separadas al recibirla, así cada valor queda nombrado:

%% code prov-17
m, lo, hi = estadisticos(temperaturas)
print(f"Media:  {m:.2f}")
print(f"Mínimo: {lo}")
print(f"Máximo: {hi}")

%% md prov-18
Este patrón — función que devuelve varios resultados, llamada que los desempaca — es muy común. Evita tener que hacer varias funciones separadas para cada resultado cuando todos salen del mismo cálculo.

%% md enu-03
### Actividad 3: amplitud pico a pico y promedio

Dada una lista de muestras, querés obtener en una sola llamada el **valor medio** y la **amplitud pico a pico** (la diferencia entre el máximo y el mínimo).

1. Escribí una función `medio_y_vpp(muestras)` que devuelva ambos valores.
2. Probala con la lista `[0.0, 0.3, 0.7, 1.1, 1.4, 1.2, 0.8, 0.4, 0.0, -0.3, -0.6]`.
3. Desempacá el resultado en dos variables `vm` y `vpp`, y mostralas con un f-string, con tres decimales cada una.

%% code act-03
muestras = [0.0, 0.3, 0.7, 1.1, 1.4, 1.2, 0.8, 0.4, 0.0, -0.3, -0.6]

# TU CÓDIGO AQUÍ

%% md prov-19
## 5. Funciones que llaman a otras funciones

Una vez definida una función, se puede usar desde adentro de otras funciones. Esto permite **construir soluciones complejas combinando piezas más simples**, que se pueden probar por separado.

Veamos un ejemplo con conversión de unidades de temperatura. Definimos dos funciones básicas:

%% code prov-20
def celsius_a_kelvin(t_c):
    return t_c + 273.15

def kelvin_a_fahrenheit(t_k):
    return t_k * 9/5 - 459.67

print(celsius_a_kelvin(0))        # 273.15
print(kelvin_a_fahrenheit(300))   # ~80.33

%% md prov-21
Si ahora queremos convertir directamente de Celsius a Fahrenheit, no hace falta deducir la fórmula: podemos **combinar** las dos funciones anteriores.

%% code prov-22
def celsius_a_fahrenheit(t_c):
    t_k = celsius_a_kelvin(t_c)
    return kelvin_a_fahrenheit(t_k)

print(celsius_a_fahrenheit(0))    # 32.0
print(celsius_a_fahrenheit(100))  # 212.0

%% md prov-22b
Cada función hace una sola cosa y es fácil de verificar. Al combinarlas, obtenemos una nueva función más compleja sin repetir código ni complicar la lógica. Este estilo — **descomponer** un problema grande en funciones chicas y bien nombradas — es una de las herramientas más potentes para escribir código que se entienda y se pueda mantener.

%% md prov-22c
### Usar funciones que ya vienen con Python: `import`

Antes de la próxima actividad necesitamos una función nueva, `log10` (el logaritmo en base 10), que no viene disponible por defecto. Python trae un conjunto enorme de funciones matemáticas en un **módulo** de su biblioteca estándar llamado `math`, pero hay que **importarlas** explícitamente antes de usarlas.

La forma más cómoda es traer solo lo que necesitás con `from ... import ...`:

%% code prov-22d
from math import log10, sqrt, pi

print(log10(1000))    # 3.0
print(sqrt(2))        # 1.4142...
print(pi)             # 3.1415...

%% md prov-22e
Una vez ejecutada la línea `from math import ...`, esos nombres (`log10`, `sqrt`, `pi`) quedan disponibles en el resto del notebook como si fueran funciones o variables cualquiera.

> **Convención.** Los `import` suelen ir **al principio** del notebook (o al principio de la celda de ejemplo, si el ejemplo es autocontenido). Más adelante, en el módulo de NumPy, vas a ver una variante (`import numpy as np`) que importa el módulo completo bajo un nombre corto.

%% md enu-04
### Actividad 4: potencia en decibeles

La potencia en decibeles relativa a una referencia de 1 mW se calcula como

$$P_{dBm} = 10 \cdot \log_{10}(P / 1\,\text{mW})$$

Ya tenés la función `potencia(v, r)` de la sección 1. Ahora necesitás otra función que, dada una potencia en watts, devuelva su valor en dBm.

1. Importá `log10` con `from math import log10`.
2. Escribí una función `a_dbm(p_watts)` que devuelva la potencia en dBm. Pista: 1 mW = 0.001 W.
3. Escribí una función `v_r_a_dbm(v, r)` que, dadas tensión y resistencia, devuelva la potencia disipada en dBm. Esta función debe **usar** `potencia(...)` y `a_dbm(...)`; no repitas la fórmula.
4. Verificá que `v_r_a_dbm(1, 1000)` da un valor cercano a 0 dBm (porque $1\,\text{V}^2 / 1\,\text{k}\Omega = 1\,\text{mW}$).

%% code act-04
from math import log10

def potencia(v, r):
    return v**2 / r

# TU CÓDIGO AQUÍ

%% md prov-23
## 6. Alcance de las variables (*scope*)

Cuando una función usa una variable, Python tiene que decidir **de dónde viene** esa variable. La regla es simple:

- Las variables definidas **dentro** de la función (incluyendo sus parámetros) son **locales**: solo existen mientras la función se está ejecutando, y no se ven desde afuera.
- Las variables definidas **fuera** de cualquier función son **globales**: se pueden leer desde adentro de las funciones, pero por defecto no se pueden modificar.

### Variable local

%% code prov-24
def calcular():
    resultado = 42   # variable local: nace y muere dentro de la función
    print(resultado)

calcular()
# print(resultado)   # ← si descomentás esta línea, da NameError:
                     #   resultado no existe fuera de la función

%% md prov-25
### Lectura de una variable global

%% code prov-26
tension_alimentacion = 5.0   # global

def mostrar_alimentacion():
    print(f"Vcc = {tension_alimentacion} V")   # la lee desde adentro

mostrar_alimentacion()

%% md prov-27
### Recomendación

Mezclar lecturas de variables globales dentro de funciones es cómodo al principio, pero hace que las funciones dejen de ser **autocontenidas**: el resultado depende de cosas que están afuera, y se vuelve más difícil razonar sobre qué hace cada pieza.

La convención sana es: **todo lo que la función necesita, recibirlo como parámetro; todo lo que produce, devolverlo con `return`**. Así cada función es independiente, reutilizable y fácil de testear.

%% md prov-28
## 7. Funciones como valores y funciones `lambda`

En Python, las funciones son **valores**: podés asignarlas a una variable, guardarlas en una lista o pasarlas como argumento a otra función, exactamente como con un número o una string.

%% code prov-29
def duplicar(x):
    return 2 * x

# Asignamos la función (sin paréntesis) a otro nombre
f = duplicar
print(f(10))   # 20

%% md prov-30
Fijate que `duplicar` (sin paréntesis) se refiere a la función en sí; `duplicar(10)` sería llamarla. Al asignar `f = duplicar`, ambos nombres apuntan a la misma función.

### Funciones `lambda`

Cuando necesitás una función **muy corta y para un solo uso**, es tedioso escribir un `def` completo. Python ofrece una sintaxis compacta llamada `lambda`:

```python
lambda parametros: expresion
```

Una `lambda` define una función anónima de una sola expresión. Estas dos formas son equivalentes:

%% code prov-31
# Con def
def cuadrado(x):
    return x**2

# Con lambda
cuadrado_l = lambda x: x**2

print(cuadrado(5), cuadrado_l(5))

%% md prov-32
### Uso típico: pasar una función como argumento

El caso más frecuente de `lambda` es pasarla como argumento a otra función que espera una función. Por ejemplo, `sorted(...)` acepta un parámetro `key=` que le indica **según qué criterio** ordenar.

%% code prov-33
componentes = [
    {"nombre": "R1", "valor": 220},
    {"nombre": "R2", "valor": 1000},
    {"nombre": "R3", "valor": 47},
    {"nombre": "R4", "valor": 4700},
]

# Ordenar por el valor de resistencia, de menor a mayor
ordenados = sorted(componentes, key=lambda comp: comp["valor"])

for c in ordenados:
    print(c)

%% md prov-34
La `lambda comp: comp["valor"]` es una función chiquita que, dado un componente, devuelve su clave `"valor"`. `sorted()` la llama sobre cada elemento para decidir el orden. Para algo tan corto y local, definir una función con `def` sería exagerado.

> **Cuándo usar `lambda`.** Sirve para expresiones **simples** y **únicas**, típicamente como `key` de `sorted()`, `max()`, `min()`, o `filter()`. Si la lógica es larga o se usa en varios lugares, mejor una función definida con `def`, que puede tener nombre claro, varias líneas y hasta *docstring*.

%% md enu-05
### Actividad 5: ordenar señales por amplitud

Tenés una lista de señales, cada una representada como un diccionario con un nombre y una lista de muestras:

```python
senales = [
    {"nombre": "s1", "muestras": [0.1, -0.2, 0.3, 0.0, -0.1]},
    {"nombre": "s2", "muestras": [1.0, -1.2, 0.8, -0.9, 1.1]},
    {"nombre": "s3", "muestras": [0.5, -0.6, 0.4, -0.3, 0.7]},
]
```

1. Usá `sorted(...)` con una `lambda` para ordenar la lista **de mayor a menor** según la **amplitud pico a pico** de las muestras (la diferencia entre `max` y `min`). Pista: para ordenar descendente pasale `reverse=True` a `sorted`.
2. Recorré la lista ordenada con un `for` y mostrá, por cada señal, su nombre y su amplitud pico a pico con un f-string, con dos decimales.

%% code act-05
senales = [
    {"nombre": "s1", "muestras": [0.1, -0.2, 0.3, 0.0, -0.1]},
    {"nombre": "s2", "muestras": [1.0, -1.2, 0.8, -0.9, 1.1]},
    {"nombre": "s3", "muestras": [0.5, -0.6, 0.4, -0.3, 0.7]},
]

# TU CÓDIGO AQUÍ

%% md prov-35
## Cierre

En este módulo viste cómo empaquetar código en unidades reutilizables:

- **`def` y `return`**: la forma básica de definir una función y devolver un resultado.
- **Parámetros posicionales y con nombre**: dos maneras de pasar los argumentos al llamar; los *keyword arguments* hacen el código más legible.
- **Valores por defecto**: parámetros opcionales que no hace falta especificar en cada llamada.
- **Retorno múltiple**: devolver varios valores separados por coma; el receptor los desempaca en variables independientes.
- **Composición**: combinar funciones chicas para construir otras más grandes sin repetir código.
- **Alcance**: las variables locales viven solo dentro de la función. Preferir pasar todo por parámetro y devolver con `return`.
- **Funciones como valores y `lambda`**: una función puede usarse como dato y pasarse a otra función; `lambda` es la forma compacta para expresiones de una sola línea.

Con funciones dejás de repetir el mismo bloque de código una y otra vez: definís una vez, probás una vez, y después lo usás cuantas veces haga falta.

**En el próximo módulo** vamos a ver una idea emparentada pero más potente: **clases y objetos**. Una clase permite agrupar datos y las funciones que operan sobre esos datos en una sola unidad. Es la base de la *programación orientada a objetos*, y vas a reconocer su sintaxis cuando más adelante uses librerías como NumPy, Matplotlib o SciPy.
