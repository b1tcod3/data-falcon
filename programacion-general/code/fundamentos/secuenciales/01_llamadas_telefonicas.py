# Ejercicio secuencial: llamadas telefonicas
#
# Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer
# operador y dos a un segundo. El cliente desea conocer el costo de cada
# llamada, el costo total de las llamadas a cada operador y el total de las
# cuatro llamadas.
#
# Datos de entrada:
#   M1_Op1, M2_Op1  -> minutos de las llamadas al primer operador
#   M1_Op2, M2_Op2  -> minutos de las llamadas al segundo operador
#   Val_Op1, Val_Op2 -> valor por minuto de cada operador
# Datos de salida:
#   costo de cada llamada, costo total por operador y costo total


def costo_llamadas(min_op1_1, min_op1_2, min_op2_1, min_op2_2, val_op1, val_op2):
    """Calcula el costo de cada llamada, por operador y el total."""
    llamada1 = min_op1_1 * val_op1
    llamada2 = min_op1_2 * val_op1
    llamada3 = min_op2_1 * val_op2
    llamada4 = min_op2_2 * val_op2

    total_op1 = llamada1 + llamada2
    total_op2 = llamada3 + llamada4
    total = total_op1 + total_op2

    return llamada1, llamada2, llamada3, llamada4, total_op1, total_op2, total


def main():
    m1_op1 = int(input("Minutos primera llamada (operador 1): "))
    m2_op1 = int(input("Minutos segunda llamada (operador 1): "))
    m1_op2 = int(input("Minutos primera llamada (operador 2): "))
    m2_op2 = int(input("Minutos segunda llamada (operador 2): "))
    val_op1 = float(input("Valor por minuto operador 1: "))
    val_op2 = float(input("Valor por minuto operador 2: "))

    c1, c2, c3, c4, tot_op1, tot_op2, total = costo_llamadas(
        m1_op1, m2_op1, m1_op2, m2_op2, val_op1, val_op2
    )

    print("\n=== Costo de cada llamada ===")
    print(f"Llamada 1: $ {c1:,.2f}")
    print(f"Llamada 2: $ {c2:,.2f}")
    print(f"Llamada 3: $ {c3:,.2f}")
    print(f"Llamada 4: $ {c4:,.2f}")
    print("\n=== Costo por operador ===")
    print(f"Operador 1: $ {tot_op1:,.2f}")
    print(f"Operador 2: $ {tot_op2:,.2f}")
    print(f"\nTotal de las cuatro llamadas: $ {total:,.2f}")


if __name__ == "__main__":
    main()