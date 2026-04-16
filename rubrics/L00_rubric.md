# Rúbrica — Laboratorio 0: Práctica integradora de Python

**Notebook evaluado:** `L00_practica_python.ipynb`
**Celdas a corregir:** todas las `act-*` (ver `docs/FORMATO_CELDAS.md`).
**Puntaje total:** 100 puntos.

---

## Criterios generales (aplican a todas las actividades)

- La celda **debe ejecutarse sin errores** al correr el notebook de arriba a abajo después de un *Restart*.
- Los resultados impresos deben ser **numéricamente correctos** (con tolerancia razonable por redondeo).
- Código legible: nombres de variables descriptivos, sin código muerto.
- Si la celda usa Matplotlib: título, etiquetas en ambos ejes, grilla.

**Descuentos transversales:**

- Celda con error de ejecución que impide correr las siguientes: −100 % de los puntos de esa actividad y de todas las que dependan de ella.
- `# TU CÓDIGO AQUÍ` sin borrar junto a código real: −10 % de la actividad.

---

## Actividad 1 — Longitud de onda (8 pts)

**Solución de referencia:**

```python
c = 3e8
lambda_am = c / 900e3       # ≈ 333.33 m
lambda_fm = c / 100e6       # = 3.00 m
lambda_wifi = c / 2.4e9     # ≈ 0.125 m
print(f"AM:   λ = {lambda_am:.2f} m")
print(f"FM:   λ = {lambda_fm:.2f} m")
print(f"WiFi: λ = {lambda_wifi:.2f} m")
```

**Puntaje:**

- [2 pts] Usa `c = 3e8` o equivalente (`3 * 10**8`).
- [4 pts] Los tres valores numéricos son correctos (333.33 m, 3.00 m, ~0.125 m).
- [2 pts] Imprime los tres resultados con f-strings y formato numérico.

**Errores comunes:**

- Confundir MHz con Hz (faltar el factor 1e6): −3 pts.
- Usar el nombre `lambda` a secas (es palabra reservada): error de ejecución.

---

## Actividad 2 — Frecuencias de una melodía (10 pts)

**Solución de referencia:**

```python
notas = {
    "Do": 261.63, "Re": 293.66, "Mi": 329.63, "Fa": 349.23,
    "Sol": 392.00, "La": 440.00, "Si": 493.88,
}
frecuencias = [notas[n] for n in melodia]
print(frecuencias)
```

**Puntaje:**

- [3 pts] Diccionario `notas` con las 7 notas correctamente.
- [5 pts] Obtiene la lista de frecuencias correctamente (7 elementos, en orden correcto).
- [2 pts] Imprime el resultado.

**Alternativas aceptadas:**

- Bucle `for` con `.append()` en lugar de comprensión: equivalente.

---

## Actividad 3 — Clasificar frecuencias por banda (12 pts)

**Solución de referencia:**

```python
for f in frecuencias:
    if 3e6 <= f < 30e6:
        banda = "HF"
    elif 30e6 <= f < 300e6:
        banda = "VHF"
    elif 300e6 <= f < 3e9:
        banda = "UHF"
    else:
        banda = "?"
    print(f"{f} Hz → {banda}")

vhf = [f for f in frecuencias if 30e6 <= f < 300e6]
print(vhf)
```

**Puntaje:**

- [6 pts] Clasificación correcta de las 7 frecuencias (1 pt cada una, redondeando a favor).
- [3 pts] Usa `if/elif/else` (no tres `if` separados).
- [3 pts] La comprensión final devuelve exactamente `[88e6, 145e6]`.

**Clasificación correcta esperada:**

| Frecuencia | Banda |
|------------|-------|
| 5 MHz   | HF  |
| 27 MHz  | HF  |
| 88 MHz  | VHF |
| 145 MHz | VHF |
| 433 MHz | UHF |
| 915 MHz | UHF |
| 2.4 GHz | UHF |

---

## Actividad 4 — Tres funciones encadenadas (12 pts)

**Solución de referencia:**

```python
def fc_rc(R, C):
    return 1 / (2 * np.pi * R * C)

def ganancia_db(v_in, v_out):
    return 20 * np.log10(v_out / v_in)

def ganancia_total_db(g1_db, g2_db):
    return g1_db + g2_db

print(f"fc = {fc_rc(R=10e3, C=100e-9):.2f} Hz")       # ≈ 159.15 Hz
print(f"G = {ganancia_db(1, 10):.2f} dB")              # = 20.00 dB
print(f"G_tot = {ganancia_total_db(20, 6):.2f} dB")    # = 26.00 dB
```

