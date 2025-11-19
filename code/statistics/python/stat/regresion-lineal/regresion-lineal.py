import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Creación de un conjunto de datos ficticio
data = {
    'Tamaño (pies cuadrados)': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'Precio ($)': [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000, 460000, 480000]
}

df = pd.DataFrame(data)
print(df)

plt.scatter(df['Tamaño (pies cuadrados)'], df['Precio ($)'])
plt.title('Precio de la Casa vs Tamaño')
plt.xlabel('Tamaño (pies cuadrados)')
plt.ylabel('Precio ($)')
plt.grid()
plt.show()

X = df[['Tamaño (pies cuadrados)']]  # Variable independiente
y = df['Precio ($)']                  # Variable dependiente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r_squared = model.score(X_test, y_test)
print(f'Coeficiente de determinación R²: {r_squared:.2f}')

plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', label='Predicción de regresión lineal')
plt.title('Predicción de Precio de Casa')
plt.xlabel('Tamaño (pies cuadrados)')
plt.ylabel('Precio ($)')
plt.legend()
plt.grid()
plt.show()