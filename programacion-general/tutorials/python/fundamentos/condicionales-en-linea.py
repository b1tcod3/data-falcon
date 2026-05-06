# Sintaxis: resultado = valor_si_true if condición else valor_si_false
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # "Mayor de edad"

# Más ejemplos
numero = -5
tipo = "positivo" if numero > 0 else "negativo" if numero < 0 else "cero"
print(f"El número es {tipo}")