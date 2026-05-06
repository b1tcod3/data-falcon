## Gráfico de Barras

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# leyendo data
DATA = Path().resolve() / 'data'
LC_LOANS_CSV = DATA / 'lc_loans.csv'

lc_loans = pd.read_csv(LC_LOANS_CSV)

crosstab = lc_loans.pivot_table(index='grade', columns='status', 
                                aggfunc=lambda x: len(x), margins=True)
print(crosstab)
