import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
np.random.seed(42)
grupo_a = np.random.normal(50,10,100)
grupo_b = np.random.normal(70,15,100)
grupo_c = np.random.normal(40,5,100)
grupo_d = np.random.normal(8,8,100)

datos = [grupo_a, grupo_b, grupo_c, grupo_d]
etiquetas = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']
# Crear el box plot
plt.figure(figsize=(10, 6))

bp = plt.boxplot(datos, labels=etiquetas, patch_artist=True)

#colores personalizados
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
# Personalizar el box plot
for i, grupo in enumerate(datos):
    x = np.random.normal(i + 1, 0.04, size=len(grupo))  # Añadir un poco de ruido para la separación
    plt.scatter(x, grupo, alpha=0.5, color='darkblue', s=30)

plt.title('Distribución de Datos por Grupo')
plt.ylabel('Valores')
plt.grid(axis='y', alpha=0.3)

plt.show()
