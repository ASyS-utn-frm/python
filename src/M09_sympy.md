---
prefix: M09_sympy
source: M09_sympy.ipynb
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
# Módulo 9 — SymPy

En todo lo que viste hasta acá, Python manejaba **números**: una variable valía 3, o 2.5, o `3+4j`. Un array de NumPy tiene miles de números. Matplotlib dibuja números. Cuando pedís `np.sin(1.0)`, la computadora calcula un valor aproximado con muchos decimales y te lo devuelve.

Hay otra forma de hacer matemática, una que no pasa por los números: el **álgebra simbólica**. En lugar de preguntar "¿cuánto da $\sin(1.0)$?" trabajás con el símbolo $x$ y manipulás la expresión: la derivás, la factorizás, la resolvés. El resultado es exacto y se expresa con los mismos símbolos, no con un número aproximado.

**SymPy** es la librería estándar de Python para hacer eso. Es lo más cercano a tener Mathematica o Maple integrado en tu notebook. Se usa para:

- Derivar e integrar funciones de manera exacta.
- Resolver ecuaciones con variables literales (no solo con valores concretos).
- Simplificar, factorizar y expandir expresiones algebraicas.
- Tener resultados exactos en fracciones o radicales, sin errores de redondeo.

Los temas de este módulo son:

| Tema | Para qué sirve |
|------|----------------|
| `import sympy as sy` | Cargar la librería |
| `sy.symbols(...)` | Crear variables simbólicas |
| `sy.simplify`, `factor`, `expand` | Manipular expresiones algebraicas |
| `.subs(...)` y `.evalf()` | Sustituir variables y evaluar numéricamente |
| `sy.solve(...)` | Resolver ecuaciones y sistemas |
| `sy.diff(...)` y `sy.integrate(...)` | Derivar e integrar simbólicamente |
| `sy.Piecewise(...)` | Funciones definidas a trozos |
| `sy.lambdify(...)` | Convertir una expresión simbólica en una función numérica para graficar |

> **Numérico vs. simbólico.** NumPy y SymPy son herramientas complementarias, no competidoras. NumPy es rápido y trabaja con números; SymPy es exacto y trabaja con símbolos. Al final de este módulo vas a ver cómo combinarlas: derivar algo con SymPy y después graficarlo con NumPy y Matplotlib.

%% md prov-02
## 1. Cargar SymPy

Por convención, se importa con el alias `sy`. Además, conviene llamar una vez a `sy.init_printing()`: esto le dice a Jupyter que muestre las expresiones con formato matemático (fracciones apiladas, exponentes en superíndice, etc.) en lugar de texto plano.

%% code prov-03
import sympy as sy

sy.init_printing()

%% md prov-04
`init_printing()` se ejecuta **una sola vez** al abrir el notebook. A partir de ahí, cuando una celda termine con una expresión simbólica, Jupyter la va a dibujar en formato matemático automáticamente.

%% md prov-05
## 2. Variables simbólicas

El punto de partida de todo trabajo con SymPy es declarar qué letras van a ser símbolos. No alcanza con escribir `x + 2`: antes tenés que decirle a SymPy "la letra `x` es un símbolo". Se hace con la función `sy.symbols`:

%% code prov-06
x = sy.symbols("x")
print(type(x))

%% md prov-07
`x` ya no es un número: es un objeto de la clase `Symbol`. Una vez que existe, podés armar expresiones algebraicas combinándolo con operadores de Python (`+`, `-`, `*`, `/`, `**`) o con funciones de SymPy. El resultado es otra expresión simbólica, que Jupyter muestra en formato matemático.

%% code prov-08
x + 2

%% code prov-09
x**2 - 2*x - 10

%% md prov-10
Para funciones matemáticas (seno, coseno, raíz cuadrada, exponencial, logaritmo, etc.) **tenés que usar las versiones de SymPy**, no las de `math` ni las de NumPy. Si usás `math.sin(x)` Python intentaría calcular el seno de un símbolo y daría error; SymPy en cambio sabe representar `sy.sin(x)` como una expresión simbólica.

