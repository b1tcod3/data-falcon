import pandas as pd
import numpy as np
from statsmodels import robust

STATE_CSV = 'state.csv' # leer la fuente de los datos
state = pd.read_csv(STATE_CSV)

# desviacion estandar
print(state['Population'].std())

# rango intercuartílico es calculado con la diferencia entre el 75 y el 
# 25 cuartil

print(state['Population'].quantile(0.75) - state['Population'].quantile(0.25))

# desviacion absoluta mediana de la mediana  se calcula
# con un metodo de statmodels
print(robust.scale.mad(state['Population']))
print(abs(state['Population'] - 
          state['Population'].median()).median() / 0.6744897501960817)
