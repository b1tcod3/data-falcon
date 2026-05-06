import torch.nn as nn
import torch.nn.functional as F
import torch

class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleClassifier, self).__init__()
        # capa de entrada al primera capa oculta
        self.fc1 = nn.Linear(input_size, hidden_size)
        # capa de la primera capa oculta a la segunda capa oculta
        self.fc2 = nn.Linear(hidden_size, hidden_size // 2)
        # capa de la segunda capa oculta a la capa de salida
        self.fc3 = nn.Linear(hidden_size // 2, output_size)
    
    def forward(self, x):
        # aplicamos la primera capa lineal y la funcion de activacion ReLU
        x = F.relu(self.fc1(x))
        # aplicamos la segunda capa lineal y la funcion de activacion ReLU
        x = F.relu(self.fc2(x))
        # aplicamos la capa de salida final
        x = self.fc3(x)
        
        #aplicamos la funcion de activacion sigmoide para obtener probabilidades
        x = torch.sigmoid(x)
        
        return x
    
loaded_model = SimpleClassifier(input_size=8, hidden_size=16, output_size=1)
loaded_model.load_state_dict(torch.load('modelo_clasificador_binario.pth'))


# Imprimimos la arquitectura del modelo
# print("Arquitectura del modelo:")
# print(model)