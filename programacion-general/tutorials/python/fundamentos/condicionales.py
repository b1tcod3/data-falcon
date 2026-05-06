# Ejemplo básico de condicional
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar y conducir")
elif edad >= 13:
    print("Eres adolescente")
    print("Puedes usar redes sociales con supervisión")
else:
    print("Eres niño")
    print("Disfruta tu infancia")

# Condicional anidado
temperatura = 25
lluvia = False

if temperatura > 20:
    if not lluvia:
        print("¡Día perfecto para salir!")
    else:
        print("Hace calor pero llueve")
else:
    print("Hace frío, mejor quédate en casa")
    
