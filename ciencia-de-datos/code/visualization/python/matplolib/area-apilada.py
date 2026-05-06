import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
y2 = np.array([1, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plt.figure(figsize=(10, 6))

plt.stackplot(x, y1, y2, y3, labels=['Serie 1', 'Serie 2', 'Serie 3'], colors=['#ff9999','#66b3ff','#99ff99'] ,alpha=0.8)

plt.title('Ventas acumuladas por producto', fontsize=16)
plt.xlabel('Meses', fontsize=14)
plt.ylabel('Ventas (miles)', fontsize=14)
plt.xticks(x, [f'Mes {i}' for i in x])
plt.legend(loc='upper left')

total = y1 + y2 + y3
plt.plot(x, total, linewidth=2, label='Total Ventas')

plt.tight_layout()
plt.show()