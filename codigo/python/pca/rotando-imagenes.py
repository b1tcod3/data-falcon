# 1. Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces

# 2. Preparar los datos

# Cargar el conjunto de datos de caras con aleatorización
data = fetch_olivetti_faces(shuffle=True, random_state=42)  

X = data.data  # Matriz de características
y = data.target  # Etiquetas de las imágenes

n_faces = 10  # Seleccionar un subconjunto de imágenes
faces = X[:n_faces]

# 3. Cálculo de la Matriz de Covarianza

cov_matrix = np.cov(faces, rowvar=False)  # Calcular la matriz de covarianza sin transponer

# 4. Cálculo de Valores y Vectores Propios

# Obtener valores y vectores propios
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)  # Usar eigh para matrices simétricas

# Ordenar los vectores propios por su valor propio
sorted_indices = np.argsort(eigenvalues)[::-1]  # Ordenar de mayor a menor
eigenvectors_sorted = eigenvectors[:, sorted_indices]

# 5. Proyección y Rotación
# Proyectar las imágenes en el nuevo espacio
n_components = 2  # Número de componentes principales
projected_faces = faces @ eigenvectors_sorted[:, :n_components]

# Crear una matriz de rotación para el espacio proyectado
theta = np.radians(45)  # Rotar 45 grados
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

# Rotar las imágenes proyectadas
rotated_faces = projected_faces @ rotation_matrix

# Invertir la rotación
inverse_rotation_matrix = np.linalg.inv(rotation_matrix)
reconstructed_faces = rotated_faces @ inverse_rotation_matrix.T

# Proyectar de vuelta al espacio original
reconstructed_faces_original_space = reconstructed_faces @ eigenvectors_sorted[:, :n_components].T

# Visualizar las caras reconstruidas
fig, axes = plt.subplots(2, n_faces, figsize=(15, 6))
for i in range(n_faces):
    # Mostrar cara original
    axes[0, i].imshow(faces[i].reshape(64, 64), cmap='gray')
    axes[0, i].axis('off')
    
    # Mostrar cara reconstruida
    axes[1, i].imshow(reconstructed_faces_original_space[i].reshape(64, 64), cmap='gray')
    axes[1, i].axis('off')

axes[0, 0].set_ylabel('Originales')
axes[1, 0].set_ylabel('Reconstruidas')
plt.show()