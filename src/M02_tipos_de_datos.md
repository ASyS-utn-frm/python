---
prefix: M02_tipos_de_datos
source: M02_tipos_de_datos.ipynb
---

%% md hdr-01
@header

%% md prov-01
# Módulo 2 — Tipos de datos y variables

En este módulo vamos a empezar a escribir Python propiamente dicho. El foco está en lo más básico del lenguaje: **variables** (cómo guardar valores para usarlos después) y **tipos de datos** (qué clase de valores maneja Python: números, texto, etc.).

Al terminar este módulo vas a poder escribir celdas que hagan cálculos, los muestren con un formato prolijo, y pedirle datos a quien esté ejecutando el notebook.

%% md prov-02
## 1. Variables y asignación

Una **variable** es un nombre al que le asociamos un valor, para poder reutilizarlo después sin tener que volver a escribirlo. Pensalo como una etiqueta que le ponemos a un dato.

En Python la asignación se hace con el símbolo `=`:

```
nombre_de_la_variable = valor
```

Ya usamos esta idea en el Módulo 1 cuando escribimos `a = 2`. Ahora lo vemos con un poco más de detalle.

%% code prov-03
edad = 22
pi_aprox = 3.14
nombre = "Ana"

%% md prov-04
Después de ejecutar esa celda, las tres variables quedan guardadas en memoria (en el kernel del notebook). Podés usarlas en cualquier celda posterior:

%% code prov-05
edad + 5

%% md prov-06
> **Nota:** en Python la asignación no imprime nada por pantalla. Para ver el valor de una variable hay dos formas comunes: escribir su nombre solo en la última línea de una celda (como arriba), o usar `print()`, que veremos en la próxima sección.

%% md prov-07
### Reglas para nombrar variables

Un nombre de variable puede contener letras, números y guiones bajos (`_`), **pero no puede empezar con un número**. Tampoco puede tener espacios ni signos como `-`, `+`, `$`, etc.

Además, los nombres son **sensibles a mayúsculas y minúsculas**: `edad`, `Edad` y `EDAD` son tres variables distintas.

%% code prov-08
edad = 22
Edad = 99
print(edad, Edad)

%% md prov-09
Por convención, en Python se usan nombres en minúsculas, separando palabras con guión bajo: `tiempo_total`, `frecuencia_corte`, `indice_maximo`. Elegí nombres que describan lo que contiene la variable — es la mejor forma de que tu código se entienda solo.

Hay también un conjunto de palabras **reservadas** por Python (como `if`, `for`, `def`, `return`, `import`, `True`, `False`, `None`, etc.) que no pueden usarse como nombres de variables. Las vas a ir reconociendo a medida que avances en el curso.

%% md enu-01
### Actividad 1: primeras asignaciones

En la celda de abajo:

1. Creá una variable `frecuencia` con el valor `50` (la frecuencia de la red eléctrica en Argentina, en Hz).
2. Creá una variable `periodo` que valga `1 / frecuencia`.
3. Escribí `periodo` en la última línea para ver su valor.

%% code act-01
# TU CÓDIGO AQUÍ

%% md prov-10
## 2. La función `print()`

`print()` es la función más básica de Python: muestra por pantalla lo que le pases entre paréntesis. Ya la usamos en el Módulo 1 de forma intuitiva; ahora la vemos en detalle, porque la vas a usar en cada notebook del curso.

%% code prov-11
print("Hola")
print(42)
print(2 + 3)

%% md prov-12
`print()` puede recibir **varios argumentos separados por comas**, y los muestra en la misma línea separados por un espacio:

%% code prov-13
nombre = "Ana"
edad = 22
print("Nombre:", nombre, "- Edad:", edad)

%% md prov-14
### f-strings: la forma prolija de armar mensajes

Cuando querés mezclar texto fijo con valores de variables, la forma más clara es usar **f-strings** (del inglés *formatted string literals*). Se escribe una `f` antes de las comillas, y dentro del texto se colocan las variables entre llaves `{ }`:

