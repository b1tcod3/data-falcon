# Importación de las bibliotecas necesarias:
# numpy para operaciones numéricas y manejo de matrices.
# matplotlib.pyplot para la creación de gráficos.
import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos originales (un triángulo en este caso)
puntos = np.array([[1, 0], [0, 1], [-1, 0]])

# Definir el ángulo de rotación en grados
angulo = 45
theta = np.radians(angulo)  # Convertir a radianes

# Matriz de rotación
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

# Aplicar la transformación
puntos_rotados = puntos @ R.T  # Transponer R para multiplicar correctamente

# Graficar los puntos originales y rotados
plt.figure(figsize=(8, 8))
plt.plot(puntos[:, 0], puntos[:, 1], 'ro-', label='Originales')
plt.plot(puntos_rotados[:, 0], puntos_rotados[:, 1], 'bo-', label='Rotados')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Rotación de {angulo} Grados')
plt.legend()
plt.show()