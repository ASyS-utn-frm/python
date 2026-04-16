---
prefix: TP1_variable_compleja
source: TP1_variable_compleja.ipynb
---

%% md hdr-01
<center>


<div style="display: flex; justify-content: center;">
    <img src="data:image/jpeg;base64,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" alt="Logo UTN"/>
</div>
</center>
<center>
    <div style="font-family: 'Georgia', serif; font-size: 24px;">
        <p><strong>Ingeniería electrónica. Análisis de Señales y Sistemas</strong></p>
        <!--<p><em>Profesor Mg. Ing. Javier Velez</em></p>-->
    </div>
</center>


%% md prov-01
# 0. Preparativos — importaciones básicas

%% code prov-02
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Configuración de SymPy
sp.init_printing()

%% md prov-03
> 💡 **Tip**  
> En Jupyter podés ejecutar celdas con **Shift + Enter** 



%% md prov-04
# 1. Representaciones y operaciones básicas

Un número complejo puede describirse en:


- Cartesiana  $z = x + jy$ Parte real $x$, parte imaginaria $y$ 
-  Polar $z = r e^{j\theta}$  Módulo $r$, ángulo $\theta$ 
- Trigonométrica  $z = r(\cos\theta + j\sin\theta)$  Igual que la polar, usando la identidad de Euler 

A continuación trabajaremos con un ejemplo guiado 👇


%% md prov-05
### Ejemplo guiado 1 — de cartesiana a polar (paso a paso)

En este ejemplo partiremos del número complejo

\[ z = 3 + 4j \]

1. **Forma cartesiana**.  

   La construimos directamente como `z = 3 + 4j` (recordá que en Python la unidad imaginaria es `j`).

2. **Módulo** `|z|` y **argumento** $	\theta$.  

   *Con NumPy* existen funciones rápidas: `abs(z)` y `np.angle(z)`.

3. **Impresión con formato**.  

   Usaremos *f‑strings* y especificadores `:.2f`, `:.3f`:

   * `:.2f` → número con **2 decimales** (\*.2f ≡ formato float de 2 dígitos).  

   * `:.3f` → número con **3 decimales**.

4. **Conversión simbólica** con **SymPy** para obtener $z = r e^{j	\theta}$ de manera exacta.  

   Aquí aparece `sp.nsimplify`, que intenta convertir un número decimal al racional/raíz exacta correspondiente.


%% code prov-06
z = 3 + 4j           # forma cartesiana
r = abs(z)            # módulo
theta = np.angle(z)   # ángulo (rad)
print(f"z = {z}")
print(f"|z| = {r:.2f}")
print(f"θ   = {theta:.3f} rad")


%% md prov-07
**Nota**  

`abs` es una función built‑in de Python que, para complejos, devuelve el módulo.  

`np.angle` entrega el ángulo en **radianes**.


%% code prov-08
# Ejemplo guiado 1 · parte B — SymPy (representación exacta)
z_sym = sp.nsimplify(z)           # convierte 3+4j → 3 + 4⋅I (exacto)
polar_sym = sp.Abs(z_sym) * sp.exp(sp.I * sp.arg(z_sym))
polar_sym

%% md prov-09
En la salida de arriba SymPy muestra **exactamente** $5 e^{0.927…\,j}$, donde $5$ es \(|z|\) y $0.927…$ el ángulo. `sp.nsimplify` asegura que, si la parte decimal representa un valor racional sencillo, lo muestre como tal (no es imprescindible, pero ayuda a obtener fracciones limpias).

---

%% md enu-01
### Actividad 1

Completá el siguiente código  para:

1. Pedir al usuario (función `input`) los valores de $x$ e $y$.

2. Construir el número complejo $z = x + jy$.

3. Imprimir su módulo y su fase en grados.

4. Mostrar el punto en el plano (usar `plt.scatter`).

%% code act-01
# TU CÓDIGO AQUÍ
# --------------------------------------


