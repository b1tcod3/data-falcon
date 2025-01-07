## diagrama de Violìn

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

# leyendo data
DATA = Path().resolve() / 'data'
AIRLINE_STATS_CSV = DATA / 'airline_stats.csv'

airline_stats = pd.read_csv(AIRLINE_STATS_CSV)

# seaborn soporto el diagrama de violín con violinplot.

fig, ax = plt.subplots(figsize=(5, 5))
sns.violinplot(data=airline_stats, x='airline', y='pct_carrier_delay',
               ax=ax, inner='quartile', color='white')
ax.set_xlabel('')
ax.set_ylabel('Daily % of Delayed Flights')

plt.tight_layout()
plt.show()
