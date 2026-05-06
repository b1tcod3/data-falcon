import numpy as np

#matriz
m1 = np.array([[1, 2], [3, 4]])

# Calcular los valores y vectores propios
valores, vectores = np.linalg.eig(m1)

print("Valores propios:")
print(valores)
# Resultado: [-0.37228132  5.37228132]
print("Vectores propios:")
print(vectores)

# Resultado: 
# [
# [-0.82456484 -0.41597356]
# [ 0.56576746 -0.90937671]
# ]