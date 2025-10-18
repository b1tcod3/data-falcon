# Ejemplo práctico: calculadora con entrada del usuario
def sumar_numeros():
    # La entrada siempre es string
    num1 = input("Primer número: ")   # "5"
    num2 = input("Segundo número: ")  # "3"

    # Necesitamos casting para operar
    resultado = int(num1) + int(num2)  # 5 + 3 = 8

    # Casting para mostrar resultado
    print("Resultado: " + str(resultado))  # "Resultado: 8"

sumar_numeros()