%% code prov-15
nombre = "Ana"
edad = 22
print(f"{nombre} tiene {edad} años.")

%% md prov-16
Dentro de las llaves también se pueden poner **expresiones**, no solo variables:

%% code prov-17
a = 3
b = 4
print(f"La suma de {a} y {b} es {a + b}.")

%% md prov-18
Los f-strings son la forma recomendada de armar mensajes y vas a verlos todo el tiempo en el curso.

%% md enu-02
### Actividad 2: armar un mensaje con f-string

Dadas las variables `resistencia = 220` (en ohms) y `corriente = 0.05` (en amperes), usá un f-string en una llamada a `print()` para mostrar el mensaje:

```
Con R = 220 ohms e I = 0.05 A, la tensión es V = 11.0 V
```

Recordá que la Ley de Ohm dice $V = R \cdot I$. Usá las variables (no escribas los números a mano dentro del mensaje) y calculá la tensión dentro del propio f-string.

%% code act-02
resistencia = 220
corriente = 0.05

# TU CÓDIGO AQUÍ

%% md prov-19
## 3. Tipos numéricos: enteros y flotantes

Python tiene dos tipos numéricos básicos:

- **`int`** (*integer*): números enteros, sin parte decimal. Por ejemplo `3`, `-7`, `42`.
- **`float`** (*floating point*): números con parte decimal. Por ejemplo `3.14`, `-0.5`, `2.0`.

La función `type()` te dice el tipo de un valor o de una variable:

%% code prov-20
print(type(3))
print(type(3.0))

%% md prov-21
Observá que `3` y `3.0` son matemáticamente iguales pero Python los distingue: el `.0` marca que es un flotante. En la práctica, **cualquier operación con un flotante da un flotante**.

### Operaciones aritméticas

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| `+` | suma | `3 + 2` → `5` |
| `-` | resta | `5 - 2` → `3` |
| `*` | multiplicación | `4 * 3` → `12` |
| `/` | división (siempre da flotante) | `10 / 4` → `2.5` |
| `//` | división entera (descarta el resto) | `10 // 4` → `2` |
| `%` | resto de la división | `10 % 4` → `2` |
| `**` | potencia | `2 ** 3` → `8` |

%% code prov-22
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)

%% md prov-23
### Precedencia y paréntesis

Python respeta la precedencia matemática habitual: primero paréntesis, después potencia, después multiplicación y división, y por último suma y resta. Ante la duda, **usá paréntesis**: aclaran la intención y evitan errores.

%% code prov-24
print(2 + 3 * 4)       # 14  (primero 3*4, después +2)
print((2 + 3) * 4)     # 20  (los paréntesis fuerzan el orden)
print(2 ** 3 * 2)      # 16  (primero 2**3, después *2)

%% md enu-03
### Actividad 3: cálculo con flotantes

La velocidad del sonido en el aire a 20 °C es aproximadamente `343` m/s. Si un sonido viaja `0.8` segundos hasta chocar con una pared y volver, ¿a qué distancia está la pared?

Pista: el sonido recorre ida y vuelta, así que la distancia a la pared es la mitad del recorrido total.

Guardá el resultado en una variable `distancia` y mostralo con un f-string que diga `La pared está a X metros.`

%% code act-03
velocidad_sonido = 343
tiempo_ida_y_vuelta = 0.8

# TU CÓDIGO AQUÍ

%% md prov-25
## 4. Booleanos y comparaciones

El tipo **`bool`** (booleano) solo tiene dos valores posibles: `True` y `False`. Representan una afirmación verdadera o falsa.

%% code prov-26
print(type(True))
print(type(False))

%% md prov-27
### Comparaciones

Los **operadores de comparación** comparan dos valores y devuelven un booleano:

| Operador | Significado |
|----------|-------------|
| `==` | igual a |
| `!=` | distinto de |
| `<` | menor que |
| `<=` | menor o igual que |
| `>` | mayor que |
| `>=` | mayor o igual que |