%% md prov-10
# 2. Mapeo de curvas

Los **mapeos** (o transformaciones) muestran cómo una función compleja $f$ deforma puntos y curvas del plano $z$ hacia el plano $w$.  

Aquí exploraremos el mapeo de un **círculo unitario** mediante la función  
$$ f(z)=z^2 $$

**Idea clave**  

Si escribimos un punto en forma polar $z = r·e^{j\theta}$, al aplicar $f$ obtenemos  

$f(z)=r^2 e^{j 2\theta}$.

1. El **radio** se **eleva al cuadrado**.

2. El **ángulo** se **duplica**.


## 2.1 Definimos la curva original `C`

Describiremos la curva dada por una semicircunferencia donde $\theta$ varía entre $0$ y $\pi$

Para esto definiremos un vector de numpy llamado `theta` que varía entre $0$ y $\pi$ tomando $500$ puntos. Luego creamos la curva utilizando la expresión ya obtenida.


%% code prov-11
# Definición de la curva original C (círculo unitario)
theta = np.linspace(0, np.pi, 500)      # parámetro θ
C = np.exp(1j * theta)                    # z = e^{jθ}

%% md prov-12
**Explicación del código**
* `np.linspace(a, b, N)` genera N valores equiespaciados desde *a* hasta *b*.
* `1j` es la unidad imaginaria en Python.
* `np.exp(1j*t)` evalúa $e^{j\theta}$ para cada $\theta$.


Grafiquemos la curva original:

%% code prov-13
# Gráfico de la curva original
fig, ax = plt.subplots(figsize=(4,4))
ax.plot(C.real, C.imag)
ax.set_aspect('equal')
ax.set_title('Curva original  $C : |z|=1$')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.grid(True)
plt.show()

%% md prov-14
## 2.2 Aplicamos el mapeo $f(z)=z^2$ a nuestra curva $C$

Para esto elevamos al cuadrado todos los elementos de C

%% code prov-15
C_mapeada = C**2

%% md prov-16
`C_mapeada` contiene la imagen de cada punto de `C` bajo el mapeo `z → z²`

## 2.3 Gráfico comparativo:

%% code prov-17
# Gráfico comparativo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

ax1.plot(C.real, C.imag)
ax1.set_title('Plano z  —  curva C')
ax1.set_aspect('equal'); ax1.grid(True)

ax2.plot(C_mapeada.real, C_mapeada.imag, 'r')
ax2.set_title('Plano w  —  imagen f(C)')
ax2.set_aspect('equal'); ax2.grid(True)

plt.show()

%% md prov-18
El semi círculo pasa a ser un círculo de radio 1 porque |z|=1 ⇒ |z|^2=1.  

El punto $\theta = 0$ en $C$ va a $\theta = 0$ en $f(C)$, pero $\theta = \pi$ va a $\theta = 2\pi$.

En resumen, la semi circunferencia se mapea en una circunferencia completa superponiendo puntos extremos.

%% md enu-02
## 2.4 Actividad   (🌟 puesta en práctica)

En esta actividad vas a **explorar el mapeo de un segmento recto** mediante la función recíproca.

Repetí TODO el proceso presentado anteriormente para:

- **Curva:** segmento rectilíneo que une $z=0$ con $z=1+j$  
- **Función:** $f(z)=1/z$

**Cuidado con la división por cero**  

La función `f(z)=1/z` **no está definida en _z = 0_**.  

Para evitar el error:

* Construí la curva con un parámetro que **empiece en un pequeño ε > 0** (por ejemplo `ε = 1e-3`) en lugar de incluir el punto 0.  

* Otra opción es usar `np.linspace(ε, 1, N, endpoint=True)` tanto para la componente real `x` como para la componente imaginaria `y`.


Sugerencia: 
primero definí el segmento que une el origen con `1 + j`, evitando el punto 0:  
   ```python
   eps = 1e-3                # pequeño desplazamiento
   t = np.linspace(eps, 1, 300)
   C_seg = t + 1j*t          # z(t) = t + j t
   ```


