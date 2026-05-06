import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# generar datos financierons sinteticos
np.random.seed(42)

dates = pd.date_range(start='2020-01-01', periods=500, freq='D')

data = {
    'Precio_Accion': np.cumsum(np.random.randn(500)) + 100,
    'Volumen': np.abs(np.random.randn(500) * 1000)+50000,
    'RSI': np.random.uniform(30, 70, 500),
    'MACD': np.cumsum(np.random.randn(500))*0.1,
}

df = pd.DataFrame(data, index=dates)

corr_matrix = df.corr(method='spearman')
p_values = pd.DataFrame(index=corr_matrix.index, columns=corr_matrix.columns)
# p = lambda x, y: pd.Series(spearmanr(x, y)[1], index=corr_matrix.columns)
# p_values = df.corr(method=p)

# Visualación con máscara de para correlaciones no sifnificaivas (p > 0.05)
mask = np.triu(np.ones_like(corr_matrix,dtype=bool)) | p_values > 0.05

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", vmin=-1,vmax=1, cmap='coolwarm', mask=mask, cbar_kws={"shrink": .8})
plt.title('Matriz de Correlación Spearman con P-values')
plt.xticks(rotation=45)
plt.show()