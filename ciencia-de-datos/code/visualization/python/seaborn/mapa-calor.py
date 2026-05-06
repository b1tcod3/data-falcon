import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
df = sns.load_dataset('penguins')

# calcular la matriz de correlación
correlation = df.corr(numeric_only=True)

# crear el mapa de calor
sns.heatmap(correlation, annot=True, cmap='coolwarm',vmin=-1, vmax=1)

plt.title('Mapa de Calor de Correlación de Datos de Pingüinos')
plt.show()
