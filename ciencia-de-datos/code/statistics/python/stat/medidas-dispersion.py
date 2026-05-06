# importación de las bibliotecas necesarias:
from pathlib import Path
import pandas as pd
import numpy as np
from statsmodels import robust

DATA = Path().resolve() / 'data'
# se define la ruta del archivo CSV que contiene los datos.
STATE_CSV = DATA / 'state.csv' # leer la fuente de los datos

# se lee el archivo CSV utilizando pandas
state = pd.read_csv(STATE_CSV)

# 1. Desviacion estandar
print(state['Population'].std())
# 6848235.347401142

# 2. IQR rango intercuartílico es calculado con la diferencia entre el 75 y el 
# 25 cuartil

print(state['Population'].quantile(0.75) - state['Population'].quantile(0.25))
# 4847308.0

# desviacion absoluta mediana de la mediana  se calcula
# con un metodo de statmodels
print(robust.scale.mad(state['Population']))
# 3849876.1459979336

# calculo manual de la desviacion absoluta mediana de la mediana
print(abs(state['Population'] - 
          state['Population'].median()).median() / 0.6744897501960817)
# 3849876.1459979336