%% md prov-19
1. Define la curva $C$

%% code act-02
# 🔧 TU CÓDIGO AQUÍ


%% md prov-20
2. Grafica el segmento en el plano z.

%% code act-03
# 🔧 TU CÓDIGO AQUÍ


%% md prov-21
3. Aplica el mapeo y crea un gráfico de comparación:

%% code act-04
# 🔧 TU CÓDIGO AQUÍ


%% md prov-22
# 3. Funciones armónicas conjugadas  

Una **función armónica** satisface la ecuación de Laplace  

$$
\nabla^{2}u \;=\; \frac{\partial^{2}u}{\partial x^{2}} +
                 \frac{\partial^{2}u}{\partial y^{2}} = 0.
$$  

Si $$f(z)=u(x,y)+iv(x,y)$$ es **analítica**, entonces  
sus partes real e imaginaria verifican las **ecuaciones de Cauchy‑Riemann (C‑R)**  

$$
\frac{\partial u}{\partial x}= \frac{\partial v}{\partial y},
\qquad
\frac{\partial u}{\partial y}= -\frac{\partial v}{\partial x}.
$$  


Trabajaremos paso a paso con `sympy` y explicaremos cada
función de Python que aparece.

Nuestro objetivo: hallar la conjugada armónica de  

$$
u(x,y)=x^{2}-y^{2}.
$$

Paso 1 – definir símbolos y la función u

%% code prov-23

import sympy as sp
x, y = sp.symbols('x y', real=True)
u = x**2 - y**2
u



%% md prov-24
**Paso 2 – calcular derivadas parciales de $u$**  

Necesitamos $u_x$ y $u_y$ para las ecuaciones C‑R.

%% code prov-25
u_x = sp.diff(u, x)  # derivada parcial de u respecto a x
u_y = sp.diff(u, y) # derivada parcial de u respecto a y
u_x, u_y


%% md prov-26
Resultado:  

$$
u_x = 2x, \qquad u_y = -2y.
$$

Según C‑R la segunda derivada que necesitamos es $v_x = -u_y$ .

**Paso 3 – integrar $v_x$ para obtener una expresión preliminar de $v$.**


%% code prov-27
# v_x = -u_y  ⇒  v_x = 2y
v_x = -u_y
v_provisional = sp.integrate(v_x, x)   # integramos respecto a x
v_provisional


%% md prov-28
La integración introduce una **“constante de integración”** que puede depender solo de *y*, la denotamos $C(y)$:

$$
v(x,y)=2xy + C(y).
$$

**Paso 4 – imponer la otra ecuación C‑R**  

Recordemos que $u_x = v_y$.  Derivemos $v$ respecto a *$y$*:


%% code prov-29
C = sp.Function('C')            # C(y) aún desconocida
v = 2*x*y + C(y)                # expresión general
v_y = sp.diff(v, y)             # v_y  debe igualar u_x = 2x
v_y


%% md prov-30
Obtenemos  :
$$
v_y = 2x + C'(y).
$$  

Para satisfacer $v_y = u_x = 2x$ se requiere $C'(y)=0$ ⇒ **$C(y)=\text{constante}$**.

Podemos tomar la constante 0.  

Así hallamos la **conjugada armónica definitiva**:

$$
\boxed{\,v(x,y) = 2\,x\,y\,}.
$$

**Paso 5 – construir la función analítica**  
$f(z)=u+iv$


%% code prov-31
v_final = 2*x*y                      # constante omitida
f = sp.Matrix([u, v_final])          # solo para mostrar (u,v)
f


%% md prov-32
💡 **Comprobación rápida**  

Podemos expresar $f(z)$ directamente en función de $z=x+iy$:  

$$
f(z)=x^{2}-y^{2}+\,i(2xy)= (x+iy)^{2}=z^{2},
$$