%% code prov-11
sy.sqrt(x) + sy.sin(x) - sy.exp(x)

%% md prov-12
Se pueden declarar varios símbolos a la vez, separando los nombres por espacios (o por comas):

%% code prov-13
p, q, r = sy.symbols("p q r")
p**q + r/q

%% md prov-14
### 2.1 Restricciones sobre los símbolos

A veces conviene decirle a SymPy algo extra sobre un símbolo: que es **entero**, **real** o **positivo**. Esas restricciones le permiten simplificar mejor. Por ejemplo, si $a$ es positivo, SymPy sabe que $\sqrt{a^2} = a$; sin esa información, deja la expresión sin simplificar.

%% code prov-15
n = sy.symbols("n", integer=True)
y = sy.symbols("y", real=True)
a = sy.symbols("a", positive=True)

sy.sqrt(a**2)

%% md prov-16
Las restricciones más usadas son `integer=True`, `real=True`, `positive=True` y `complex=True`. Si no se especifica nada, SymPy asume que el símbolo es complejo (el caso más general).

%% md prov-17
## 3. Manipular expresiones

%% code prov-18
x, y = sy.symbols("x y")
a, b, c = sy.symbols("a b c")

%% md prov-19
### 3.1 Simplificación automática

SymPy simplifica automáticamente las cosas más obvias: combina términos semejantes, cancela sumandos opuestos, y ordena la expresión en una forma canónica.

%% code prov-20
x**2 + 5*x**3 - 10*x**2 - 5*x - 10*(x + 1)

%% md prov-21
### 3.2 Factorizar

La función `sy.factor` intenta escribir una expresión como producto de factores:

%% code prov-22
expr = a*b + a*c
sy.factor(expr)

%% code prov-23
expr = a**2 + 2*a*b + b**2
sy.factor(expr)

%% code prov-24
expr = x**2 - 5*x + 6
sy.factor(expr)

%% md prov-25
### 3.3 Expandir

La operación inversa es `sy.expand`, que distribuye productos y potencias:

%% code prov-26
sy.expand((x - 7)*(x - 3))

%% code prov-27
sy.expand((x + y)**3)

%% md prov-28
### 3.4 Simplificar en general

Para casos más complejos (fracciones racionales, identidades trigonométricas, combinaciones de funciones) está la función general `sy.simplify`. Aplica varias técnicas hasta encontrar una forma más corta.

%% code prov-29
sy.simplify((x**2 - 3*x) / (x**2 + 3*x))

%% code prov-30
sy.simplify(sy.sin(x)**2 + sy.cos(x)**2)

%% md prov-31
`simplify` es cómodo pero puede ser lento en expresiones grandes. Cuando se sabe qué tipo de manipulación se quiere, conviene usar directamente `factor`, `expand` u otras funciones específicas como `sy.trigsimp` (identidades trigonométricas) o `sy.expand_trig` (sumas de ángulos).

%% code prov-32
sy.expand_trig(sy.sin(x + y))

%% md enu-01
### Actividad 1: factorizar y expandir

1. Definí `x` como símbolo (una sola línea).
2. Factorizá la expresión $x^2 - 7x + 12$ con `sy.factor`.
3. Expandí la expresión $(x + 4)^3$ con `sy.expand`.
4. Tomá el resultado del punto 3 y pasáselo a `sy.factor`. ¿Recuperás la expresión original?

%% code act-01
import sympy as sy
sy.init_printing()

# TU CÓDIGO AQUÍ

%% md prov-33
## 4. Sustituir y evaluar

Una expresión simbólica no tiene valor numérico hasta que reemplazás sus símbolos por números. Eso se hace con el método `.subs`, que además sirve para reemplazar un símbolo por otra expresión.

%% md prov-34
### 4.1 Sustitución simbólica

%% code prov-35
expr = sy.cos(x)**2 + sy.sin(x)**2
expr.subs(x, y**2)

%% md prov-36
Importante: `.subs` **no modifica** la expresión original. Devuelve una expresión nueva.

