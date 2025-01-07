import numpy as np

# Definir la matriz A
A = np.array([[5, 4],
              [2, 3]])

# Calcular los valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(A)

# Normalizar los vectores propios para que nos arroje el mismo valore del ejemplo
vectores_propios[:, 0] = vectores_propios[:, 0] / vectores_propios[1, 0]
vectores_propios[:, 1] = vectores_propios[:, 1] / vectores_propios[1, 1]

# Mostrar los resultados
print("Valores propios:")
for i, valor in enumerate(valores_propios):
    print(f"λ_{i + 1} = {valor:.2f}")

# Mostrar los vectores propios normalizados,tomando los valores por columna
for i in range(len(vectores_propios)):
    print(f"Vector propio asociado a λ_{i + 1}: {vectores_propios[:,i]}")

# Comprobamos que los valores propios y los vectores propios son correctos mediante la igualdad: AV = λV
for i in range(len(valores_propios)):
    av = np.dot(A, vectores_propios[:, i])
    lv = valores_propios[i]* vectores_propios[:, i]
    print(f"AV = {av}")
    print(f"λV = {lv}")
     
# Valores propios:
# λ_1 = 7.00
# λ_2 = 1.00
# Vector propio asociado a λ_1: [2. 1.]
# Vector propio asociado a λ_2: [-1.  1.]
# AV = [14.  7.]
# λV = [14.  7.]
# AV = [-1.  1.]
# λV = [-1.  1.]

