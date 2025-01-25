## diagrama de cajas en R

# 1. Importación de las bibliotecas necesarias:

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# 2. Leyendo la data
DATA = Path().resolve() / 'data'

STATE_CSV = DATA / 'state.csv'
state = pd.read_csv(STATE_CSV)

# 3. Creación del diagrama de cajas:
ax = (state['Population']/1_000_000).plot.box(figsize=(3, 4))
ax.set_ylabel('Population (millions)')

# 4. Ajuste del diseño y visualización del gráfico:

plt.tight_layout()
plt.show()

