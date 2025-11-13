# Bucle for - ideal para iterar sobre secuencias
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}")

# Bucle for con range() - para contar
for i in range(1, 6):  # Del 1 al 5
    print(f"Número: {i}")

# Bucle while - se ejecuta mientras la condición sea verdadera
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Importante: actualizar la variable de control

# Bucle con break y continue
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numeros:
    if num == 5:
        print("¡Encontré el 5! Deteniendo...")
        break  # Sale del bucle
    if num % 2 == 0:
        continue  # Salta a la siguiente iteración
    print(f"Número impar: {num}")