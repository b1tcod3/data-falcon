# importamos las librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos Iris
# Este conjunto de datos es ideal para funciones de clasificación y agrupamiento
iris = load_iris() 
X = iris.data  # Características
y = iris.target  # Etiquetas de clase


# Proceso 1. Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Proceso 2,3,4,5. Aplicar PCA y transformar los datos
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Proceso 5. Crear un DataFrame para los datos transformados
df = pd.DataFrame(data=X_pca, columns=['Componente 1', 'Componente 2'])
df['Clase'] = iris.target

# Graficar
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['Componente 1'], df['Componente 2'], c=df['Clase'], cmap='viridis')
plt.title('PCA de Iris Dataset')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.colorbar(scatter, label='Clase')
plt.grid()
plt.show()


