import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", data=df, hue="sex", split=True, 
               inner="quart", palette="muted")

plt.title("Distribución de facturas por día y sexo")

plt.show()