Ojo con `=` vs `==`: `=` es **asignación** (guardar un valor), `==` es **comparación** (preguntar si son iguales).

%% code prov-28
print(3 == 3)
print(3 == 4)
print(3 < 4)
print(3 >= 3)

%% md prov-29
### Operadores lógicos

Para combinar varios booleanos se usan `and`, `or` y `not`:

- `a and b` → `True` solo si ambos son `True`.
- `a or b` → `True` si al menos uno es `True`.
- `not a` → invierte el valor (`True` se vuelve `False` y viceversa).

%% code prov-30
print(True and False)
print(True or False)
print(not True)

%% code prov-31
x = 5
print(0 < x and x < 10)   # ¿x está entre 0 y 10?
print(x == 5 or x == 10)  # ¿x es 5 o 10?

%% md prov-32
> **Nota:** los booleanos y las comparaciones se vuelven realmente útiles cuando queremos que el programa **tome decisiones** (ejecutar algo solo si se cumple una condición). Eso lo vemos en el Módulo 4 — por ahora alcanza con saber que existen y cómo se evalúan.

%% md enu-04
### Actividad 4: evaluar comparaciones

Dado `tension = 12` (volts), escribí tres expresiones que devuelvan booleanos y mostralas con `print()`:

1. ¿La tensión es positiva?
2. ¿La tensión está entre 5 y 24 inclusive?
3. ¿La tensión es distinta de 0?

%% code act-04
tension = 12

# TU CÓDIGO AQUÍ

%% md prov-33
## 5. Cadenas de caracteres (strings)

El tipo **`str`** (*string*) representa texto: una secuencia de caracteres. Se escribe entre comillas simples `'...'` o dobles `"..."` — son equivalentes, y podés usar la que te resulte más cómoda (o la que evite tener que escapar caracteres).

%% code prov-34
saludo = "Hola"
nombre = 'Ana'
print(type(saludo))
print(saludo, nombre)

%% md prov-35
### Concatenación

El operador `+` aplicado a dos strings los **une** (concatena):

%% code prov-36
mensaje = saludo + ", " + nombre + "!"
print(mensaje)

%% md prov-37
En la mayoría de los casos, sin embargo, un f-string queda más prolijo que concatenar con `+`:

%% code prov-38
print(f"{saludo}, {nombre}!")

%% md prov-39
### Strings multilínea: comillas triples

Si querés que un string ocupe varias líneas, se usan **comillas triples** (`"""..."""` o `'''...'''`):

%% code prov-40
texto_largo = """Esta es la primera línea.
Esta es la segunda.
Y esta es la tercera."""

print(texto_largo)

%% md prov-41
> **Aclaración útil.** A veces vas a encontrar, dentro de un código, un bloque de texto entre comillas triples "flotando" sin asignarse a ninguna variable. Se usan a menudo **como si fueran comentarios** de varias líneas, y funciona porque Python simplemente evalúa el string y lo descarta. Pero técnicamente **no son comentarios**: son strings (objetos de tipo `str`) que no se están usando. El comentario real en Python es el que empieza con `#`.

%% md prov-42
## 6. Números complejos

Python tiene soporte nativo para números complejos — fundamentales en análisis de señales y sistemas. Se escriben con el sufijo `j` para la parte imaginaria:

%% code prov-43
z = 3 + 4j
print(z)
print(type(z))

%% md prov-44
A un complejo `z` se le pueden pedir:

- `z.real` → parte real
- `z.imag` → parte imaginaria
- `abs(z)` → módulo (magnitud)

%% code prov-45
z = 3 + 4j
print(f"z = {z}")
print(f"Parte real: {z.real}")
print(f"Parte imaginaria: {z.imag}")
print(f"|z| = {abs(z)}")

%% md prov-46
Los complejos se suman, restan, multiplican y dividen entre sí como cualquier otro número:

%% code prov-47
z1 = 2 + 3j
z2 = 1 - 1j
print(f"Suma:   {z1 + z2}")
print(f"Producto: {z1 * z2}")

