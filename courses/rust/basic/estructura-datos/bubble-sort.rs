//! Algoritmo de ordenamiento Bubble Sort en rust
//!
//! Este módulo contiene implementación del algoritmo de ordenamiento Bubble Sort, que es un método
//! sencillo pero ineficiente para ordenar listas. El algoritmo funciona comparando cada par de
//! elementos adyacentes y cambiándolos de posición si están en el orden incorrecto. Este proceso
//! se repite hasta que la lista está ordenada.

/// ordena un slice utilizando el algoritmo de burbuja (Bubble Sort)
///
/// Este método es estable y tiene una optimización de "salida temprana"
/// si la lista se ordena antes de completar todas las interacciones.
///
/// # Parámetros
/// * `lista` - Una referencia mutable a un slice de elementos que implementan `PartialOrd`.
///
/// # Ejemplo
/// ```
/// let mut numeros = vec![64, 34, 25, 12, 22, 11, 90];
/// bubble_sort(&mut numeros);
/// assert_eq!(numeros, vec![11, 12, 22, 25, 34, 64, 90]);
/// ```
///
/// # Complejidad
/// * Tiempo: O(n^2) en el peor caso, O(n) en el mejor caso (cuando la lista ya está ordenada).
/// * Espacio: O(1)
pub fn bubble_sort<T: PartialOrd>(lista: &mut [T]) {
    let n = lista.len();

    for i in 0..n {
        // en cada pasada, el elemento más grande se mueve al final
        let mut intercambiado = false;
        for j in 0..(n - i - 1) {
            if lista[j] > lista[j + 1] {
                // intercambiamos los elementos usando el método swap de rust
                lista.swap(j, j + 1);
                intercambiado = true;
            }
        }
        if !intercambiado {
            break; // la lista ya está ordenada
        }
    }
}

fn main() {
    let mut numeros = vec![64, 34, 25, 12, 22, 11, 90];
    println!("Lista original: {:?}", numeros);
    bubble_sort(&mut numeros);
    println!("Lista ordenada: {:?}", numeros);
}
