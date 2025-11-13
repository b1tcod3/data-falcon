import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset('penguins')

sns.pairplot(df, hue="species", palette="husl", diag_kind="kde")

plt.title('Relaciones entre variables en el dataset Penguins')
plt.show()
