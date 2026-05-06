import pandas as pd

nutri = pd.read_csv('nutri.csv')

crosstab = pd.crosstab(nutri.gender, nutri.situation, margins=True)

print(crosstab)

