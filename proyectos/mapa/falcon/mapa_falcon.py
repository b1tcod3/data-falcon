import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el shape file
shapefile_path = "ven/ven.shp"
gdf = gpd.read_file(shapefile_path)

# Mostrar información básica del shape file
print("Información del shape file:")
print(f"Número de municipios: {len(gdf)}")
print(f"Columnas disponibles: {list(gdf.columns)}")
print("\nEstados disponibles:")
print(gdf['ADM1_ES'].unique())

# Filtrar solo los municipios del estado Falcón
falcon_gdf = gdf[gdf['ADM1_ES'] == 'Falcón']
print(f"\nNúmero de municipios en Falcón: {len(falcon_gdf)}")

# Verificar si encontramos municipios de Falcón
if len(falcon_gdf) == 0:
    print("No se encontraron municipios del estado Falcón. Verificando estados similares...")
    # Buscar estados que contengan "Falcón" en su nombre
    estados_similares = [estado for estado in gdf['ADM1_ES'].unique() if 'falc' in estado.lower()]
    print(f"Estados similares encontrados: {estados_similares}")
    if estados_similares:
        falcon_gdf = gdf[gdf['ADM1_ES'] == estados_similares[0]]
        print(f"Utilizando el estado: {estados_similares[0]} con {len(falcon_gdf)} municipios")

# Crear una figura para el mapa
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Plotear el mapa de Falcón
falcon_gdf.plot(ax=ax,
               edgecolor='black',  # Color de los bordes
               linewidth=0.8,     # Grosor de los bordes
               cmap='tab20',      # Mapa de colores
               legend=False)      # No mostrar leyenda para municipios

# Añadir título y mejorar la visualización
ax.set_title('Mapa del Estado Falcón por Municipio', fontsize=18, fontweight='bold')
ax.set_axis_off()  # Ocultar ejes

# Guardar el mapa
plt.savefig('mapa_falcon.png', dpi=300, bbox_inches='tight')
print("\nMapa guardado como 'mapa_falcon.png'")

# Mostrar el mapa
plt.tight_layout()
plt.show()

# Crear un segundo mapa con etiquetas de municipios
fig, ax = plt.subplots(1, 1, figsize=(12, 12))

# Plotear el mapa de Falcón
falcon_gdf.plot(ax=ax,
               edgecolor='black',  # Color de los bordes
               linewidth=0.8,     # Grosor de los bordes
               cmap='tab20',      # Mapa de colores
               legend=False)      # No mostrar leyenda para municipios

# Añadir etiquetas de municipios usando la columna correcta
for idx, row in falcon_gdf.iterrows():
    # Obtener el nombre del municipio
    nombre_municipio = row['ADM2_ES']
    
    # Obtener el centroide del polígono
    centroide = row.geometry.centroid
    
    # Añadir la etiqueta
    plt.annotate(text=nombre_municipio,
                 xy=(centroide.x, centroide.y),
                 horizontalalignment='center',
                 fontsize=8,
                 color='black',
                 fontweight='bold')

# Añadir título y mejorar la visualización
ax.set_title('Mapa del Estado Falcón por Municipio con Nombres', fontsize=18, fontweight='bold')
ax.set_axis_off()  # Ocultar ejes

# Guardar el mapa con etiquetas
plt.savefig('mapa_falcon_con_etiquetas.png', dpi=300, bbox_inches='tight')
print("Mapa con etiquetas guardado como 'mapa_falcon_con_etiquetas.png'")

# Mostrar el mapa con etiquetas
plt.tight_layout()
plt.show()

# Imprimir lista de municipios de Falcón
print("\nLista de municipios del estado Falcón:")
for municipio in falcon_gdf['ADM2_ES'].sort_values():
    print(f"- {municipio}")