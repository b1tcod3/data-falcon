# Abrir un archivo en modo lectura
archivo = open('codigo/python/archivos/datos.txt', 'r')

# Realizar operaciones con el archivo
contenido = archivo.read()
print(contenido)

# Cerrar el archivo
archivo.close()