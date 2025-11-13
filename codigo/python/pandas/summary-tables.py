import pandas as pd

nutri = pd.read_csv('nutri.csv')

print(nutri['fat'].describe())

print(nutri['fat'].value_counts())

