# Ejercicio de seleccion multiple: calificacion de una nota
#
# Dada una nota de 1 a 5 imprimir la calificación correspondiente:
#   - 5 -> Excelente
#   - 4 -> Bueno
#   - 3 -> Aceptable
#   - 2 -> Insuficiente
#   - 1 -> Deficiente
#
# Datos de entrada: nota (1 a 5)
# Datos de salida: calificación


CALIFICACIONES = {5: "Excelente", 4: "Bueno", 3: "Aceptable", 2: "Insuficiente", 1: "Deficiente"}


def calificar(nota):
    """Retorna la calificación según la nota, o un mensaje de error."""
    if nota in CALIFICACIONES:
        return CALIFICACIONES[nota]
    return "Nota fuera de rango (debe estar entre 1 y 5)"


def main():
    nota = int(input("Ingrese la nota (1 a 5): "))

    print(f"\n{calificar(nota)}")


if __name__ == "__main__":
    main()