confirmando que efectivamente es analítica.




%% md prov-33
## 3.1 Actividad 


1. Repetí TODO el procedimiento para cada $u(x,y)$:  

   a) $u = e^{x}\cos y$  

   b) $ u = x\,y$

2. Verifica que $u$ y la $v$ hallada satisfacen Laplace y C‑R.  

3. Construye $f(z)=u+iv$ y simplifícala con `sympy.simplify`.

 **Tip SymPy**   

 *Integrar con variable múltiple*  


 `sp.integrate(expr, (x,))`    integra respecto a x
 
 `sp.integrate(expr, (y,))`    integra respecto a y


%% code act-05
# 🔧 TU CÓDIGO AQUÍ

%% md prov-34
# 4. Series de **Taylor** y **Laurent** con SymPy  

Las series de potencias son una herramienta clave para “aproximar” o representar
funciones analíticas.  
En Python, la librería **SymPy** ofrece el método `series()` para generar
tanto series de **Taylor** como de **Laurent**.

Recordemos:  

* **Serie de Taylor** de una función $f(z)$ en torno a $z_0$  
  $$f(z)=\sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}\,(z-z_0)^{\,n}.$$

* **Serie de Laurent** (permite potencias negativas)  
  $$f(z)=\sum_{n=-\infty}^{\infty} a_{n}\,(z-z_0)^{\,n}.$$

A continuación veremos **cómo utilizar** `series()` paso a paso.

Primero debemos importar SymPy y declarar la variable simbólica:


%% code prov-35
import sympy as sp
z = sp.symbols('z')   # variable compleja formal

%% md prov-36
## 4.1 — Serie de Taylor de $e^{z}$ alrededor de $z_0=0$

La sintaxis básica es  

`expr.series(var, point, n)`

- `expr` – expresión simbólica a expandir.

- `var` – variable respecto a la cual se hace la serie.

- `point` – punto de expansión ($z_0$).

- `n` – orden: genera términos hasta $(z-z_0)^{n-1}$.

Por defecto el resultado incluye un término “$O!\bigl(z^{n}\bigr)$” que representa el resto.

%% code prov-37
expr = sp.exp(z)                   # función e^z
taylor = expr.series(z, 0, 6)      # hasta z^5
taylor

%% md prov-38
`series()` nos devuelve  

$$
1 + z + \frac{z^{2}}{2} + \frac{z^{3}}{6} + \frac{z^{4}}{24}
+ \frac{z^{5}}{120} \;+\; O\!\bigl(z^{6}\bigr).
$$

%% md prov-39
## 4.2 Serie de Laurent con `series()`

Para obtener potencias **negativas** necesitamos una expansión
alrededor de una **singularidad** de la función.  

El argumento `n` sigue indicando *cuántos* términos se generan, pero
ahora incluye también los exponentes negativos
$\,z^{-1}, z^{-2},\dots$.

**Ejemplo**  
Sea  

$$
g(z)=\frac{1}{z\,(z-1)}.
$$

Queremos su serie de Laurent alrededor de $z_0 = 0$.


%% code prov-40
g = 1 / (z*(z - 1))

# genera términos desde z^{-1} hasta z^{4} (5 potencias diferentes de 0 en total)
laurent = g.series(z, 0, 5)    # 5 potencias de z en total
laurent

%% md prov-41
La salida incluye el resto  

$$
O\!\bigl(z^{3}\bigr),
$$ 

lo que indica que los términos a partir de $z^{3}$ se omiten:

$$
-\frac{1}{z} - 1 - z - z^2 - z^3 - z^4+ O(z^5).
$$

Notar que los 5 términos de potencias de $z$ distintas de cero que incluye la función `series()` en este caso contiene potencias negativas de $z$.


%% md enu-03
## 4.3 Actividad 4 🚀  

En esta actividad practicarás el uso de **`series()`** para obtener:

