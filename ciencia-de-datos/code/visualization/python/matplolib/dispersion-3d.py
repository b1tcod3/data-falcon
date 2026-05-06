import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Datos de ejemplo
np.random.seed(42)
n = 100
x = np.random.normal(50, 15, n)
y = np.random.normal(30, 10, n)
z = np.random.normal(70, 5, n)

colores = np.sqrt(x**2 + y**2 + z**2)  # Colores basados en la distancia al origen
tamaños = np.random.uniform(20, 200, n)  # Tamaños

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# grafico de dispersión 3D
scatter = ax.scatter(x, y, z, c=colores, s=tamaños, alpha=0.7, cmap='viridis',edgecolor='k')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Gráfico de Dispersión 3D',fontsize=16)

# Barra de color
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Color basado en la distancia al origen', rotation=270, labelpad=15)

ax.view_init(elev=25, azim=45)  # Ajustar la vista

plt.tight_layout()
plt.show()