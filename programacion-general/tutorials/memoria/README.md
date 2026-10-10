# Gestión de Memoria (C)

Ejemplo del manejo manual de memoria en C y de cómo se produce una **fuga de memoria** cuando se reserva espacio en el heap con `malloc` y se olvida liberarlo con `free`.

## Contenido

- `memoria-leak.c`: función que reserva memoria para 10 enteros y nunca la libera.

## Cómo ejecutar

```bash
cd programacion-general/tutorials/memoria
gcc memoria-leak.c -o memoria_leak
valgrind --leak-check=full ./memoria_leak   # valgrind reporta la fuga
```

Sin `free(lista)`, el bloque reservado queda inaccesible hasta que termina el programa: eso es una fuga de memoria.
