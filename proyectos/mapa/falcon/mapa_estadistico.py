import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Cargar el shape file
shapefile_path = "ven/ven.shp"
gdf = gpd.read_file(shapefile_path)

# Filtrar solo los municipios del estado Falcón
falcon_gdf = gdf[gdf['ADM1_ES'] == 'Falcón'].copy()

# Generar datos estadísticos ficticios para cada municipio
np.random.seed(42)  # Para reproducibilidad
num_municipios = len(falcon_gdf)

# Datos ficticios de población (en miles)
poblacion = np.random.randint(5, 100, size=num_municipios)

# Datos ficticios de densidad de población (habitantes por km²)
densidad = np.random.randint(10, 200, size=num_municipios)

# Datos ficticios de índice de desarrollo (0-100)
desarrollo = np.random.randint(30, 95, size=num_municipios)

# Añadir estos datos al GeoDataFrame
falcon_gdf['Poblacion'] = poblacion
falcon_gdf['Densidad'] = densidad
falcon_gdf['Desarrollo'] = desarrollo

# Función para crear un mapa coroplético
def mapa_coropletico(datos, titulo, archivo_salida, colormap='viridis'):
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Crear el mapa coroplético
    falcon_gdf.plot(column=datos,
                   ax=ax,
                   edgecolor='black',
                   linewidth=0.8,
                   cmap=colormap,
                   legend=True,
                   legend_kwds={'label': titulo.split(": ")[1],
                               'orientation': 'horizontal',
                               'shrink': 0.6,
                               'aspect': 40,
                               'pad': 0.05})
    
    # Añadir etiquetas de municipios
    for idx, row in falcon_gdf.iterrows():
        nombre_municipio = row['ADM2_ES']
        centroide = row.geometry.centroid
        plt.annotate(text=nombre_municipio, 
                     xy=(centroide.x, centroide.y),
                     horizontalalignment='center',
                     fontsize=7,
                     color='black',
                     fontweight='bold')
    
    # Añadir título
    ax.set_title(titulo, fontsize=16, fontweight='bold')
    ax.set_axis_off()  # Ocultar ejes
    
    # Guardar el mapa
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight')
    print(f"Mapa guardado como '{archivo_salida}'")
    
    # Mostrar el mapa
    plt.tight_layout()
    plt.show()

# Crear mapa de población
mapa_coropletico('Poblacion', 
                'Mapa del Estado Falcón: Población por Municipio (miles de habitantes)', 
                'mapa_falcon_poblacion.png',
                colormap='YlOrRd')

# Crear mapa de densidad de población
mapa_coropletico('Densidad', 
                'Mapa del Estado Falcón: Densidad de Población (hab/km²)', 
                'mapa_falcon_densidad.png',
                colormap='Blues')

# Crear mapa de índice de desarrollo
mapa_coropletico('Desarrollo', 
                'Mapa del Estado Falcón: Índice de Desarrollo por Municipio', 
                'mapa_falcon_desarrollo.png',
                colormap='Greens')

# Crear un resumen estadístico
print("\nResumen Estadístico del Estado Falcón:")
print("=" * 50)
print(f"Total de municipios: {num_municipios}")
print(f"Población total: {falcon_gdf['Poblacion'].sum():.0f} miles de habitantes")
print(f"Población promedio por municipio: {falcon_gdf['Poblacion'].mean():.1f} miles")
print(f"Densidad promedio: {falcon_gdf['Densidad'].mean():.1f} hab/km²")
print(f"Índice de desarrollo promedio: {falcon_gdf['Desarrollo'].mean():.1f}/100")
print("\nMunicipios con mayor población:")
top_poblacion = falcon_gdf.sort_values('Poblacion', ascending=False).head(3)
for idx, row in top_poblacion.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['Poblacion']:.0f} miles de habitantes")

print("\nMunicipios con mayor índice de desarrollo:")
top_desarrollo = falcon_gdf.sort_values('Desarrollo', ascending=False).head(3)
for idx, row in top_desarrollo.iterrows():
    print(f"  - {row['ADM2_ES']}: {row['Desarrollo']:.0f}/100")

# Crear una tabla con todos los datos
tabla_datos = falcon_gdf[['ADM2_ES', 'Poblacion', 'Densidad', 'Desarrollo']].copy()
tabla_datos.columns = ['Municipio', 'Población (miles)', 'Densidad (hab/km²)', 'Índice de Desarrollo']
tabla_datos = tabla_datos.sort_values('Municipio')

# Guardar la tabla como CSV
tabla_datos.to_csv('datos_estadisticos_falcon.csv', index=False)
print("\nTabla de datos guardada como 'datos_estadisticos_falcon.csv'")