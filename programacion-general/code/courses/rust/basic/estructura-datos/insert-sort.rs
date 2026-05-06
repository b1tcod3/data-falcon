//! # Algoritmo de Ordenamiento por Inserción (Insertion Sort)
//!
//! Este módulo contiene la implementación del algoritmo Insertion Sort.
//! Es un algoritmo eficiente para conjuntos de datos pequeños o listas que
//! ya se encuentran casi ordenadas.
//!
//! ## Funcionamiento
//! Recorre la lista de izquierda a derecha, tomando cada elemento y "desplazándolo"
//! hacia atrás hasta que encuentra su posición correcta entre los elementos
//! que ya han sido procesados.
pub fn insertion_sort<T: PartialOrd>(lista: &mut [T]) {
    let n = lista.len();

    // Empezamos desde el segundo elemento (índice 1)
    for i in 1..n {
        // Guardamos el elemento actual que vamos a insertar
        let mut j = i;

        // Movemos los elementos mayores hacia la derecha
        // para hacer espacio para el elemento actual
        while j > 0 && lista[j] < lista[j - 1] {
            lista.swap(j, j - 1);
            j -= 1;
        }
    }
}

// Versión con genéricos y orden descendente
fn insertion_sort_desc<T: PartialOrd>(lista: &mut [T]) {
    let n = lista.len();

    for i in 1..n {
        let mut j = i;

        // Movemos los elementos menores hacia la derecha
        while j > 0 && lista[j] > lista[j - 1] {
            lista.swap(j, j - 1);
            j -= 1;
        }
    }
}

fn main() {
    // Ejemplos de uso
    let mut numeros = vec![64, 34, 25, 12, 22, 11, 90];
    println!("Lista original: {:?}", numeros);

    insertion_sort(&mut numeros);
    println!("Lista ordenada: {:?}", numeros);
}