**Puntaje:**

- [3 pts] `fc_rc` correcta (acepta $1/(2\pi RC)$).
- [3 pts] `ganancia_db` correcta (20 · log10 de la relación).
- [3 pts] `ganancia_total_db` simplemente suma.
- [3 pts] Los tres valores impresos son correctos.

**Errores comunes:**

- Confundir `log10` con `log` (natural): `ganancia_db(1, 10)` daría ≈ 46 en lugar de 20. −3 pts.
- Usar `10 * log10(...)` (fórmula de potencia) en vez de `20 * log10(...)` (fórmula de tensión). −2 pts.

---

## Actividad 5 — Clase `Bateria` (12 pts)

**Solución de referencia:**

```python
class Bateria:
    def __init__(self, capacidad_ah, tension):
        self.capacidad_ah = capacidad_ah
        self.tension = tension

    def energia_wh(self):
        return self.capacidad_ah * self.tension

    def autonomia(self, corriente_a):
        return self.capacidad_ah / corriente_a

b1 = Bateria(capacidad_ah=60, tension=12)
b2 = Bateria(capacidad_ah=4, tension=3.7)
print(f"b1: {b1.energia_wh()} Wh, {b1.autonomia(0.5)} h")
print(f"b2: {b2.energia_wh()} Wh, {b2.autonomia(0.5)} h")
```

**Puntaje:**

- [3 pts] Definición correcta de `__init__` con los dos atributos.
- [3 pts] `energia_wh()` devuelve `capacidad_ah * tension`.
- [3 pts] `autonomia(corriente_a)` devuelve `capacidad_ah / corriente_a`.
- [3 pts] Crea las dos instancias e imprime los 4 valores (energía y autonomía de cada una).

**Valores esperados:**

- `b1`: 720 Wh, 120 h.
- `b2`: 14.8 Wh, 8 h.

---

## Actividad 6 — Tono DTMF tecla "5" + RMS (12 pts)

**Solución de referencia:**

```python
fs = 8000
duracion = 0.05
t = np.linspace(0, duracion, int(duracion * fs))
x = np.sin(2 * np.pi * 770 * t) + np.sin(2 * np.pi * 1336 * t)
x_rms = np.sqrt(np.mean(x ** 2))
print(f"RMS: {x_rms:.2f}")   # ≈ 1.00
```

**Puntaje:**

- [2 pts] `fs = 8000`, `duracion = 0.05`.
- [2 pts] `t` armado con `np.linspace` y cantidad entera de puntos.
- [4 pts] `x` es la suma de dos senoidales con las frecuencias correctas (770 y 1336 Hz).
- [2 pts] RMS calculado correctamente con `np.sqrt(np.mean(x**2))`.
- [2 pts] Imprime el RMS con formato razonable.

**Errores comunes:**

- Olvidar el `2*np.pi` en el argumento del seno: la frecuencia queda mal. −4 pts.
- Olvidar el `int(...)` en `linspace`: error `TypeError`. −2 pts.

---

## Actividad 7 — Tres señales en subplots (12 pts)

**Solución de referencia:**

```python
t = np.linspace(0, 0.02, 500)
x1 = np.exp(50 * t)
pulsos = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])
n = np.arange(10)
x3 = np.exp(-100 * t) * np.cos(2 * np.pi * 200 * t)

fig, axs = plt.subplots(3, 1, figsize=(9, 7))
axs[0].plot(t, x1)
axs[0].set_title("Exponencial creciente")
axs[0].set_ylabel("x1")
axs[0].grid(True)
axs[1].stem(n, pulsos)
axs[1].set_title("Tren de pulsos digitales")
axs[1].set_ylabel("bit")
axs[1].grid(True)
axs[2].plot(t, x3)
axs[2].set_title("Senoidal amortiguada")
axs[2].set_xlabel("Tiempo [s]")
axs[2].set_ylabel("x3")
axs[2].grid(True)
plt.tight_layout()
plt.show()
```

**Puntaje:**

- [3 pts] Tres paneles en una figura (`subplots(3, 1, ...)`).
- [3 pts] Señales calculadas correctamente (exp creciente, pulsos, exp decreciente × cos).
- [2 pts] Usa `stem` para los pulsos (no `plot`).
- [2 pts] Cada panel tiene título, ylabel y grilla; el de abajo tiene xlabel.
- [2 pts] `tight_layout()` incluido.

**Errores comunes:**

- Usar `plot` para los pulsos: −2 pts.
- Olvidar el `2*np.pi` en la senoidal amortiguada: se ve muy rápido o muy lento. −1 pt.

