import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5.0, 5.0, 100)
y = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure(figsize=(10,8))

contour = plt.contourf(X, Y, Z, levels=20, cmap='RdYlBu')
plt.clabel(contour, inline=True, fontsize=8)

plt.contourf(X, Y, Z, levels=20, cmap='RdYlBu', alpha=0.75)
plt.colorbar(contour, label='Intensity')

plt.title('Contour Plot of $Z = \sin(\sqrt{X^2 + Y^2})$')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks(np.arange(-5, 6, 1))
plt.yticks(np.arange(-5, 6, 1))
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')

plt.tight_layout()
plt.show()