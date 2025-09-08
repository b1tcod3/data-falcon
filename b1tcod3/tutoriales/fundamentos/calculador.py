# Paso 1: Importaciones y constantes
import math

# Paso 2: Variables globales y constantes
OPERACIONES_DISPONIBLES = {
    '1': '+', '2': '-', '3': '*', '4': '/',
    '5': '^', '6': '√', '7': '%'
}

# Paso 4: Funciones definidas por el usuario
def mostrar_menu():
    """
    Paso 4: Función que muestra el menú de operaciones disponibles
    Utiliza: strings, concatenación, print()
    """
    print("\n" + "="*40)
    print("🧮 CALCULADORA AVANZADA")
    print("="*40)
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potencia (^)")
    print("6. Raíz cuadrada (√)")
    print("7. Porcentaje (%)")
    print("8. Historial")
    print("9. Salir")
    print("="*40)

def obtener_numero(mensaje):
    """
    Paso 4: Función que obtiene un número válido del usuario
    Utiliza: Paso 6 (manejo de errores), Paso 3 (bucles while), Paso 2 (casting)
    """
    while True:  # Paso 3: Bucle while
        try:  # Paso 6: Manejo de excepciones
            entrada = input(mensaje)  # Paso 2: String
            return float(entrada)  # Paso 2: Casting a float
        except ValueError:  # Paso 6: Captura de excepciones específicas
            print("❌ Error: Ingresa un número válido")

def calcular(operacion, num1, num2=None):
    """
    Paso 4: Función que realiza el cálculo según la operación seleccionada
    Utiliza: Paso 3 (condicionales), Paso 6 (manejo de errores), Paso 2 (strings, números)
    """
    try:  # Paso 6: Bloque try-except
        # Paso 3: Condicionales if-elif-else
        if operacion == '+':
            return num1 + num2, f"{num1} + {num2}"
        elif operacion == '-':
            return num1 - num2, f"{num1} - {num2}"
        elif operacion == '*':
            return num1 * num2, f"{num1} × {num2}"
        elif operacion == '/':
            if num2 == 0:  # Paso 3: Condicional anidado
                raise ZeroDivisionError("No se puede dividir por cero")  # Paso 6: Lanzar excepciones
            return num1 / num2, f"{num1} ÷ {num2}"
        elif operacion == '^':
            return num1 ** num2, f"{num1}^{num2}"
        elif operacion == '√':
            if num1 < 0:  # Paso 3: Validación con condicional
                raise ValueError("No se puede calcular raíz cuadrada de número negativo")
            return math.sqrt(num1), f"√{num1}"
        elif operacion == '%':
            return (num1 * num2) / 100, f"{num1}% de {num2}"
        else:
            raise ValueError("Operación no válida")
    except Exception as e:  # Paso 6: Captura general de excepciones
        raise e

