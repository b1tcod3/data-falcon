// Ejercicio secuencial: llamadas telefonicas (version PSeInt)
//
// Un cliente de telefonia celular realiza cuatro llamadas: dos a un primer
// operador y dos a un segundo. El cliente desea conocer el costo de cada
// llamada, el costo total de las llamadas a cada operador y el total de las
// cuatro llamadas.
//
// Datos de entrada: minutos y valor por minuto de cada operador.
// Datos de salida: costo de cada llamada, total por operador y total general.

Algoritmo LlamadasTelefonicas
    Definir m1_op1, m2_op1, m1_op2, m2_op2 Como Real
    Definir val_op1, val_op2 Como Real
    Definir llamada1, llamada2, llamada3, llamada4 Como Real
    Definir total_op1, total_op2, total Como Real

    Escribir "Minutos primera llamada (operador 1):"
    Leer m1_op1
    Escribir "Minutos segunda llamada (operador 1):"
    Leer m2_op1
    Escribir "Minutos primera llamada (operador 2):"
    Leer m1_op2
    Escribir "Minutos segunda llamada (operador 2):"
    Leer m2_op2
    Escribir "Valor por minuto operador 1:"
    Leer val_op1
    Escribir "Valor por minuto operador 2:"
    Leer val_op2

    llamada1 <- m1_op1 * val_op1
    llamada2 <- m2_op1 * val_op1
    llamada3 <- m1_op2 * val_op2
    llamada4 <- m2_op2 * val_op2

    total_op1 <- llamada1 + llamada2
    total_op2 <- llamada3 + llamada4
    total <- total_op1 + total_op2

    Escribir ""
    Escribir "=== Costo de cada llamada ==="
    Escribir "Llamada 1: $ ", llamada1
    Escribir "Llamada 2: $ ", llamada2
    Escribir "Llamada 3: $ ", llamada3
    Escribir "Llamada 4: $ ", llamada4
    Escribir ""
    Escribir "=== Costo por operador ==="
    Escribir "Operador 1: $ ", total_op1
    Escribir "Operador 2: $ ", total_op2
    Escribir ""
    Escribir "Total de las cuatro llamadas: $ ", total
FinAlgoritmo
