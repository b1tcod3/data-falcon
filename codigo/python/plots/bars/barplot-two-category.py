import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

nutri = pd.read_csv('data/nutri.csv')

sns.countplot(x='situation', hue="gender", data=nutri,
              hue_order= ['Male','Female'], palette=['SkyBlue','Pink'],
              saturation=1, edgecolor="black"
)

plt.legend(loc='upper center')
plt.xlabel('')
plt.ylabel('Counts')
plt.show()