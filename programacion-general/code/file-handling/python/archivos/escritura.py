# Abrir un archivo en modo lectura
import csv

ruta = 'codigo/python/archivos/datos.txt'
archivo = open(ruta, 'r')

# 1
with open(ruta, 'w') as archivo:
    archivo.write('Hola, mundo!\n')
    archivo.write('Este es un archivo de texto.\n')

# 2
lineas = ['Primera línea.\n', 'Segunda línea.\n', 'Tercera línea.\n']

with open(ruta, 'w') as archivo:
    archivo.writelines(lineas)

# 3
with open(ruta, 'a') as archivo:
    archivo.write('Cuarta línea agregada.\n')

# 4
datos_binarios = bytes([120, 3, 255, 0, 100])  # Ejemplo de datos binarios

with open(ruta, 'wb') as archivo:
    archivo.write(datos_binarios)

# 5
with open('saludo.txt', 'w') as archivo:
    print('Hola, mundo!', file=archivo)
    print('Este es un archivo de texto.', file=archivo)

# 6
datos = [
    ['Nombre', 'Edad'],
    ['Alice', 23],
    ['Bob', 22],
    ['Charlie', 21]
]

with open('datos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)    