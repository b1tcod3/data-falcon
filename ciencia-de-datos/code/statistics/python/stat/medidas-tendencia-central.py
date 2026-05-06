# Importación de las bibliotecas necesarias:
import pandas as pd
import numpy as np
from scipy.stats import trim_mean
import wquantiles

# Definición de la ruta del archivo CSV:
STATE_CSV = 'state.csv' # leer la fuente de los datos

# Se lee el archivo CSV utilizando pandas y se almacena en el DataFrame state.
state = pd.read_csv(STATE_CSV)

# 1. Media
# Se calcula la media de la columna Population del DataFrame state.
mean = state['Population'].mean()

# 2. Media Truncada
# Se calcula la media truncada de la columna Population del DataFrame state, eliminando el 10% de los valores más altos y más bajos.
trim_mean(state['Population'], 0.1)

# 3. Media ponderada
# Se calcula la media ponderada de la columna Murder.Rate del DataFrame state, utilizando los valores de la columna Population como peso
np.average(state['Murder.Rate'], weights=state['Population'])

# 4. Mediana
# Se calcula la mediana de la columna Population del DataFrame state.
state['Population'].median()

# 5. Mediana ponderada
# Se calcula la mediana ponderada de la columna Murder.Rate del DataFrame state, utilizando los valores de la columna Population como peso.
wquantiles.median(state['Murder.Rate'], weights=state['Population'])