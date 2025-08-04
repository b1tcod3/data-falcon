import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 10 * np.pi, 1000)  # 4 vueltas
r = theta**2  # Espiral de Arquímides

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8, 8), dpi=100)
plt.plot(x, y, 'b-',linewidth=2)
plt.title('Espiral de Arquímedes', size=20, color='black')
plt.axis('equal')  # Igualar escalas de los ejes
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()