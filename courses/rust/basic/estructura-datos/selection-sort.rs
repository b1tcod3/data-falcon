fn selection_sort<T: Ord>(arr: &mut [T]) {
    let n = arr.len();
    
    for i in 0..n {
        // Encontrar el índice del elemento mínimo en la sublista no ordenada
        let mut min_idx = i;
        for j in i + 1..n {
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
fn selection_sort_desc<T: Ord>(arr: &mut [T]) {
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
fn main() {
    // Ejemplos de uso
    let mut numbers = [64, 25, 12, 22, 11];
    println!("Array original: {:?}", numbers);

    selection_sort(&mut numbers);
    println!("Array ordenado: {:?}", numbers);
}
