## diagrama de cajas en R

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'

STATE_CSV = DATA / 'state.csv'
state = pd.read_csv(STATE_CSV)

# # diagrama de cajas
ax = (state['Population']/1_000_000).plot.box(figsize=(3, 4))
ax.set_ylabel('Population (millions)')

plt.tight_layout()
plt.show()

