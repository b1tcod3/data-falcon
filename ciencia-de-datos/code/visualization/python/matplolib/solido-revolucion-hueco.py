import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def f_outer(x):
    return np.sqrt(x)+1
def f_inner(x):
    return np.sqrt(x)

a, b = 1, 4  # límites de integración

theta = np.linspace(0, 2 * np.pi, 50)
x = np.linspace(a, b, 100)
X, Theta = np.meshgrid(x, theta)

# coordenadas cartesianas para el sólido exterior
Y_outer = f_outer(X) * np.cos(Theta)
Z_outer = f_outer(X) * np.sin(Theta)

# coordenadas cartesianas para el sólido interior
Y_inner = f_inner(X) * np.cos(Theta)
Z_inner = f_inner(X) * np.sin(Theta)

# crear la figura y el eje 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
# dibujar el sólido exterior    8, edgecolor='none')8, edgecolor='none')
ax.plot_surface(X, Y_inner, Z_inner, color='red', alpha=0.5, edgecolor='none')
# dibujar el sólido interior8, edgecolor='none')
ax.plot_surface(X, Y_outer, Z_outer, color='blue', alpha=0.5, edgecolor='none')

# tapas
for x_val in [a, b]:
    
    theta = np.linspace(0, 2 * np.pi, 50)
    r_outer = np.full_like(theta, f_outer(x_val))
    r_inner = np.full_like(theta, f_inner(x_val))
    
    Y_outer_cap = r_outer * np.cos(theta)
    Z_outer_cap = r_outer * np.sin(theta)
    
    Y_inner_cap = r_inner * np.cos(theta)
    Z_inner_cap = r_inner * np.sin(theta)
    
    ax.plot(np.full_like(theta, x_val), Y_outer_cap, Z_outer_cap, 'b-', alpha=0.7)
    ax.plot(np.full_like(theta, x_val), Y_inner_cap, Z_inner_cap, 'r-', alpha=0.7)

ax.set_title('Sólido de Revolución Hueco')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1
ax.view_init(elev=20, azim=30)
plt.show()