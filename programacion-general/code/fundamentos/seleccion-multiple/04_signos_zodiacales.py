# Ejercicio de seleccion multiple: signos zodiacales
#
# Dado un signo zodiacal, indicar a qué elemento de la naturaleza pertenece:
#   - Fuego: Aries, Leo, Sagitario
#   - Tierra: Tauro, Virgo, Capricornio
#   - Aire: Géminis, Libra, Acuario
#   - Agua: Cáncer, Escorpión, Piscis
#
# Datos de entrada: signo zodiacal
# Datos de salida: elemento de la naturaleza


ELEMENTOS = {
    "Aries": "Fuego",
    "Leo": "Fuego",
    "Sagitario": "Fuego",
    "Tauro": "Tierra",
    "Virgo": "Tierra",
    "Capricornio": "Tierra",
    "Géminis": "Aire",
    "Libra": "Aire",
    "Acuario": "Aire",
    "Cáncer": "Agua",
    "Escorpión": "Agua",
    "Piscis": "Agua",
}


def elemento_zodiacal(signo):
    """Retorna el elemento del signo o None si no está contemplado."""
    return ELEMENTOS.get(signo)


def main():
    signo = input("Ingrese su signo zodiacal: ").strip().capitalize()

    elemento = elemento_zodiacal(signo)

    if elemento is None:
        print("\nSigno zodiacal no contemplado.")
    else:
        print(f"\nEl elemento de {signo} es: {elemento}")


if __name__ == "__main__":
    main()