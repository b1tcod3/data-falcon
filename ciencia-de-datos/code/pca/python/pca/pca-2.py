# importamos las librerias necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Cargamos el dataset Iris
df = sns.load_dataset('iris')

# estadarización de los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('species', axis=1))

# Creamos el objeto PCA y ajustamos los datos
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)
# Creamos un DataFrame con los componentes principales
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
df_pca['species'] = df['species']

# Visualizamos los resultados
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PC1', y='PC2', hue='species', data=df_pca, palette='viridis', s=100)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Species')

# vectores de caracteristicas
feature_vectores = pca.components_.T * np.sqrt(pca.explained_variance_)
for i, feature in enumerate(df.columns[:-1]):
    plt.arrow(0, 0, feature_vectores[i, 0], feature_vectores[i, 1], 
              color='r', alpha=0.5, head_width=0.05, head_length=0.5)
    plt.text(feature_vectores[i, 0] * 1.1, feature_vectores[i, 1] * 1.1, feature, 
             color='darkred', ha='center', va='center', fontsize=12)
plt.grid()
plt.show()