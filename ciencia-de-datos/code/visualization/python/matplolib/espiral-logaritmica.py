import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 10* np.pi, 1000) 
a = 0.1  # Parámetro de la espiral logarítmica
r = np.exp(a*theta)  # Espiral logarítmica

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8, 8), dpi=100)
plt.plot(x, y, 'b-',linewidth=2)
plt.title('Espiral de logaritmica', size=20, color='black')
plt.axis('equal')  # Igualar escalas de los ejes
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()