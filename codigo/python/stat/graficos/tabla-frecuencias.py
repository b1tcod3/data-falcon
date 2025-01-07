## diagrama de cajas en R

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'

STATE_CSV = DATA / 'state.csv'
state = pd.read_csv(STATE_CSV)

# tabla de frecuencias
# El metodo `cut` separa la data

binnedPopulation = pd.cut(state['Population'], 10)
print(binnedPopulation.value_counts())
