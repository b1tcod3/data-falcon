import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# definir la función para el sólido de revolución
def f(x):
    return x**2

a,b = 0, 2  # límites de integración
x = np.linspace(a, b, 100)

# crear malla para la revolución
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# coordenadas cartesianas
Y = f(X)*np.cos(Theta)
Z = f(X)*np.sin(Theta)

# crear la figura y el eje 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', color='cyan', alpha=0.8, edgecolor='none')

ax.set_title('Sólido de Revolución: $y = x^2$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, 2)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
ax.view_init(elev=30, azim=30)  # ajustar la vista

plt.tight_layout()
plt.show()
