## Gráfico de Barras

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'
AIRPORT_DELAYS_CSV = DATA / 'dfw_airline.csv'

dfw = pd.read_csv(AIRPORT_DELAYS_CSV)

ax = dfw.transpose().plot.bar(figsize=(4, 4), legend=False)
ax.set_xlabel('Cause of delay')
ax.set_ylabel('Count')

plt.tight_layout()
plt.show()