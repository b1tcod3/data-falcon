import matplotlib.pyplot as plt
import numpy as np

# Parámetros de la espiral cuadrada
x, y = [0], [0]
steps = 1
direccion = 0  # 0: derecha, 1: arriba, 2: izquierda, 3: abajo
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(50):
    dx, dy = directions[direccion]
    for _ in range(steps):
        x.append(x[-1]+dx)
        y.append(y[-1]+dy)
    direccion = (direccion + 1) % 4
    if i % 2 == 0:
        steps += 1

plt.figure(figsize=(8, 8))
plt.plot(x, y, 'm-o', markersize=4, linewidth=2, label='Espiral Cuadrada')
plt.title('Espiral Cuadrada')
plt.axis('equal')
plt.grid(alpha=0.3)

plt.show()