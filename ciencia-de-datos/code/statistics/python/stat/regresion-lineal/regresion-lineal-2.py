from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

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