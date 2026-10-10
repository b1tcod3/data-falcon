#include <stdlib.h>

void crear_fuga() {
    // Reservamos espacio para 10 enteros en el "heap"
    int *lista = malloc(10 * sizeof(int));

    lista[0] = 42; 
    // ¡Oh no! Olvidamos usar free(lista) antes de que termine la función
}

int main() {
    crear_fuga();
    return 0;
}
