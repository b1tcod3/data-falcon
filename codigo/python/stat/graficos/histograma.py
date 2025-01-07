## Histograma de Python

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'

STATE_CSV = DATA / 'state.csv'
state = pd.read_csv(STATE_CSV)

# ax = (state['Population'] / 1_000_000).plot.hist(figsize=(4, 4))
# ax.set_xlabel('Population (millions)')

# Histograma

ax = state['Murder.Rate'].plot.hist(density=True, xlim=[0, 12], 
                                    bins=range(1,12), figsize=(4, 4))
state['Murder.Rate'].plot.density(ax=ax)
ax.set_xlabel('Murder Rate (per 100,000)')

plt.tight_layout()
plt.show()

