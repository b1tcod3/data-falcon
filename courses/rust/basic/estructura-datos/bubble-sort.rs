fn bubble_sort<T: PartialOrd>(lista: &mut [T]) {
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
