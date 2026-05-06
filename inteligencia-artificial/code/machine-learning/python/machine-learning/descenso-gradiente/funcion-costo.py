import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Parámetros
alpha = 0.01  # Tasa de aprendizaje
iterations = 1000
m = len(y)

# Inicialización de parámetros
theta = 0  # Pendiente
b = 0      # Intersección

# Función de costo (MSE)
def compute_cost(X, y, theta, b):
    return (1/(2*m)) * np.sum((theta*X + b - y) ** 2)

# Descenso de gradiente
for _ in range(iterations):
    theta -= alpha * (1/m) * np.sum((theta*X + b - y) * X)
    b -= alpha * (1/m) * np.sum(theta*X + b - y)

# Resultados
print(f'Pendiente: {theta}, Intersección: {b}')
print(f'Costo final: {compute_cost(X, y, theta, b)}')

# Visualización
plt.scatter(X, y, color='blue')
plt.plot(X, theta*X + b, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal usando Descenso de Gradiente')
plt.show()