---

## Actividad 8 — Despejar $C$ con SymPy (10 pts)

**Solución de referencia:**

```python
R, C, fc = sp.symbols("R C fc", positive=True)
ec = sp.Eq(fc, 1 / (2 * sp.pi * R * C))
sol = sp.solve(ec, C)
print(sol[0])                                  # 1/(2*pi*R*fc)

C_val = float(sol[0].subs({fc: 1000, R: 10000}).evalf())
print(f"C = {C_val:.2e} F")                    # ≈ 1.59e-08 F
print(f"C = {C_val * 1e9:.2f} nF")             # ≈ 15.92 nF
```

**Puntaje:**

- [2 pts] Define los símbolos con `sp.symbols`.
- [2 pts] Escribe la ecuación con `sp.Eq(...)`.
- [2 pts] Despeja `C` con `sp.solve(...)`.
- [2 pts] Sustituye valores numéricos con `.subs(...)` y `.evalf()`.
- [2 pts] Imprime el valor en nanofarads (≈ 15.92 nF).

---

## Integrador — Detector DTMF (12 pts)

**Solución de referencia:**

```python
mapa_teclas = {
    "1": (697, 1209), "2": (697, 1336), "3": (697, 1477),
    "4": (770, 1209), "5": (770, 1336), "6": (770, 1477),
    "7": (852, 1209), "8": (852, 1336), "9": (852, 1477),
    "*": (941, 1209), "0": (941, 1336), "#": (941, 1477),
}

errores = []
for tecla, (f_fila, f_col) in mapa_teclas.items():
    x_teorico = np.sin(2 * np.pi * f_fila * t) + np.sin(2 * np.pi * f_col * t)
    mse = np.mean((x_misterio - x_teorico) ** 2)
    errores.append((tecla, mse))

detectada, mse = min(errores, key=lambda par: par[1])
print(f"Tecla detectada: {detectada}")
print(f"MSE: {mse:.4e}")
print(f"¿Acerté? Tecla real: {tecla_elegida}")

# Bonus gráfico
mask = t < 0.01
x_teorica_det = np.sin(2 * np.pi * mapa_teclas[detectada][0] * t) + \
                np.sin(2 * np.pi * mapa_teclas[detectada][1] * t)
fig, axs = plt.subplots(2, 1, figsize=(9, 5))
axs[0].plot(t[mask], x_misterio[:mask.sum()])
axs[0].set_title("x_misterio")
axs[0].grid(True)
axs[1].plot(t[mask], x_teorica_det[:mask.sum()])
axs[1].set_title(f"Teórica (tecla {detectada})")
axs[1].set_xlabel("Tiempo [s]")
axs[1].grid(True)
plt.tight_layout()
plt.show()
```

**Puntaje:**

- [2 pts] Diccionario `mapa_teclas` correcto (12 entradas).
- [3 pts] Bucle que recorre el diccionario y genera cada señal teórica.
- [2 pts] Calcula MSE con `np.mean((x_misterio - x_teorico) ** 2)`.
- [2 pts] Encuentra el mínimo con `min(..., key=lambda ...)` u otra vía equivalente (p. ej. `sorted(...)[0]`).
- [1 pt] Imprime la tecla detectada y compara con `tecla_elegida`.
- [2 pts] Gráfico comparativo con los dos paneles (arriba `x_misterio`, abajo teórica).

**Criterio de éxito:** la tecla detectada debe coincidir con `tecla_elegida`. Con la semilla provista (`seed=42`), la tecla real es `"2"`. Si el detector devuelve algo distinto, revisar la fórmula del MSE o el diccionario.

**Bonus (no obligatorio, suma hasta +5):**

- Calcular el MSE usando **comprensión de diccionario** en vez de bucle explícito.
- Normalizar el error por el MSE mínimo (ver cuánto más grande es el MSE del segundo candidato — gives información sobre la robustez de la detección).

---

## Tabla resumen

| Actividad | Puntaje | Depende de |
|-----------|---------|------------|
| 1. Longitud de onda | 8 | — |
| 2. Notas musicales | 10 | — |
| 3. Bandas de radio | 12 | — |
| 4. Funciones | 12 | — |
| 5. Clase `Bateria` | 12 | — |
| 6. DTMF tecla "5" + RMS | 12 | — |
| 7. Subplots | 12 | — |
| 8. SymPy | 10 | (Act 4 como referencia conceptual) |
| 9. Integrador DTMF | 12 | Act 6 (conceptualmente) |
| **Total** | **100** | |
