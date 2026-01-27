import torch
import torch.nn as nn
import torch.optim as optim

# Generate synthetic data
true_weight = 2.0
true_bias = 0.5
num_samples = 100

# creamos datos de entrada (caracteristicas únicas)
X = torch.randn(num_samples, 1)*10 # 100 muestras, 1 característica, valores mas dispersos

# creamos los valores de salida
# y = mx + b + ruido (ruido simula el componente 'normal' o error Gaussiano)

noise = torch.randn(num_samples,1)*1.5
y = true_weight * X + true_bias + noise

print(f"Parámetros Reales : Peso: {true_weight}, Sesgo: {true_bias}")

# Definición del modelo lineal
class LinearRegressionModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel, self).__init__()
        # nn.Linear es la capa que implementa y = Wx+b
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# instaciamos el modelo: 1 entrada, 1 salida
model  = LinearRegressionModel(1, 1)

# MSE es la función de pérdida estandar. 
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001) # descenso de gradiente estocástico, con tasa de aprendizaje 0.01

# bucle de entrenamiento
num_epochs = 1000

for epoch in range(num_epochs):
    # paso de avance: calcular la predicción
    y_predicted = model(X)

    # calcular la pérdida
    loss = criterion(y_predicted, y)

    # reiniciar los gradientes a cero
    optimizer.zero_grad()

    # paso de retroceso (backward pass) calcular los gradientes
    loss.backward()

    # actualizar los parámetros del modelo
    optimizer.step()

    if(epoch +1 ) % 10 == 0:
        print(f'Época [{epoch+1}/{num_epochs}], Pérdida: {loss.item():.4f}')

# resultados finales

learned_weight = model.linear.weight.item()
learned_bias = model.linear.bias.item()

print("\n--- Parámetros Aprendidos ---")
print(f'Peso Aprendido: {learned_weight:.4f}, Sesgo Aprendido: {learned_bias:.4f}')
print("\n--- Parámetros Reales ---")
print(f'Peso Real: {true_weight}, Sesgo Real: {true_bias}')
print("\n--- Comparación ---")
print(f'Diferencia en Peso: {abs(learned_weight - true_weight):.4f}, Diferencia en Sesgo: {abs(learned_bias - true_bias):.4f}')
print("\n--- Fin del Entrenamiento ---")
