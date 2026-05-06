import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

# Configuración del dispositivo (GPU si está disponible, si no, CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Usando dispositivo: {device}")

# 1. Transformaciones para los datos MNIST
transform = transforms.Compose([
    transforms.ToTensor(), # Convierte la imagen a un tensor PyTorch
    transforms.Normalize((0.1307,), (0.3081,)) # Normaliza con media y desv. est. de MNIST
])

# 2. Cargar los datos de MNIST
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, transform=transform)

# Dataloaders para iterar sobre los datos
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 3. Definición del Modelo de Red Neuronal con Dropout
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Primera capa convolucional
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1) # Entrada: 1 canal (escala de grises), 32 filtros, kernel 3x3
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2) # Reducción de tamaño 28x28 -> 14x14

        # Segunda capa convolucional
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1) # Entrada: 32 canales, 64 filtros
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2) # Reducción de tamaño 14x14 -> 7x7

        # Capa aplanadora (para pasar de 2D a 1D)
        self.flatten = nn.Flatten()

        # Capas densas (fully connected)
        self.fc1 = nn.Linear(64 * 7 * 7, 128) # Entrada: 64 filtros * 7x7 (tamaño de la imagen después de pooling)
        self.relu3 = nn.ReLU()

        # !!!!!!! LA CLAVE: Dropout Bayesiano !!!!!!!
        # Dropout aplicado en la capa densa. El 0.5 es la probabilidad de "apagar" una neurona.
        self.dropout = nn.Dropout(p=0.5)

        # Capa de salida
        self.fc2 = nn.Linear(128, 10) # 10 clases para los dígitos (0-9)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = self.flatten(x)
        x = self.relu3(self.fc1(x))

        # !!!!!!! Aplicar Dropout !!!!!!!
        x = self.dropout(x)

        x = self.fc2(x)
        return x

# Instanciar el modelo y enviarlo al dispositivo
model = Net().to(device)

# 4. Función de Pérdida y Optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 5. Bucle de Entrenamiento
num_epochs = 5
print("\n--- Entrenando el modelo ---")
for epoch in range(num_epochs):
    model.train() # Asegurarse de que el modelo está en modo entrenamiento (Dropout activo)
    running_loss = 0.0
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    epoch_loss = running_loss / len(train_loader.dataset)
    print(f"Época {epoch+1}/{num_epochs}, Pérdida: {epoch_loss:.4f}")

print("\n--- Entrenamiento Completado ---")

# 6. Evaluación del Modelo (predicción con incertidumbre)
print("\n--- Evaluando el modelo con Dropout Bayesiano ---")

# Seleccionamos algunas imágenes de prueba para visualizar la incertidumbre
num_test_samples = 5
test_images_batch = []
test_labels_batch = []

# Tomamos un lote de imágenes del test_loader
for images, labels in test_loader:
    test_images_batch.append(images)
    test_labels_batch.append(labels)
    if len(test_images_batch) * images.size(0) >= num_test_samples:
        break

test_images = torch.cat(test_images_batch)[:num_test_samples].to(device)
true_labels = torch.cat(test_labels_batch)[:num_test_samples].to(device)

# Número de pasadas Monte Carlo para estimar la incertidumbre
num_mc_dropout_passes = 100

# Almacenar las predicciones para cada imagen y cada pasada MC
all_predictions = torch.zeros(num_test_samples, num_mc_dropout_passes, 10).to(device) # 10 clases

# !!!!!!! La clave: Poner el modelo en modo TRAIN para que el dropout esté activo durante la inferencia !!!!!!!
model.train()

with torch.no_grad(): # No necesitamos calcular gradientes en la inferencia
    for i in range(num_mc_dropout_passes):
        outputs = model(test_images)
        all_predictions[:, i, :] = outputs # Guardar los logits (salidas antes de softmax)

# Convertir logits a probabilidades (softmax)
all_probabilities = torch.softmax(all_predictions, dim=2)

# Calcular la media y la desviación estándar de las probabilidades para cada imagen
mean_probabilities = all_probabilities.mean(dim=1) # Promedio de las probabilidades en las pasadas MC
std_probabilities = all_probabilities.std(dim=1)   # Desviación estándar para la incertidumbre

# 7. Visualización de Resultados
fig, axes = plt.subplots(num_test_samples, 2, figsize=(12, num_test_samples * 3))
fig.suptitle("Predicciones e Incertidumbre con Dropout Bayesiano", fontsize=16)

for i in range(num_test_samples):
    # Mostrar la imagen
    image_display = test_images[i].cpu().squeeze().numpy()
    axes[i, 0].imshow(image_display, cmap='gray')
    axes[i, 0].set_title(f"Real: {true_labels[i].item()}")
    axes[i, 0].axis('off')

    # Mostrar las probabilidades y la incertidumbre
    class_probabilities = mean_probabilities[i].cpu().numpy()
    class_uncertainty = std_probabilities[i].cpu().numpy()

    predicted_class = np.argmax(class_probabilities)

    bars = axes[i, 1].bar(range(10), class_probabilities, yerr=class_uncertainty, capsize=3, color='skyblue')
    bars[predicted_class].set_color('salmon') # Resaltar la clase predicha

    axes[i, 1].set_title(f"Predicción: {predicted_class} (Confianza: {class_probabilities[predicted_class]:.2f})")
    axes[i, 1].set_xlabel("Dígito")
    axes[i, 1].set_ylabel("Probabilidad")
    axes[i, 1].set_ylim(0, 1)
    axes[i, 1].set_xticks(range(10))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# También podemos ver la precisión "clásica" en el test set (con Dropout en modo eval)
model.eval() # Poner el modelo en modo evaluación para la métrica clásica
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"\nPrecisión del modelo en el conjunto de prueba (modo eval): {100 * correct / total:.2f}%")
