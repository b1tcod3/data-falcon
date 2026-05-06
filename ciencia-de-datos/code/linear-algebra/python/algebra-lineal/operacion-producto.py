import numpy as np

# vectores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
#matrices
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# producto punto de vectores
producto_punto = np.dot(v1, v2)  
# Resultado: 32
print(producto_punto)

# producto cruz de vectores
producto_cruz= np.cross(v1, v2)  
# Resultado: [-3  6 -3]
print(producto_cruz)

producto_cruz_matriz = np.dot(m1, m2)  
# Resultado: [-3  6 -3]
print(producto_cruz_matriz)
# Resultado: [[-19,  22], [43,  50]]