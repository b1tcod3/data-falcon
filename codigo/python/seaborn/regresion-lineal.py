import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", col="day",
           data=df,palette="coolwarm", height=4, aspect=0.7   )

plt.show()
