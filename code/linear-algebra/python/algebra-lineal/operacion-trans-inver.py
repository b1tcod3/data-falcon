import numpy as np

m1 = np.array([[1, 2], [3, 4]])

# transpuesta
m_transpuesta = m1.T  
print(m_transpuesta)
# Resultado: [[1, 3], [2, 4]]

# inversión
m_inversa = np.linalg.inv(m1)  
print(m_inversa)
# Resultado: 
# [[-2, 1], 
# [1.5, -0.5]]

# determinante
det = np.linalg.det(m1)  
print(det)
# Resultado: -2.0

# Verificar si es invertible
if det != 0:
    print("La matriz es invertible.")
else:
    print("La matriz no es invertible.")
# Resultado: La matriz es invertible.