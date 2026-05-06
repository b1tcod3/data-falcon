//! Algoritmo de ordenamiento por selección en Rust (selection sort)
//!
//! Este módulo contiene implementaciones del algoritmo Selection Sort.
//! A diferencia de Bubble Sort, este algoritmo minimiza el número de intercambios
//! realizados, haciendo un máximo de **n-1** swaps.
//!
//! ## Funcionamiento
//! El algoritmo divide la lista en dos partes: una sublista de elementos ya ordenados
//! y otra de elementos por ordenar. En cada iteración, busca el elemento más pequeño
//! (o más grande) de la sublista desordenada y lo intercambia con el primer
//! elemento de dicha sublista.

/// Ordena un slice de forma ascendente utilizando Selection Sort.
///
/// Este algoritmo es **inestable** (puede cambiar el orden relativo de elementos iguales)
/// pero es eficiente en memoria ya que opera *in-place*.
///
/// # Parámetros
/// * `arr` - Una referencia mutable a un slice de elementos comparables.
///
/// # Ejemplos
/// ```
/// let mut v = vec![64, 25, 12, 22, 11];
/// selection_sort(&mut v);
/// assert_eq!(v, [11, 12, 22, 25, 64]);
/// ```
///
/// # Complejidad
/// * **Tiempo**: $O(n^2)$ en todos los casos (mejor, promedio y peor).
/// * **Espacio**: $O(1)$ (no requiere memoria adicional significativa).
pub fn selection_sort<T: PartialOrd>(arr: &mut [T]) {
    let n = arr.len();

    for i in 0..n {
        // Encontrar el índice del elemento mínimo en la sublista no ordenada
        // asumimos que el primer elemento no ordenado es el mínimo
        let mut min_idx = i;
        for j in i + 1..n {
            // si encontramos un elemento
            if arr[j] < arr[min_idx] {
                min_idx = j;
            }
        }

        // Intercambiar el elemento mínimo con el primer elemento no ordenado
        if i != min_idx {
            arr.swap(i, min_idx);
        }
    }
}

// Versión con genéricos y orden descendente
fn selection_sort_desc<T: PartialOrd>(arr: &mut [T]) {
    let n = arr.len();

    for i in 0..n {
        let mut max_idx = i;
        for j in i + 1..n {
            if arr[j] > arr[max_idx] {
                max_idx = j;
            }
        }

        if i != max_idx {
            arr.swap(i, max_idx);
        }
    }
}
//fn main() {
//    // Ejemplos de uso
//    let mut numbers = [64, 25, 12, 22, 11];
//    println!("Array original: {:?}", numbers);
//
//    selection_sort(&mut numbers);
//    println!("Array ordenado: {:?}", numbers);
//}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ordenar_lista_desordenada() {
        let mut v = vec![64, 25, 12, 22, 11];
        selection_sort(&mut v);
        assert_eq!(v, [11, 12, 22, 25, 64]);
    }

    #[test]
    fn test_list_ya_ordenada() {
        let mut v = vec![1, 2, 3, 4, 5];
        selection_sort(&mut v);
        assert_eq!(v, vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_lista_vacia() {
        let mut v: Vec<i32> = vec![];
        selection_sort(&mut v);
        assert_eq!(v, vec![]);
    }
}
