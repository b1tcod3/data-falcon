import numpy as np

# Definir los vectores
v1 = np.array([1, 2])
v2 = np.array([3, 4])
v = np.array([7, 8])

# Formar la matriz A con v1 y v2 como columnas
A = np.column_stack((v1, v2))

# Resolver el sistema Ax = v
try:
    coefficients = np.linalg.solve(A, v)
    print(f"El vector v es combinación lineal de v1 y v2 con coeficientes: {coefficients}")
except np.linalg.LinAlgError:
    print("El vector v NO es combinación lineal de v1 y v2.")

# verificando
v_testing = coefficients[0]*v1 + coefficients[1]*v2
assert np.array_equal(v,v_testing), "Fallo la comprobación"  # Si no se cumple la condición, se lanza un error

    
# Resultado:
# El vector v es combinación lineal de v1 y v2 con coeficientes: [-2.  3.]