%% code prov-37
expr

%% md prov-38
También se puede sustituir una subexpresión completa, por ejemplo cambiar $\sin(x)$ por $e^x$:

%% code prov-39
expr.subs(sy.sin(x), sy.exp(x))

%% md prov-40
### 4.2 Sustitución numérica

Si el argumento de `.subs` es un número, la expresión se evalúa en ese punto:

%% code prov-41
expr2 = x**2 + 3*x + 1
expr2.subs(x, 2)

%% md prov-42
### 4.3 Pasar a decimal con `.evalf()`

Si el resultado contiene fracciones, raíces o constantes como $\pi$, SymPy lo deja en esa forma exacta. Para obtener un decimal hay que encadenar `.evalf()`, que acepta un argumento opcional con la cantidad de dígitos:

%% code prov-43
sy.sqrt(2).evalf()

%% code prov-44
sy.exp(x).subs(x, 5).evalf(7)

%% md prov-45
### 4.4 Fracciones exactas: `sy.Rational`

Los literales como `1/2` en Python son `float` (aproximación decimal). Si querés preservar la fracción exacta, usá `sy.Rational(numerador, denominador)`:

%% code prov-46
expr = x**2 / 4
expr.subs(x, sy.Rational(3, 2))

%% md prov-47
El resultado queda como $9/16$ en lugar de $0.5625$. Esto importa en cálculos largos donde los errores de redondeo se van acumulando.

%% md prov-48
## 5. Resolver ecuaciones

La función `sy.solve` resuelve ecuaciones y sistemas. Trabaja con expresiones **igualadas a cero**: si querés resolver $x - 3 = 0$, pasás `x - 3` directamente.

%% md prov-49
### 5.1 Ecuación lineal

%% code prov-50
x = sy.symbols("x")
sy.solve(x - 3)

%% md prov-51
El resultado es una **lista** con las soluciones. En este caso, una sola: $x = 3$.

%% md prov-52
### 5.2 Ecuación cuadrática

%% code prov-53
sy.solve(x**2 + 2*x + 2)

%% md prov-54
Esta cuadrática no tiene raíces reales, así que SymPy devuelve las complejas. Notá que aparece `I` con mayúscula: es la unidad imaginaria según SymPy (no `j` como en Python puro).

%% md prov-55
### 5.3 Ecuación con varias incógnitas

Cuando la expresión tiene más de un símbolo, hay que indicarle a `solve` respecto a cuál resolver. Por ejemplo, la fórmula general de la cuadrática $ax^2 + bx + c = 0$:

%% code prov-56
a, b, c = sy.symbols("a b c")
sy.solve(a*x**2 + b*x + c, x)

%% md prov-57
El segundo argumento (`x`) le dice a `solve` que queremos las soluciones en función de `a`, `b` y `c`. Obtenemos las dos raíces de la fórmula resolvente.

%% md prov-58
### 5.4 Sistemas de ecuaciones

Para resolver varias ecuaciones simultáneas, se pasan en una tupla, junto con la tupla de las incógnitas:

$$
\begin{cases}
x + y = 5 \\
x - y = 1
\end{cases}
$$

%% code prov-59
y = sy.symbols("y")
sy.solve((x + y - 5, x - y - 1), (x, y))

%% md prov-60
El resultado es un **diccionario** con los valores que satisfacen las dos ecuaciones.

%% md enu-02
### Actividad 2: divisor de tensión

Un divisor de tensión resistivo cumple

$$V_{out} = \frac{R_2}{R_1 + R_2} \cdot V_{in}$$

Queremos elegir $R_1$ de manera que, con $V_{in} = 12$ V y $R_2 = 1000$ Ω, la salida sea $V_{out} = 5$ V.

1. Definí `R1, R2, Vin, Vout` como símbolos positivos con `sy.symbols("...", positive=True)`.
2. Armá la expresión `ecuacion = Vout - R2*Vin/(R1 + R2)` (igualada a cero).
3. Sustituí los valores conocidos con `.subs({...})` pasando un diccionario.
4. Resolvé para `R1` con `sy.solve(..., R1)`.

