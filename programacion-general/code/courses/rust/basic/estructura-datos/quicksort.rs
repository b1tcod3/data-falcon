//! Algoritmo de ordenamiento rápido en Rust (Quick Sort)
//!
//! Este módulo contiene la implementación del algoritmo Quick Sort.
//! Es uno de los algoritmos de ordenamiento más eficientes y utilizados,
//! basado en la estrategia "divide y vencerás".
//!
//! ## Funcionamiento
//! 1. Seleccionar un elemento como pivote
//! 2. Particionar: reorganizar el array para que todos los elementos menores
//!    que el pivote estén a la izquierda y los mayores a la derecha
//! 3. Aplicar recursivamente a las sublistas izquierda y derecha

/// Ordena un slice de forma ascendente utilizando Quick Sort.
///
/// Este algoritmo es **in-place** y muy eficiente para la mayoría de casos.
/// Utiliza el último elemento como pivote.
///
/// # Parámetros
/// * `arr` - Una referencia mutable a un slice de elementos comparables.
///
/// # Ejemplos
/// ```
/// let mut v = vec![64, 25, 12, 22, 11];
/// quicksort(&mut v);
/// assert_eq!(v, [11, 12, 22, 25, 64]);
/// ```
///
/// # Complejidad
/// * **Tiempo**: O(n log n) promedio, O(n²) peor caso (array ya ordenado)
/// * **Espacio**: O(log n) por la profundidad de recursión
pub fn quicksort<T: PartialOrd>(arr: &mut [T]) {
    if arr.is_empty() {
        return;
    }
    _quicksort(arr, 0, arr.len() - 1);
}

fn _quicksort<T: PartialOrd>(arr: &mut [T], left: usize, right: usize) {
    // Caso base: si el subarray tiene 0 o 1 elementos, ya está ordenado
    if left >= right {
        return;
    }

    //
    let pivot_pos = partition(arr, left, right);

    if pivot_pos > 0 {
        _quicksort(arr, left, pivot_pos - 1);
    }
    _quicksort(arr, pivot_pos + 1, right);
}

/// Particiona el array alrededor de un pivote y devuelve la posición final del pivote.
fn partition<T: PartialOrd>(arr: &mut [T], left: usize, right: usize) -> usize {
    // Elegimos el último elemento como pivote
    let pivot = right;
    // Índice para el elemento más pequeño
    let mut i = left;

    for j in left..right {
        //
        if arr[j] < arr[pivot] {
            arr.swap(i, j);
            i += 1;
        }
    }
    // Colocamos el pivote en su posición final
    arr.swap(i, pivot);
    i
}

//fn main() {
//    let mut numbers = vec![64, 25, 12, 22, 11];
//    println!("Array original: {:?}", numbers);
//    quicksort(&mut numbers);
//    println!("Array ordenado: {:?}", numbers);
//}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ordenar_lista_desordenada() {
        let mut v = vec![64, 25, 12, 22, 11];
        quicksort(&mut v);
        assert_eq!(v, [11, 12, 22, 25, 64]);
    }

    #[test]
    fn test_lista_ya_ordenada() {
        let mut v = vec![1, 2, 3, 4, 5];
        quicksort(&mut v);
        assert_eq!(v, [1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_lista_vacia() {
        let mut v: Vec<i32> = vec![];
        quicksort(&mut v);
        assert_eq!(v, []);
    }

    #[test]
    fn test_elementos_repetidos() {
        let mut v = vec![3, 1, 4, 1, 5, 9, 2, 6, 5];
        quicksort(&mut v);
        assert_eq!(v, [1, 1, 2, 3, 4, 5, 5, 6, 9]);
    }

    #[test]
    fn test_un_elemento() {
        let mut v = vec![42];
        quicksort(&mut v);
        assert_eq!(v, [42]);
    }

    #[test]
    fn test_dos_elementos() {
        let mut v = vec![2, 1];
        quicksort(&mut v);
        assert_eq!(v, [1, 2]);
    }
}
