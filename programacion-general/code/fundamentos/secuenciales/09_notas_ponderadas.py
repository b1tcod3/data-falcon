# Ejercicio secuencial: notas ponderadas
#
# La nota definitiva de un grupo de estudiantes se calcula así:
#   - 15% el promedio de dos talleres
#   - 30% el promedio de tres evaluaciones
#   - 30% el promedio del trabajo final (una calificación)
#   - 25% el promedio de cuatro seguimientos
# Se pide calcular e imprimir la nota definitiva de cada estudiante.
#
# Datos de entrada: notas de talleres, evaluaciones, trabajo y seguimientos
# Datos de salida: nota definitiva


PESO_TALLERES = 0.15
PESO_EVALUACIONES = 0.30
PESO_TRABAJO = 0.30
PESO_SEGUIMIENTOS = 0.25


def nota_definitiva(talleres, evaluaciones, trabajo, seguimientos):
    """Calcula la nota definitiva con los pesos del sistema."""
    prom_talleres = sum(talleres) / len(talleres)
    prom_evaluaciones = sum(evaluaciones) / len(evaluaciones)
    prom_seguimientos = sum(seguimientos) / len(seguimientos)

    definitiva = (
        prom_talleres * PESO_TALLERES
        + prom_evaluaciones * PESO_EVALUACIONES
        + trabajo * PESO_TRABAJO
        + prom_seguimientos * PESO_SEGUIMIENTOS
    )

    return definitiva


def ingredientes(mensaje, cantidad):
    """Pide `cantidad` notas y retorna la lista de valores."""
    notas = []
    for i in range(1, cantidad + 1):
        nota = float(input(f"{mensaje} {i}: "))
        notas.append(nota)
    return notas


def main():
    talleres = ingredientes("Nota taller", 2)
    evaluaciones = ingredientes("Nota evaluación", 3)
    trabajo = float(input("Nota trabajo final: "))
    seguimientos = ingredientes("Nota seguimiento", 4)

    definitiva = nota_definitiva(talleres, evaluaciones, trabajo, seguimientos)

    print(f"\nNota definitiva: {definitiva:,.2f}")


if __name__ == "__main__":
    main()