%% code act-02
import sympy as sy
sy.init_printing()

# TU CÓDIGO AQUÍ

%% md prov-61
## 6. Derivadas

La función `sy.diff` calcula derivadas simbólicas. Toma al menos dos argumentos: la expresión y la variable respecto a la cual derivar.

%% code prov-62
x = sy.symbols("x")
expr = sy.exp(x) * sy.cos(x)
sy.diff(expr, x)

%% md prov-63
### 6.1 Derivadas de orden superior

Un tercer argumento indica el orden de la derivada. Por ejemplo, la derivada segunda de $5x^2 + 3x - 10$:

%% code prov-64
sy.diff(5*x**2 + 3*x - 10, x, 2)

%% md prov-65
### 6.2 Derivadas parciales

Si la expresión tiene varias variables, `diff` deriva respecto a la que le indiques, tratando las otras como constantes:

%% code prov-66
y, z = sy.symbols("y z")
f = sy.exp(x*y) + sy.sin(z)
sy.diff(f, y)

%% md enu-03
### Actividad 3: energía almacenada en un capacitor

La energía almacenada en un capacitor en función de la tensión aplicada es

$$E(v) = \tfrac{1}{2} \, C \, v^2$$

donde $C$ es la capacidad (una constante del componente) y $v$ la tensión.

1. Definí `C` como símbolo positivo y `v` como símbolo real.
2. Armá la expresión `E = sy.Rational(1, 2) * C * v**2` (usando `sy.Rational` para que $1/2$ quede exacto).
3. Calculá $\dfrac{dE}{dv}$ con `sy.diff`. (Deberías obtener $C \cdot v$, que es la carga almacenada $Q$.)
4. Calculá ahora $\dfrac{d^2 E}{dv^2}$. ¿Qué representa físicamente?

%% code act-03
import sympy as sy
sy.init_printing()

# TU CÓDIGO AQUÍ

%% md prov-67
## 7. Integrales

La función `sy.integrate` calcula integrales simbólicas. Para una **integral indefinida**, se le pasan la expresión y la variable de integración:

%% code prov-68
sy.integrate(x**2 + 3*x - 7, x)

%% md prov-69
SymPy devuelve la primitiva, sin la constante de integración $C$ (asume que el usuario la agrega cuando la necesita).

Para una **integral definida**, la variable se reemplaza por una tupla `(variable, a, b)`:

%% code prov-70
sy.integrate(sy.sin(x), (x, 0, sy.pi))

%% md prov-71
Algunas observaciones:

- `sy.pi` es la constante $\pi$ en versión simbólica (exacta). Distinta de `np.pi`, que es una aproximación en `float`.
- El resultado de la integral definida es **exacto**: $2$ en este caso, sin decimales.
- Si SymPy no encuentra una primitiva en forma cerrada, devuelve la integral sin evaluar.

%% md enu-04
### Actividad 4: carga acumulada en un capacitor

Un capacitor recibe una corriente que crece linealmente con el tiempo:

$$i(t) = I_0 \cdot t \qquad \text{para } 0 \leq t \leq T$$

La carga acumulada es la integral de la corriente:

$$Q = \int_0^{T} i(t)\, dt$$

1. Definí `t` como símbolo real, `I0` como positivo y `T` como positivo.
2. Armá la expresión `i = I0 * t`.
3. Calculá `Q = sy.integrate(i, (t, 0, T))`.
4. Sustituí `I0 = 0.1` (ampere por segundo) y `T = 2` (segundos) con `.subs(...)` y luego `.evalf()` para obtener el valor numérico de la carga en coulombs.

%% code act-04
import sympy as sy
sy.init_printing()

# TU CÓDIGO AQUÍ

%% md prov-72
## 8. Funciones definidas a trozos: `Piecewise`

Algunas funciones cambian de expresión según el intervalo. Por ejemplo:

