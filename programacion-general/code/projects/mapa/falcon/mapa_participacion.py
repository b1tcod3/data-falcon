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

# Cargar los datos de participación
datos_participacion = pd.read_csv('datos-participacion.csv')

# Limpiar los datos de participación
# Eliminar la última fila que no tiene nombre de municipio
datos_participacion = datos_participacion[:-1]

# Convertir la columna %PART a valores numéricos
datos_participacion['%PART'] = datos_participacion['%PART'].str.replace('%', '').astype(float)

# Renombrar la columna de municipios para que coincida
datos_participacion = datos_participacion.rename(columns={'Municipio': 'ADM2_ES'})

# Unir los datos geográficos con los datos de participación
falcon_gdf = falcon_gdf.merge(datos_participacion, on='ADM2_ES', how='left')

# Crear una paleta de colores sobria y profesional
# Usaremos una escala de azules y grises
colors = ['#f0f0f0', '#d0d0d0', '#a0a0a0', '#707070', '#404040', '#1a5276', '#2874a6', '#3498db']
n_bins = 100
cmap = LinearSegmentedColormap.from_list('participacion', colors, N=n_bins)

# Crear una figura para el mapa
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Plotear el mapa con los datos de participación
falcon_gdf.plot(column='%PART',
                ax=ax,
                edgecolor='black',
                linewidth=0.8,
                cmap=cmap,
                legend=True,
                legend_kwds={'label': 'Porcentaje de Participación (%)',
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
ax.set_title('Participación Electoral por Municipio - Estado Falcón', fontsize=18, fontweight='bold', pad=20)
ax.set_axis_off()  # Ocultar ejes

# Añadir una nota sobre la fuente de datos
fig.text(0.5, 0.01, 'Fuente: datos-participacion.csv', ha='center', fontsize=10, style='italic')

# Guardar el mapa con alta calidad
plt.savefig('mapa_participacion.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Mapa guardado como 'mapa_participacion.png'")

# Mostrar el mapa
plt.tight_layout()
plt.show()

# Crear un segundo mapa con un enfoque más minimalista
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Plotear el mapa con los datos de participación
falcon_gdf.plot(column='%PART',
                ax=ax,
                edgecolor='black',
                linewidth=0.8,
                cmap=cmap,
                legend=True,
                legend_kwds={'label': 'Porcentaje de Participación (%)',
                            'orientation': 'horizontal',
                            'shrink': 0.6,
                            'aspect': 40,
                            'pad': 0.05})

# Añadir título con un estilo profesional
ax.set_title('Participación Electoral por Municipio - Estado Falcón', fontsize=18, fontweight='bold', pad=20)
ax.set_axis_off()  # Ocultar ejes

# Añadir una nota sobre la fuente de datos
fig.text(0.5, 0.01, 'Fuente: datos-participacion.csv', ha='center', fontsize=10, style='italic')

# Guardar el mapa minimalista con alta calidad
plt.savefig('mapa_participacion_minimalista.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Mapa minimalista guardado como 'mapa_participacion_minimalista.png'")

# Mostrar el mapa minimalista
plt.tight_layout()
plt.show()

# Imprimir un resumen de los datos
print("\nResumen de Datos de Participación:")
print("=" * 50)
print(f"Participación promedio: {falcon_gdf['%PART'].mean():.1f}%")
print(f"Participación máxima: {falcon_gdf['%PART'].max():.1f}% - {falcon_gdf.loc[falcon_gdf['%PART'].idxmax(), 'ADM2_ES']}")
print(f"Participación mínima: {falcon_gdf['%PART'].min():.1f}% - {falcon_gdf.loc[falcon_gdf['%PART'].idxmin(), 'ADM2_ES']}")

print("\nMunicipios con mayor participación:")
top_participacion = falcon_gdf.sort_values('%PART', ascending=False).head(5)
for idx, row in top_participacion.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['%PART']:.1f}%")

print("\nMunicipios con menor participación:")
bottom_participacion = falcon_gdf.sort_values('%PART', ascending=True).head(5)
for idx, row in bottom_participacion.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['%PART']:.1f}%")