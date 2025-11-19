from model import model
import torch

all_predictions = []
all_labels = []
train_loader = __import__('dataloader').train_loader

with torch.no_grad():
    for inputs, labels in train_loader:
        # 1. Forward pass: obtenemos las predicciones del modelo
        outputs = model(inputs)
        
        # 2. convertirmos probabilidades a etiquetas binarias
        predicted_classes = torch.round(outputs)
        
        all_predictions.append(predicted_classes)
        all_labels.append(labels)
        
# calculo de precisión
pred_tensor = torch.cat(all_predictions)
label_tensor = torch.cat(all_labels)

# comparamos si las predicciones son iguales a las etiquetas reales
# El resultado es una tensor de booleanos
correct_predictions = (pred_tensor == label_tensor).float()

# Calculamos la precisión (accuracy)
accuracy = correct_predictions.sum() / len(correct_predictions)
print(f'Accuracy del modelo en el conjunto de datos: {accuracy.item():.4f}')