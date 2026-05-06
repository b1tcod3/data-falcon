# 1. Importar las bibliotecas necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Cargar el conjunto de datos Iris
iris = sns.load_dataset('iris')

# 3. Mostrar las primeras filas del conjunto de datos
print("Primeras filas del conjunto de datos Iris:")
print(iris.head())

# 4. Calcular la matriz de covarianza
cov_matrix = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].cov()

# Mostrar la matriz de covarianza
print("\nMatriz de Covarianza:")
print(cov_matrix)

# 5. Visualizar la matriz de covarianza utilizando un heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cov_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Covarianza de las Características de Iris')
plt.show()