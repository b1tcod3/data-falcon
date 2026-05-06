# Se importa la clase OrdinalEncoder del módulo sklearn.preprocessing. 
# Esta clase se utiliza para convertir datos categóricos en números enteros.
from sklearn.preprocessing import OrdinalEncoder

# Se crea una instancia de OrdinalEncoder llamada enc.
enc = OrdinalEncoder()

# Se define una lista de listas X que contiene datos categóricos
# y numéricos. En este caso, los datos categóricos 
# son 'Male' y 'Female', y los datos numéricos son 1, 2 y 3.
X = [['Male', 1], ['Female', 3], ['Female', 2]]

# Se ajusta el codificador enc a los datos X. 
# Esto significa que el codificador aprende las categorías presentes en los datos.
enc.fit(X)

# Se imprimen las categorías aprendidas por el codificador. 
# Esto mostrará las categorías únicas para cada característica en X.
print(enc.categories_)

# Se transforman nuevos datos utilizando el codificador ajustado. 
# Los datos categóricos se convierten en números enteros basados en las categorías aprendidas.
print(enc.transform([['Female', 3], ['Male', 1]]))

# Salida:
# [array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
# [[0. 2.]
#  [1. 0.]]