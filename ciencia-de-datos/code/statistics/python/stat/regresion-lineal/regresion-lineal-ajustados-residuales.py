from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LUNG_CSV = '/home/data/Documentos/practical-statistics-for-data-scientists-master/data/LungDisease.csv'


## Simple Linear Regression
### The Regression Equation
lung = pd.read_csv(LUNG_CSV)
lung.plot.scatter(x='Exposure', y='PEFR')
plt.tight_layout()
plt.show()

# We can use the `LinearRegression` model from _scikit-learn_.
predictors = ['Exposure']
outcome = 'PEFR'

model = LinearRegression()
model.fit(lung[predictors], lung[outcome])

print(f'Intercept: {model.intercept_:.3f}')
print(f'Coefficient Exposure: {model.coef_[0]:.3f}')

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 23)
ax.set_ylim(295, 450)
ax.set_xlabel('Exposure')
ax.set_ylabel('PEFR')
ax.plot((0, 23), model.predict(pd.DataFrame({'Exposure': [0, 23]})))
ax.text(0.4, model.intercept_, r'$b_0$', size='larger')

x = pd.DataFrame({'Exposure': [7.5,17.5]})
y = model.predict(x)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')
ax.text(5, np.mean(y), r'$\Delta Y$', size='larger')
ax.text(12, y[1] - 10, r'$\Delta X$', size='larger')
ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size='larger')

plt.tight_layout()
plt.show()

### Fitted Values and Residuals
# The method `predict` of a fitted _scikit-learn_ model can be used to predict new data points.

fitted = model.predict(lung[predictors])
residuals = lung[outcome] - fitted

print(fitted)
print(residuals)