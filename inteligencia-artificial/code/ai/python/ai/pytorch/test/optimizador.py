import torch.optim as optim
from torch import nn
from model import model
import torch


# hiperparámetros
LEARNING_RATE = 0.001
EPOCHS = 100

# 1. Función de perdida
criterion = nn.BCELoss()

# 2. Optimizador
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)  # Los parámetros del modelo se agregarán más tarde

# 3.bucle de entrenamiento (esqueleto)
for epoch in range(EPOCHS):
    #iteramos sobre el dataLoader, que nos da lotes(features, labels)
    for i, (inputs, labels) in enumerate(train_loader):
        # Reiniciamos los gradientes
        optimizer.zero_grad()
        
        # Forward pass: calculamos las predicciones del modelo
        outputs = model(inputs)
        
        # Calculamos la pérdida
        loss = criterion(outputs, labels)
        
        # Backward pass: calculamos los gradientes
        loss.backward()
        
        # Actualizamos los parámetros del modelo
        optimizer.step()
    
    print(f'Epoch [{epoch+1}/{EPOCHS}], Loss: {loss.item():.4f}')    

model_state_dict = model.state_dict()
torch.save(model_state_dict, 'modelo_clasificador_binario.pth')
print("Modelo guardado como 'modelo_clasificador_binario.pth'")