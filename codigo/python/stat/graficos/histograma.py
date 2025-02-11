## Histograma de Python

# Paso 1. Importación de bibliotecasnecesarias

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# Paso 2. leyendo data
DATA = Path().resolve() / 'data'

STATE_CSV = DATA / 'state.csv'
state = pd.read_csv(STATE_CSV)

# Paso 3. Histograma

ax = state['Murder.Rate'].plot.hist(density=True, xlim=[0, 12], 
                                    bins=range(1,12), figsize=(4, 4))

# Paso 4. Añadir la densidad de Kernel al histograma
state['Murder.Rate'].plot.density(ax=ax)

# Paso 5. Etiquetar el eje x
ax.set_xlabel('Murder Rate (per 100,000)')

# Paso 6. Ajuste del diseño y visualización del gráfico:

plt.tight_layout()
plt.show()

