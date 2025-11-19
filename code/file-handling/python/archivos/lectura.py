# Abrir un archivo en modo lectura
archivo = open('codigo/python/archivos/datos.txt', 'r')
import csv


# 1
contenido = archivo.read()
print(contenido)

# 2
linea = archivo.readline()
print(linea)

# 3
for linea in archivo.readlines():
    print(linea.strip())  # strip() elimina los espacios en blanco

# 4
parte = archivo.read(10)  # Lee los primeros 10 caracteres
print(parte)

# 5
with open('codigo/python/archivos/datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(f'Nombre: {fila[0]}, Edad: {fila[1]}')

# Cerrar el archivo
archivo.close()