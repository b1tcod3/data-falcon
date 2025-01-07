# Importación de las bibliotecas necesarias:
import pandas as pd
import numpy as np
from scipy.stats import trim_mean
import wquantiles

# Definición de la ruta del archivo CSV:
STATE_CSV = 'state.csv' # leer la fuente de los datos

# Se lee el archivo CSV utilizando pandas y se almacena en el DataFrame state.
state = pd.read_csv(STATE_CSV)

# Se calcula la media de la columna Population del DataFrame state.
mean = state['Population'].mean()

#media truncada
trim_mean(state['Population'], 0.1)
#mediana
state['Population'].median()
#media ponderada
np.average(state['Murder.Rate'], weights=state['Population'])
#mediana ponderada
wquantiles.median(state['Murder.Rate'], weights=state['Population'])