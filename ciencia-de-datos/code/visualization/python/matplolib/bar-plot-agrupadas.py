import matplotlib.pyplot as plt
import numpy as np

# datos
categorias = ['Manzanas', 'Naranjas', 'Plátanos','Peras', 'Uvas']
valores_2022 = [20, 35, 30, 35, 27]
valores_2023 = [25, 32, 34, 20, 25]
# posiciones de las barras
x = np.arange(len(categorias))
# ancho de las barras
ancho = 0.35
# crear las barras
fg, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, valores_2022, ancho, label='2022',color='skyblue')
barras2 = ax.bar(x + ancho/2, valores_2023, ancho, label='2023',color='orange')
# añadir etiquetas y título
ax.set_title('Comparación de Frutas por Año',fontsize=16)
ax.set_xlabel('Frutas', fontsize=14)
ax.set_ylabel('ventas(miles)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=12)
# añadir leyenda
ax.legend(fontsize=12)

for barra in barras1:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # 3 puntos verticales de desplazamiento
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

for barra in barras2:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # 3 puntos verticales de desplazamiento
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
# mostrar el gráfico
plt.show()