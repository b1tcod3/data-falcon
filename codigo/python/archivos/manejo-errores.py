
try:
    with open('datos.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    # Captura el error si el archivo no existe.
    print("Error: El archivo no se encontró.")
except IOError:
    #  Maneja otros errores de entrada/salida, como problemas al abrir o leer el archivo.
    print("Error: Ocurrió un problema al intentar leer el archivo.")
except Exception as e:
    # Captura cualquier otro error.
    print("Error: Ocurrió un error inesperado.")
    print(e)