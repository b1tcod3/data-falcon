import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'

dataname = 'MASS/birthwt.csv'

bwt = pd.read_csv(urlprefix + dataname)

bwt = bwt.drop('rownames', axis=1)

styles = {0: ['o', 'red'], 1: ['^', 'blue']}

for k in styles:
    grp = bwt[bwt.smoke == k]
    m,b = np.polyfit(grp.age, grp.bwt, 1)
    label = 'No Fumadora' if k == 0 else 'Fumadora'
    plt.scatter(grp.age, grp.bwt, c=styles[k][1], marker=styles[k][0],s=15, linewidth=0, label=label)
    plt.plot(grp.age, m*grp.age + b,'-',color=styles[k][1])

plt.xlabel('Edad de la madre')
plt.ylabel('Peso al nacer (onzas)')
plt.legend(prop={'size':8}, loc=(0.5,0.8))

plt.show()