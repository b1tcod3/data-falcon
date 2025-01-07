## diagrama de cajas multiples

from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'
AIRLINE_STATS_CSV = DATA / 'airline_stats.csv'

airline_stats = pd.read_csv(AIRLINE_STATS_CSV)
airline_stats.head()
ax = airline_stats.boxplot(by='airline', column='pct_carrier_delay',
                           figsize=(5, 5))
ax.set_xlabel('')
ax.set_ylabel('Daily % of Delayed Flights')
plt.suptitle('')

plt.tight_layout()
plt.show()

