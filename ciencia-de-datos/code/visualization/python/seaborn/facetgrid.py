import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset("penguins")

g = sns.FacetGrid(df, col="species", hue="species", height=4, 
                  aspect=1)

g.map(sns.histplot, "flipper_length_mm", kde=True)

g.add_legend()

plt.show()
