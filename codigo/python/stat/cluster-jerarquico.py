from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

# dataset de vinos
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df.columns = ['Class']+[f'Feature_{i}' for i in range(1, 14)]

# Normalizar los datos
X = df.drop('Class', axis=1)
X_scaled = StandardScaler().fit_transform(X)

# Calcular el linkage
Z = linkage(X_scaled, method='ward')

# Graficar el dendrograma
plt.figure(figsize=(16, 8))

dendrogram(Z,
           truncate_mode='lastp',
           p=12,
           show_leaf_counts=True,
           leaf_rotation=90,
           leaf_font_size=10,
           show_contracted=True
)

df['Cluster'] = fcluster(Z, t=15, criterion='distance')
# analisis de clusters
cluster_stats = df.groupby('Cluster').agg(['mean', 'std', 'count'])
print(cluster_stats)

plt.title('Dendrograma del clustering jerárquico')
plt.xlabel('Índice de muestra')
plt.ylabel('Distancia')
plt.axhline(y=15, color='r', linestyle='--')  # Línea horizontal para el corte
plt.show()