%% md prov-48
> **Para más adelante.** Operaciones típicas de álgebra compleja (fase, exponencial compleja, conversión a forma polar) se hacen muy cómodamente con la librería **NumPy**, que vemos en el Módulo 7. La aplicación a señales y sistemas se desarrolla en el Laboratorio 2. Por ahora alcanza con saber crear un complejo y acceder a sus partes.

%% md enu-05
### Actividad 5: un complejo a mano

Dado $z = 1 + \sqrt{3}\, j$, en la celda de abajo:

1. Asignalo a una variable `z` (usá `3 ** 0.5` para $\sqrt{3}$).
2. Mostrá con un f-string su parte real, parte imaginaria y su módulo, cada uno en una línea.

%% code act-05
# TU CÓDIGO AQUÍ

%% md prov-49
## 7. Conversiones entre tipos

A veces tenés un valor de un tipo y lo necesitás en otro. Python ofrece funciones de conversión que tienen el mismo nombre que el tipo destino:

| Función | Convierte a |
|---------|-------------|
| `int(x)` | entero |
| `float(x)` | flotante |
| `str(x)` | string |
| `bool(x)` | booleano |

%% code prov-50
print(int(3.7))      # 3 — al pasar de float a int, se trunca (no redondea)
print(float(5))      # 5.0
print(str(42))       # "42"  (ahora es texto)
print(int("123"))    # 123  (texto que representa un número → int)

%% md prov-51
**Un caso típico:** cuando se leen datos como texto (por ejemplo desde teclado o desde un archivo) hay que convertirlos a número para poder hacer cuentas. Eso es exactamente lo que vamos a hacer en la siguiente sección con `input()`.

%% md prov-52
## 8. Leer datos del usuario con `input()`

La función `input()` detiene la ejecución y espera a que quien ejecuta el notebook escriba algo y apriete Enter. Devuelve **siempre un string** con lo que se escribió — aunque sea un número.

%% code prov-53
nombre = input("¿Cómo te llamás? ")
print(f"Hola, {nombre}!")

%% md prov-54
Si lo que pedimos es un número, hay que **convertirlo** después de leerlo:

%% code prov-55
texto = input("Escribí un número entero: ")
numero = int(texto)
print(f"El doble es {2 * numero}")

%% md prov-56
Un patrón común es envolver las dos cosas en una sola línea:

%% code prov-57
numero = int(input("Escribí un número entero: "))
print(f"Su cuadrado es {numero ** 2}")

%% md prov-58
> **Dato práctico:** `input()` se usa muchísimo como herramienta didáctica para hacer que un programa se vuelva "interactivo". En los notebooks del curso vamos a usarlo ocasionalmente para que puedas probar tu código con distintos valores sin tener que editar la celda cada vez.

%% md enu-06
### Actividad 6: convertir temperaturas

Pedile al usuario una temperatura en grados Celsius con `input()`, convertila a flotante y mostrá su equivalente en Fahrenheit. La fórmula es:

$$F = C \cdot 1.8 + 32$$

Usá un f-string para mostrar el resultado con la forma `X °C equivalen a Y °F`.

%% code act-06
# TU CÓDIGO AQUÍ

%% md prov-59
## Cierre

En este módulo viste los bloques más elementales de Python:

- **Variables** y la regla `nombre = valor`.
- **`print()`** y los **f-strings** para mostrar información con formato.
- Los tipos **`int`**, **`float`**, **`bool`**, **`str`** y **`complex`**, con sus operaciones básicas.
- **Comparaciones** (`==`, `<`, ...) y **operadores lógicos** (`and`, `or`, `not`).
- **Conversiones** entre tipos con `int()`, `float()`, `str()`, `bool()`.
- **`input()`** para pedir datos al usuario.

**En el próximo módulo** vamos a ver cómo **agrupar varios valores** en una misma variable: listas, tuplas y diccionarios. Eso va a ser clave para trabajar con señales, que no son otra cosa que secuencias de valores.
