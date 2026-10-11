# Ejercicio de decision: nota cualitativa
#
# A partir de una nota cuantitativa (entre 0.0 y 5.0) se obtiene la
# calificación cualitativa según la siguiente escala:
#   - 4.5 a 5.0   -> Excelente
#   - 4.0 a 4.49  -> Bueno
#   - 3.5 a 3.99  -> Aceptable
#   - 2.5 a 3.49  -> Insuficiente
#   - 0.0 a 2.49  -> Deficiente
#
# Datos de entrada: nota
# Datos de salida: calificación cualitativa


def nota_cualitativa(nota):
    """Clasifica una nota entre 0.0 y 5.0 en su rango cualitativo."""
    if nota >= 4.5:
        return "Excelente"
    if nota >= 4.0:
        return "Bueno"
    if nota >= 3.5:
        return "Aceptable"
    if nota >= 2.5:
        return "Insuficiente"
    return "Deficiente"


def main():
    nota = float(input("Ingrese la nota (0.0 a 5.0): "))

    if 0.0 <= nota <= 5.0:
        print(f"\nCalificación: {nota_cualitativa(nota)}")
    else:
        print("\nLa nota debe estar entre 0.0 y 5.0.")


if __name__ == "__main__":
    main()