import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA


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

ts = df['Precio_Accion'].asfreq('D').ffill()

# analisis de autocorrelacion

# fig, (ax1, ax2) = plt.subplots(2,1,figsize=(12, 8))
# plot_acf(ts, lags=40, ax=ax1)
# plot_pacf(ts, lags=40, ax=ax2)  
# plt.tight_layout()
# plt.show()

# Modelado ARIMA
model = ARIMA(ts, order=(1, 1, 1))
results = model.fit()

print(results.summary())

forecast = results.get_forecast(steps=30)
forecast_ci = forecast.conf_int()

ax = ts.plot(label='Observado', figsize=(12, 7))
forecast.predicted_mean.plot(ax=ax, label='Pronóstico', color='red')
ax.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.1)
plt.title('Pronóstico ARIMA')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio de la Acción')
ax.legend()
plt.show()

