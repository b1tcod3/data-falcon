import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch

# Cargar el shape file
shapefile_path = "ven/ven.shp"
gdf = gpd.read_file(shapefile_path)

# Filtrar solo los municipios del estado Falcón
falcon_gdf = gdf[gdf['ADM1_ES'] == 'Falcón'].copy()

# Cargar los datos de votos
datos_votos = pd.read_csv('datos-votos-meta.csv')

# Limpiar los datos de votos
# Eliminar la última fila que no tiene nombre de municipio
datos_votos = datos_votos[:-1]

# Convertir la columna %VOTOS a valores numéricos
datos_votos['%PART'] = datos_votos['%PART'].str.replace('%', '').astype(float)

# Renombrar la columna de municipios para que coincida
datos_votos = datos_votos.rename(columns={'Municipio': 'ADM2_ES'})

# Unir los datos geográficos con los datos de votos
falcon_gdf = falcon_gdf.merge(datos_votos, on='ADM2_ES', how='left')

# Crear una paleta de colores sobria y profesional
# Usaremos una escala de azules y grises
colors = ['#f0f0f0', '#d0d0d0', '#a0a0a0', '#707070', '#404040', '#1a5276', '#2874a6', '#3498db']
n_bins = 100
cmap = LinearSegmentedColormap.from_list('participacion', colors, N=n_bins)

# Crear una figura para el mapa
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Plotear el mapa con los datos de votos
falcon_gdf.plot(column='%PART',
                ax=ax,
                edgecolor='black',
                linewidth=0.8,
                cmap=cmap,
                legend=True,
                legend_kwds={'label': 'Porcentaje de Votos (%)',
                            'orientation': 'horizontal',
                            'shrink': 0.6,
                            'aspect': 40,
                            'pad': 0.05})

# Añadir etiquetas de municipios con un estilo sobrio
for idx, row in falcon_gdf.iterrows():
    nombre_municipio = row['ADM2_ES']
    centroide = row.geometry.centroid
    plt.annotate(text=nombre_municipio, 
                 xy=(centroide.x, centroide.y),
                 horizontalalignment='center',
                 fontsize=8,
                 color='black',
                 fontweight='normal')

# Añadir título con un estilo profesional
ax.set_title('Porcentaje de Votos por Municipio - Estado Falcón', fontsize=18, fontweight='bold', pad=20)
ax.set_axis_off()  # Ocultar ejes

# Añadir una nota sobre la fuente de datos
fig.text(0.5, 0.01, 'Fuente: SALA PSUV', ha='center', fontsize=10, style='italic')

# Guardar el mapa con alta calidad
plt.savefig('mapa_porcentaje_votos_meta.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Mapa guardado como 'mapa_porcentaje_votos_meta.png'")

# Mostrar el mapa
plt.tight_layout()
plt.show()

# Crear un segundo mapa con un enfoque más minimalista
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Plotear el mapa con los datos de votos
falcon_gdf.plot(column='%PART',
                ax=ax,
                edgecolor='black',
                linewidth=0.8,
                cmap=cmap,
                legend=True,
                legend_kwds={'label': 'Porcentaje de Votos (%)',
                            'orientation': 'horizontal',
                            'shrink': 0.6,
                            'aspect': 40,
                            'pad': 0.05})

# Añadir título con un estilo profesional
ax.set_title('Porcentaje de Votos por Municipio - Estado Falcón', fontsize=18, fontweight='bold', pad=20)
ax.set_axis_off()  # Ocultar ejes

# Añadir una nota sobre la fuente de datos
fig.text(0.5, 0.01, 'Fuente: SALA PSUV', ha='center', fontsize=10, style='italic')

# Guardar el mapa minimalista con alta calidad
plt.savefig('mapa_porcentaje_votos_meta_minimalista.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Mapa minimalista guardado como 'mapa_porcentaje_votos_meta_minimalista.png'")

# Mostrar el mapa minimalista
plt.tight_layout()
plt.show()

# Imprimir un resumen de los datos
print("\nResumen de Datos de Votos (Porcentaje):")
print("=" * 50)
print(f"Porcentaje de votos promedio: {falcon_gdf['%PART'].mean():.1f}%")
print(f"Porcentaje de votos máximo: {falcon_gdf['%PART'].max():.1f}% - {falcon_gdf.loc[falcon_gdf['%PART'].idxmax(), 'ADM2_ES']}")
print(f"Porcentaje de votos mínimo: {falcon_gdf['%PART'].min():.1f}% - {falcon_gdf.loc[falcon_gdf['%PART'].idxmin(), 'ADM2_ES']}")

print("\nMunicipios con mayor porcentaje de votos:")
top_votos = falcon_gdf.sort_values('%PART', ascending=False).head(5)
for idx, row in top_votos.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['%PART']:.1f}%")

print("\nMunicipios con menor porcentaje de votos:")
bottom_votos = falcon_gdf.sort_values('%PART', ascending=True).head(5)
for idx, row in bottom_votos.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['%PART']:.1f}%")