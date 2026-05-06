import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

datos = np.random.rand(10, 12)

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
productos = [f'Producto {i+1}' for i in range(10)]

fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(datos, cmap='viridis')

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Valor', rotation=-90, va="bottom")

# Etiquetas de los ejes
ax.set_xticks(np.arange(len(meses)))
ax.set_xticklabels(meses)
ax.set_yticks(np.arange(len(productos)))
ax.set_yticklabels(productos)
# Rotar etiquetas del eje x
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Añadir etiquetas a las celdas
for i in range(len(productos)):
    for j in range(len(meses)):
        text = ax.text(j, i, f'{datos[i, j]:.2f}', ha='center', va='center', color='w')
ax.set_title('Mapa de Calor de Productos por Mes',fontsize=16)

ax.set_xlabel('Meses')
ax.set_ylabel('Productos')
ax.grid(False)
# Ajustar el layout para evitar superposiciones
plt.tight_layout()
plt.show()