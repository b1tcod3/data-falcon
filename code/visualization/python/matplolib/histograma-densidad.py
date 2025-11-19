import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

np.random.seed(42)

datos = np.concatenate((np.random.normal(50, 15, 1000), np.random.normal(80, 10, 500)))

plt.figure(figsize=(10, 6))

n, bins, patches = plt.hist(datos, bins=30, density=True, alpha=0.7, color='steelblue', edgecolor='black')

density = gaussian_kde(datos)
xs = np.linspace(min(datos), max(datos), 200)
plt.plot(xs, density(xs), 'r-', linewidth=2)

plt.title('Histograma de Densidad',fontsize=16)
plt.xlabel('Valor', fontsize=14)
plt.ylabel('Densidad', fontsize=14)
plt.grid(axis='y', alpha=0.3)

media = np.mean(datos)
mediana = np.median(datos)
plt.axvline(media, color='green', linestyle='--', label=f'Media: {media:.2f}')
plt.axvline(mediana, color='orange', linestyle='--', label=f'Mediana: {mediana:.2f}')
plt.legend()

plt.tight_layout()
plt.show()