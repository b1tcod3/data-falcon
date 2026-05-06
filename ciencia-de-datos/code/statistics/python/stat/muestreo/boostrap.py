## Gráfico de Barras

from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.utils import resample

DATA = Path().resolve() / 'data'
LOANS_INCOME_CSV = DATA / 'loans_income.csv'

loans_income = pd.read_csv(LOANS_INCOME_CSV).squeeze('columns')

results = []
for nrepeat in range(1000):
    sample = resample(loans_income)
    results.append(sample.median())
results = pd.Series(results)
print('Bootstrap Statistics:')
print(f'original: {loans_income.median()}')
print(f'bias: {results.mean() - loans_income.median()}')
print(f'std. error: {results.std()}')