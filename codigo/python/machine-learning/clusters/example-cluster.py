from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (ingresos vs gastos)
X = np.array([[1000, 2000], [1500, 2500], [2000, 3000],
              [3000, 4000], [3500, 4500], [4000, 5000],
              [5000, 6000], [5500, 6500], [6000, 7000],
              [7000, 8000], [7500, 8500], [8000, 9000]])

# Crear el modelo KMeans
kmeans = KMeans(n_clusters=2)
# Ajustar el modelo a los datos
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizar los resultados
colors = ['g.', 'r.']

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=15)

plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', c='black',s=150)
plt.xlabel('Ingresos')
plt.ylabel('Gastos')
plt.title('Clusters de Ingresos y Gastos')
plt.grid(True)
plt.show()
