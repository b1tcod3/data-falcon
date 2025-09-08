import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
import matplotlib.patches as mpatches

# Cargar el shape file
shapefile_path = "ven/ven.shp"
gdf = gpd.read_file(shapefile_path)

# Filtrar solo los municipios del estado Falcón
falcon_gdf = gdf[gdf['ADM1_ES'] == 'Falcón']

# Crear una figura para el mapa interactivo
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
plt.subplots_adjust(bottom=0.2)  # Espacio para los controles

# Función para actualizar el mapa
def actualizar_mapa(colormap='tab20', resaltar=None):
    ax.clear()
    
    # Plotear el mapa de Falcón
    falcon_gdf.plot(ax=ax, 
                   edgecolor='black',  # Color de los bordes
                   linewidth=0.8,     # Grosor de los bordes
                   cmap=colormap,     # Mapa de colores
                   legend=False)      # No mostrar leyenda para municipios
    
    # Resaltar un municipio específico si se solicita
    if resaltar:
        municipio_resaltar = falcon_gdf[falcon_gdf['ADM2_ES'] == resaltar]
        otros_municipios = falcon_gdf[falcon_gdf['ADM2_ES'] != resaltar]
        
        ax.clear()
        
        # Plotear otros municipios en gris
        otros_municipios.plot(ax=ax, 
                             edgecolor='black', 
                             linewidth=0.8,
                             color='lightgray',
                             legend=False)
        
        # Plotear municipio resaltado
        municipio_resaltar.plot(ax=ax, 
                               edgecolor='red', 
                               linewidth=1.5,
                               color='orange',
                               legend=False)
        
        # Añadir etiqueta al municipio resaltado
        for idx, row in municipio_resaltar.iterrows():
            centroide = row.geometry.centroid
            plt.annotate(text=row['ADM2_ES'], 
                         xy=(centroide.x, centroide.y),
                         horizontalalignment='center',
                         fontsize=10,
                         color='red',
                         fontweight='bold')
    else:
        # Añadir etiquetas de todos los municipios
        for idx, row in falcon_gdf.iterrows():
            nombre_municipio = row['ADM2_ES']
            centroide = row.geometry.centroid
            plt.annotate(text=nombre_municipio, 
                         xy=(centroide.x, centroide.y),
                         horizontalalignment='center',
                         fontsize=8,
                         color='black',
                         fontweight='bold')
    
    # Añadir título y mejorar la visualización
    if resaltar:
        ax.set_title(f'Mapa del Estado Falcón - Municipio Resaltado: {resaltar}', fontsize=18, fontweight='bold')
    else:
        ax.set_title('Mapa del Estado Falcón por Municipio', fontsize=18, fontweight='bold')
    
    ax.set_axis_off()  # Ocultar ejes
    
    # Actualizar la figura
    fig.canvas.draw_idle()

# Función para manejar el clic en un municipio
def on_click(event):
    if event.inaxes != ax:
        return
    
    # Convertir coordenadas del clic a coordenadas geográficas
    x, y = event.xdata, event.ydata
    
    # Crear un punto con las coordenadas del clic
    from shapely.geometry import Point
    punto = Point(x, y)
    
    # Encontrar el municipio que contiene el punto
    for idx, row in falcon_gdf.iterrows():
        if row.geometry.contains(punto):
            print(f"Municipio seleccionado: {row['ADM2_ES']}")
            actualizar_mapa(resaltar=row['ADM2_ES'])
            return

# Lista de municipios para el menú desplegable
municipios = sorted(falcon_gdf['ADM2_ES'].tolist())

# Función para el botón de reset
def reset(event):
    actualizar_mapa()

# Crear botón de reset
ax_reset = plt.axes([0.8, 0.05, 0.1, 0.04])
btn_reset = Button(ax_reset, 'Reiniciar')
btn_reset.on_clicked(reset)

# Conectar el evento de clic
fig.canvas.mpl_connect('button_press_event', on_click)

# Mostrar el mapa inicial
actualizar_mapa()

# Instrucciones para el usuario
print("\nInstrucciones para el mapa interactivo:")
print("- Haga clic en cualquier municipio para resaltarlo")
print("- Use el botón 'Reiniciar' para volver al mapa completo")
print("- Los municipios del estado Falcón son:")
for municipio in municipios:
    print(f"  * {municipio}")

plt.tight_layout()
plt.show()