$$
f(x) = \begin{cases}
x^2 & \text{si } x < 0 \\
\tfrac{1}{10}\,x^3 & \text{si } x \geq 0
\end{cases}
$$

En SymPy se construyen con `sy.Piecewise`, pasando tuplas de la forma `(expresión, condición)`:

%% code prov-73
f = sy.Piecewise(
    (x**2, x < 0),
    (sy.Rational(1, 10) * x**3, x >= 0)
)
f

%% md prov-74
Una vez construida, la función se comporta como cualquier expresión simbólica: se puede sustituir, derivar, integrar.

%% code prov-75
f.subs(x, -2)

%% code prov-76
f.subs(x, 3)

%% md prov-77
## 9. Del símbolo al gráfico: `lambdify`

SymPy es ideal para **obtener** una expresión (una derivada, una integral, una solución). Pero para **graficarla** conviene pasarla al mundo numérico: Matplotlib entiende arrays de NumPy, no expresiones de SymPy.

El puente entre los dos mundos es `sy.lambdify`. Toma una expresión simbólica y devuelve una función numérica de Python, lista para evaluarse sobre un array:

%% code prov-78
import numpy as np
import matplotlib.pyplot as plt

x = sy.symbols("x")
expr = sy.exp(-x/5) * sy.cos(x)

# Convertir a función numérica
g = sy.lambdify(x, expr, "numpy")

# Evaluar sobre un array y graficar
t = np.linspace(0, 20, 500)
plt.plot(t, g(t))
plt.title("exp(-x/5) · cos(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

%% md prov-79
Tres detalles:

- El primer argumento de `lambdify` es el símbolo (o la tupla de símbolos) que va a actuar como variable de entrada.
- El segundo es la expresión a convertir.
- El tercero, `"numpy"`, indica que la función resultante debe usar las implementaciones de NumPy (para que acepte arrays y sea rápida).

A partir de ahí, `g` es una función Python común que se puede evaluar en un número o en un array completo.

%% md enu-05
### Actividad 5: graficar una función y su derivada

Dada la función $f(x) = x^3 - 3x$:

1. Definí `x` como símbolo y armá la expresión `f = x**3 - 3*x`.
2. Calculá la derivada `df` con `sy.diff(f, x)`.
3. Convertí `f` y `df` en funciones numéricas con `sy.lambdify(..., "numpy")`.
4. Creá un array `t = np.linspace(-3, 3, 400)`.
5. Graficá en un mismo gráfico `f(t)` y `df(t)` usando `plt.plot`, con leyendas `"f(x)"` y `"f'(x)"`.
6. Agregá la línea horizontal $y = 0$ con `plt.axhline(0, color="black", linewidth=0.5)` para ver dónde la derivada cambia de signo.

Fijate que donde la derivada cruza el cero, la función $f$ tiene un máximo o un mínimo local.

%% code act-05
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

sy.init_printing()

# TU CÓDIGO AQUÍ

%% md prov-80
## Cierre

Con lo que aprendiste en este módulo ya podés:

- Declarar símbolos con `sy.symbols` y construir expresiones.
- Factorizar, expandir y simplificar con `factor`, `expand`, `simplify`.
- Sustituir y evaluar con `.subs` y `.evalf()`.
- Resolver ecuaciones y sistemas con `sy.solve`.
- Derivar e integrar con `sy.diff` y `sy.integrate`.
- Armar funciones por tramos con `sy.Piecewise`.
- Cruzar al mundo numérico con `sy.lambdify` para graficar con Matplotlib.

SymPy es mucho más amplio que lo que cubrimos acá: tiene soporte para álgebra lineal, series, ecuaciones diferenciales, geometría y más. La documentación oficial está en [docs.sympy.org](https://docs.sympy.org/latest/index.html) y es la mejor fuente cuando necesites algo específico.

Con este módulo terminás la introducción a Python del curso. A partir de acá, los **laboratorios** aplican todo lo que viste (variables, control, funciones, objetos, NumPy, Matplotlib y SymPy) a problemas concretos de señales y sistemas.