1. una **serie de Taylor** de $\cos z$ hasta $z^{6}$,  

   alrededor de $z_0=0$ que incluya los términos hasta $\displaystyle\frac{1}{z^{2}}$.




%% code act-06
# 🔧 TU CÓDIGO AQUÍ


%% md prov-42
2. una **serie de Laurent** de  
   $$
   f(z)=\dfrac{1}{z^2\,(z-2)}
   $$  

    alrededor de $z_0=0$ 

%% code act-07
# 🔧 TU CÓDIGO AQUÍ

%% md prov-43
# 5. Teorema de los **residuos** 

## 5.1 ¿Qué es un **residuo**?

Sea la serie de Laurent de $f(z)$ alrededor de $z_0$:  

$$
f(z)=\sum_{n=-\infty}^{\infty} a_n\,(z-z_0)^{\,n}.
$$  

El **residuo** en $z_0$ es el coeficiente  
$$a_{-1}\;=\;\text{Res}\bigl[f(z),\,z_0\bigr].$$  




## 5.2  Teorema de los residuos  

Si $f$ es analítica en una región $D$ excepto en los polos
$z_1,\dots,z_k$ contenidos dentro de una curva cerrada $C$,
entonces  

$$
\oint_C f(z)\,dz \;=\; j 2\pi 
        \sum_{j=1}^k \text{Res}\!\bigl[f(z),\,z_j\bigr].
$$  

Es decir: **integrar** $f$ sobre $C$ equivale a sumar
los residuos interiores y multiplicar por $j2\pi $.

## 5.3  Cálculo de residuos con SymPy  

`SymPy` ofrece la rutina  
```python
sp.residue(expr, z, z0)
```
Donde:

- `expr` – función simbólica.

- `z` – variable.

- `z0` – punto donde se desea el residuo.

# 5. 4  Ejemplo 

Consideremos integrar la función

$$
f(z)=\frac{z+1}{z\,(z-\tfrac12)^{3}}.
$$
Sobre la trayectoria

$$C:\;|z|=1$$  




* **Polos dentro de $|z|\lt 1$**  

  * $z=0$   (polo simple, orden 1)  

  * $z=\tfrac12$   (polo de **orden 3**)


Analicemos paso a paso.


%% code prov-44
# Importamos SymPy y declaramos la variable simbólica
import sympy as sp
z = sp.symbols('z')

# Definimos la función f(z)
f = (z + 1) / ( z * (z - sp.Rational(1, 2))**3 )
f


%% md prov-45
### Paso 1 — Residuo en $z=0$ (polo simple)


%% code prov-46
res0 = sp.residue(f, z, 0)
res0

%% md prov-47
### Paso 2 — Residuo en $z=\tfrac12$ (polo de orden 3)


%% code prov-48
res05 = sp.residue(f, z, sp.Rational(1, 2))
res05

%% md prov-49
### Paso 3 — Valor de la integral


%% code prov-50
I = sp.I * 2 * sp.pi *  (res0 + res05)
I_simplified = sp.simplify(I)
I_simplified


%% md prov-51
El resultado es  

$$
\boxed{\,I = j2\pi \left(8-8\right)=0.}
$$


%% md prov-52
## 5.5 Actividad

Encontrar el valor de la integral:

$$
\oint_C \frac{z}{(z-1)(z-2)^2} \quad C: |z-2| = \frac{1}{2}
$$

%% code act-08
# 🔧 TU CÓDIGO AQUÍ

%% md prov-53
## ✨ Cierre

Hoy exploraste cómo **Python** puede ser tu aliado para entender
la variable compleja:

* convertiste números complejos entre formas,

* visualizaste mapeos de curvas,

* calculaste funciones armónicas conjugadas,

* obtuviste series y residuos de manera simbólica.


📚 **Siguiente paso:** profundiza practicando los ejercicios y
explora la documentación oficial de **SymPy** y **NumPy**.


© UTN FRM — 2025  

