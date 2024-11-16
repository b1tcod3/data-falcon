import pandas as pd
import numpy as np
from scipy.stats import trim_mean
import wquantiles

STATE_CSV = 'state.csv' # leer la fuente de los datos
state = pd.read_csv(STATE_CSV)

#media
state['Population'].mean()
#media truncada
trim_mean(state['Population'], 0.1)
#mediana
state['Population'].median()
#media ponderada
np.average(state['Murder.Rate'], weights=state['Population'])
#mediana ponderada
wquantiles.median(state['Murder.Rate'], weights=state['Population'])