def calculadora():
    """
    Paso 4: Función principal de la calculadora
    Utiliza: Paso 5 (listas), Paso 3 (bucles while, condicionales), Paso 6 (manejo de errores)
    """
    historial = []  # Paso 5: Lista para almacenar operaciones

    print("¡Bienvenido a la Calculadora Avanzada!")

    while True:  # Paso 3: Bucle while principal
        mostrar_menu()

        try:  # Paso 6: Manejo de errores
            opcion = input("Selecciona una opción (1-9): ").strip()  # Paso 2: String

            # Paso 3: Condicionales if-elif-else
            if opcion == '9':
                print("¡Gracias por usar la calculadora!")
                break  # Paso 3: Sentencia break

            elif opcion == '8':
                # Mostrar historial - Paso 5: Trabajar con listas
                if not historial:  # Paso 3: Condicional con operador lógico
                    print("📝 No hay operaciones en el historial")
                else:
                    print("\n📋 Historial de operaciones:")
                    # Paso 3: Bucle for con enumerate
                    for i, (expresion, resultado) in enumerate(historial[-10:], 1):
                        print(f"{i}. {expresion} = {resultado}")
                continue  # Paso 3: Sentencia continue

            # Paso 3: Condicional con operador 'in' (pertenece a)
            if opcion in ['6']:  # Raíz cuadrada
                num1 = obtener_numero("Ingresa el número: ")
                resultado, expresion = calcular('√', num1)
            else:
                # Operaciones que requieren dos números
                num1 = obtener_numero("Ingresa el primer número: ")
                num2 = obtener_numero("Ingresa el segundo número: ")

                # Paso 5: Diccionario para mapear opciones a operaciones
                operaciones = {
                    '1': '+', '2': '-', '3': '*', '4': '/',
                    '5': '^', '7': '%'
                }

                # Paso 3: Condicional con operador 'not in'
                if opcion not in operaciones:
                    print("❌ Opción no válida")
                    continue

                operacion = operaciones[opcion]  # Paso 5: Acceso a diccionario
                resultado, expresion = calcular(operacion, num1, num2)

            # Mostrar resultado
            print(f"\n✅ Resultado: {expresion} = {resultado}")

            # Paso 5: Agregar tupla al historial (combinando lista con tupla)
            historial.append((expresion, resultado))

        except Exception as e:  # Paso 6: Captura de excepciones
            print(f"❌ Error: {str(e)}")
            continue

        # Paso 3: Condicional con operador de comparación
        continuar = input("\n¿Quieres realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break

def calculadora():
    """
    Paso 4: Función principal de la calculadora
    Utiliza: Paso 5 (listas), Paso 3 (bucles while, condicionales), Paso 6 (manejo de errores)
    """
    historial = []  # Paso 5: Lista para almacenar operaciones

    print("¡Bienvenido a la Calculadora Avanzada!")

    while True:  # Paso 3: Bucle while principal
        mostrar_menu()

        try:  # Paso 6: Manejo de errores
            opcion = input("Selecciona una opción (1-9): ").strip()  # Paso 2: String

            # Paso 3: Condicionales if-elif-else
            if opcion == '9':
                print("¡Gracias por usar la calculadora!")
                break  # Paso 3: Sentencia break

            elif opcion == '8':
                # Mostrar historial - Paso 5: Trabajar con listas
                if not historial:  # Paso 3: Condicional con operador lógico
                    print("📝 No hay operaciones en el historial")
                else:
                    print(f"\n📋 Historial de operaciones ({len(historial)} total):")
                    # Mostrar últimas 10 operaciones
                    for i, (expresion, resultado) in enumerate(historial[-10:], len(historial)-9):
                        print(f"{i}. {expresion} = {resultado}")
                continue  # Paso 3: Sentencia continue

            # Paso 3: Condicional con operador 'in' (pertenece a)
            if opcion in ['6']:  # Raíz cuadrada
                num1 = obtener_numero("Ingresa el número: ")
                resultado, expresion = calcular('√', num1)
            else:
                # Operaciones que requieren dos números
                num1 = obtener_numero("Ingresa el primer número: ")
                num2 = obtener_numero("Ingresa el segundo número: ")

                # Paso 5: Diccionario para mapear opciones a operaciones
                operaciones = {
                    '1': '+', '2': '-', '3': '*', '4': '/',
                    '5': '^', '7': '%'
                }

                # Paso 3: Condicional con operador 'not in'
                if opcion not in operaciones:
                    print("❌ Opción no válida")
                    continue

                operacion = operaciones[opcion]  # Paso 5: Acceso a diccionario
                resultado, expresion = calcular(operacion, num1, num2)

            # Mostrar resultado
            print(f"\n✅ Resultado: {expresion} = {resultado}")

            # Paso 5: Agregar tupla al historial (combinando lista con tupla)
            historial.append((expresion, resultado))

        except Exception as e:  # Paso 6: Captura de excepciones
            print(f"❌ Error: {str(e)}")
            continue

        # Paso 3: Condicional con operador de comparación
        continuar = input("\n¿Quieres realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break

# Paso 3: Condicional para ejecutar solo cuando se llama directamente
if __name__ == "__main__":
    calculadora()