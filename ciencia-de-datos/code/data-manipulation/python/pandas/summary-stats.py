import pandas as pd

nutri = pd.read_csv('nutri.csv')

mean_height = nutri.height.mean()
quantiles_height = nutri.height.quantile(q=[.25,.5,.75])
range = nutri.height.max()-nutri.height.min()
variance = round(nutri.height.var(),2)
std = round(nutri.height.std(),2)
resume = nutri.height.describe()

print('Promedio de heigh: ', mean_height)
print('Cuartiles: ', quantiles_height)
print('Rango: ', range)
print('Varianza: ', variance)
print('Desviación Estandar: ', std)
print('Resumen Completo: ', resume)



