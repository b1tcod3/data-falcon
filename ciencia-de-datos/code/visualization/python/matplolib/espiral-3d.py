import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 10* np.pi, 1000) 
z = np.linspace(0, 10, 1000)  # Altura de la espiral
r = 1 + 0.1 *  z # Radio que crece con theta

x = r * np.cos(theta)
y = r * np.sin(theta)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z,'g-',label='Espiral 3D', linewidth=2)

ax.set_title('Espiral 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.grid(True)   

plt.show()