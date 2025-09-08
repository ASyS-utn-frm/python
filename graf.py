import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal original
T = 1.0  # Período
omega0 = 2 * np.pi / T  # Frecuencia fundamental
a0_div_2 = 0.5  # Valor medio (componente DC, a_0/2)

# Función para calcular los coeficientes a_k (b_k son 0 para esta señal)
def calculate_ak(k):
    """Calcula el coeficiente a_k para la serie de Fourier de la onda cuadrada."""
    if k == 0:
        # a_0 se maneja a través de a0_div_2. Este a_k es para k >= 1.
        return 0.0
    if k % 2 == 0:  # k par
        return 0.0
    else:  # k impar
        # sin(pi*k/2) es 1 para k=1,5,9,... y -1 para k=3,7,11,...
        # Esto es (-1)**((k-1)/2)
        return (2 / (np.pi * k)) * np.sin(np.pi * k / 2)

# Vector de tiempo para graficar 3 períodos
t_min = -1.5 * T
t_max = 1.5 * T
t = np.linspace(t_min, t_max, 1200, endpoint=False) # Más puntos para suavidad

# Función para la reconstrucción de la serie de Fourier
def fourier_series_reconstruction(t_arr, N_terms):
    """Reconstruye la señal usando N_terms términos de la serie."""
    y = np.full_like(t_arr, a0_div_2) # Inicializa con la componente DC
    for k_val in range(1, N_terms + 1):
        ak_val = calculate_ak(k_val)
        if ak_val != 0: # b_k es 0
            y += ak_val * np.cos(k_val * omega0 * t_arr)
    return y

# --- 1. Reconstrucción con 5 términos ---
N1 = 5
y_reconstructed_N1 = fourier_series_reconstruction(t, N1)

plt.figure(figsize=(10, 6))
plt.plot(t, y_reconstructed_N1, label=f'Reconstrucción con N={N1} términos', color='blue')
plt.title(f'Reconstrucción de la Serie de Fourier (N={N1} Términos)')
plt.xlabel('t (segundos)')
plt.ylabel('x(t)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.savefig('reconstruccion_N5.png')
plt.show()

# --- 2. Componentes para la serie truncada de 5 términos ---
plt.figure(figsize=(12, 7))
# Componente DC
y_dc = np.full_like(t, a0_div_2)
plt.plot(t, y_dc, label=r'$a_0/2 = 0.5$ (DC)', linestyle='--', color='black')

# Colores para las componentes AC
colors_N1 = plt.cm.viridis(np.linspace(0, 0.9, sum(1 for k_ in range(1, N1 + 1) if calculate_ak(k_) != 0)))
color_idx = 0

for k_val in range(1, N1 + 1):
    ak_val = calculate_ak(k_val)
    if ak_val != 0:
        component = ak_val * np.cos(k_val * omega0 * t)
        # Formatear la etiqueta del coeficiente para legibilidad
        term_label = rf'$a_{k_val}\cos({k_val}\omega_0 t)$'
        if k_val == 1: term_label = rf'$\frac{{2}}{{\pi}}\cos(\omega_0 t)$'
        elif k_val == 3: term_label = rf'$-\frac{{2}}{{3\pi}}\cos(3\omega_0 t)$'
        elif k_val == 5: term_label = rf'$\frac{{2}}{{5\pi}}\cos(5\omega_0 t)$'
        
        plt.plot(t, component, label=term_label, color=colors_N1[color_idx])
        color_idx += 1

plt.title(f'Componentes de la Serie Truncada (N={N1} Términos) - 3 Períodos')
plt.xlabel('t (segundos)')
plt.ylabel('Amplitud de Componente')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('componentes_N5.png')
plt.show()

# --- 3. Reconstrucción con 30 términos ---
N2 = 30
y_reconstructed_N2 = fourier_series_reconstruction(t, N2)

plt.figure(figsize=(10, 6))
plt.plot(t, y_reconstructed_N2, label=f'Reconstrucción con N={N2} términos', color='purple')
plt.title(f'Reconstrucción de la Serie de Fourier (N={N2} Términos)')
plt.xlabel('t (segundos)')
plt.ylabel('x(t)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.savefig('reconstruccion_N30.png')
plt.show()

# --- 4. Componentes para la serie truncada de 30 términos ---
plt.figure(figsize=(15, 8))
# Componente DC
plt.plot(t, y_dc, label=r'$a_0/2 = 0.5$ (DC)', linestyle='--', color='black')

# Colores para las componentes AC (usar un ciclo de colores más grande si es necesario)
num_ac_components_N2 = sum(1 for k_ in range(1, N2 + 1) if calculate_ak(k_) != 0)
if num_ac_components_N2 > 10: # Matplotlib default cycle is 10. Using tab20 if more.
    try:
        colors_N2 = plt.cm.get_cmap('tab20', num_ac_components_N2).colors
    except AttributeError: # Older Matplotlib
        colors_N2 = [plt.cm.get_cmap('tab20')(i/num_ac_components_N2) for i in range(num_ac_components_N2)]

else:
    colors_N2 = plt.rcParams['axes.prop_cycle'].by_key()['color']

color_idx = 0
max_components_to_label_individually = 5 # Para no saturar la leyenda

for k_val in range(1, N2 + 1):
    ak_val = calculate_ak(k_val)
    if ak_val != 0:
        component = ak_val * np.cos(k_val * omega0 * t)
        current_color = colors_N2[color_idx % len(colors_N2)]
        if color_idx < max_components_to_label_individually or k_val % 5 == 0 : # Etiquetar las primeras y algunas representativas
             term_label = rf'$a_{k_val}\cos({k_val}\omega_0 t)$'
             plt.plot(t, component, label=term_label, color=current_color)
        else:
             plt.plot(t, component, color=current_color) # Sin etiqueta para no saturar
        color_idx += 1

plt.title(f'Componentes de la Serie Truncada (N={N2} Términos) - 3 Períodos')
plt.xlabel('t (segundos)')
plt.ylabel('Amplitud de Componente')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(loc='upper right', ncol=2) # Leyenda en múltiples columnas si es necesario
plt.grid(True)
plt.savefig('componentes_N30.png')
plt.show()