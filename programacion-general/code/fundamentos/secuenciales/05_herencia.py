# Ejercicio secuencial: reparto de una herencia
#
# Una madre y sus cuatro hijos reciben una herencia. El testamento establece:
#   - a la esposa le corresponde el 40% del total heredado
#   - el resto se distribuye entre los cuatro hijos con los porcentajes
#     30%, 20%, 40% y 10% respectivamente (sobre el resto)
# Se necesita mostrar lo que le corresponde a la madre, a los hijos en
# general y a cada uno de ellos.
#
# Datos de entrada: total_heredado
# Datos de salida: madre, cada hijo, total de los hijos


PORC_ESPOSA = 0.40
PORC_HIJOS = [0.30, 0.20, 0.40, 0.10]


def reparto_herencia(total_heredado):
    """Calcula lo que recibe la madre y cada uno de los cuatro hijos."""
    madre = total_heredado * PORC_ESPOSA
    resto = total_heredado - madre

    hijos = [resto * porcentaje for porcentaje in PORC_HIJOS]
    total_hijos = sum(hijos)

    return madre, hijos, resto, total_hijos


def main():
    total = float(input("Total de la herencia: "))

    madre, hijos, resto, total_hijos = reparto_herencia(total)

    print("\n=== Reparto de la herencia ===")
    print(f"Madre (40%): $ {madre:,.2f}")
    print(f"Resto a repartir (60%): $ {resto:,.2f}")
    for i, hijo in enumerate(hijos, start=1):
        print(f"Hijo {i} ({PORC_HIJOS[i - 1] * 100:.0f}% del resto): $ {hijo:,.2f}")
    print(f"Total para los hijos: $ {total_hijos:,.2f}")


if __name__ == "__main__":
    main()