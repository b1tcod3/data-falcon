import pandas as pd
import matplotlib.pyplot as plt

nutri = pd.read_csv('data/nutri.csv')

plt.scatter(nutri.height, nutri.weight, s=12, marker='o')
plt.xlabel('height')
plt.ylabel('weight')

plt.show()