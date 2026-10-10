def convertir_a_numero_seguro(valor):
    """Convierte un valor a número de forma segura"""
    try:
        # Intentar convertir a entero primero
        return int(valor)
    except ValueError:
        try:
            # Si falla, intentar convertir a float
            return float(valor)
        except ValueError:
            # Si todo falla, devolver None
            print(f"Error: '{valor}' no es un número válido")
            return None

# Ejemplos de uso
print(convertir_a_numero_seguro("42"))     # 42
print(convertir_a_numero_seguro("3.14"))   # 3.14
print(convertir_a_numero_seguro("abc"))    # None (con mensaje de error)

# Casting implícito (automático)
x = 5       # int
y = 2.0     # float
resultado = x + y  # Python convierte automáticamente: 5 + 2.0 = 7.0

# Casting explícito (manual)
a = "10"
b = "20"
suma = int(a) + int(b)  # Necesitamos convertir manualmente

print(f"Resultado implícito: {resultado}")
print(f"Tipo: {type(resultado)}")
print(f"Resultado explícito: {suma}")
print(f"Tipo: {type(suma)}")