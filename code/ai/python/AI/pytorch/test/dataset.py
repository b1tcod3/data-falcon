import pandas as pd
import torch
from torch.utils.data import Dataset

# 1. Definición de la clase CustomCSCDataset
class CustomCSCDataset(Dataset):
    def __init__(self, csv_file):
        # Usamos pandas para leer el archivo CSV
        dataframe = pd.read_csv(csv_file)
        # Convertimos el DataFrame a tensores de PyTorch
        # .iloc[:, :-1] selecciona todas las filas y todas las columnas excepto la última
        X = dataframe.iloc[:, :-1].values
        self.features = torch.tensor(X, dtype=torch.float32)
        
        # Convertimos las etiquetas(Y) a tensores de PyTorch
        Y = dataframe.iloc[:, -1].values
        
        # .unsqueeze(1) añade una dimensión extra para que las etiquetas tengan la forma correcta (N,1)
        self.labels = torch.tensor(Y, dtype=torch.float32).unsqueeze(1)

    def __len__(self):
        # devuelve el número de muestras en el dataset
        return len(self.labels)
    
    def __getitem__(self, idx):
        # devuelve una muestra (características y etiqueta) en el índice dado
        return self.features[idx], self.labels[idx]

