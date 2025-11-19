def multiplicar(a,b):
    """
    Multplica numeros usando suma
    """
    # elemento nulo
    if a == 0 or b == 0:
        return 0
    
    signo = 1
    
    #convertimos a positivo y registramos el signo
    if a < 0:
        signo = -signo
        a = -a
    if b < 0:
        signo = -signo
        b = -b
        
    # suma
    suma = 0
    for _ in range(b):
        suma += a
    
    return suma if signo > 0 else -suma
    
def dividir(a,b):
    """
    Divide numeros usando resta
    """
    # elemento nulo
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    
    signo = 1
    
    #convertimos a positivo y registramos el signo
    if a < 0:
        signo = -signo
        a = -a
    if b < 0:
        signo = -signo
        b = -b
        
    # resta
    cociente = 0
    while a >= b:
        a -= b
        cociente += 1
    
    residuo = a
    return cociente if signo > 0 else -cociente, residuo
    
def potencia(base,exponente):
    """
    Eleva un numero a otro usando multiplicacion
    """
    
    if exponente == 0:
        return 1
    if exponente < 0:
        raise ValueError("El exponente debe ser mayor o igual a cero")
    
    # manejo de signo
    signo = 1
    temp_base = base
    
    if base < 0:
        temp = exponente
        
        while temp > 1:
            temp -= 2
        if temp == 1:
            signo = -1
        base = -base
    
    # multiplicacion
    resultado = 1
    for _ in range(exponente):
        resultado = multiplicar(resultado, base)
    
    return resultado if signo > 0 else -resultado

def raiz_cuadrada(numero):
    """
    Calcula la raiz cuadrada de un numero usando la division
    """
    
    if numero < 0:
        raise ValueError("El numero debe ser mayor o igual a cero")
    if numero == 0:
        return 0
    
    contador = 0
    impar = 1
    
    while numero >= impar:
        numero -= impar
        contador += 1
        impar += 2
    
    return contador