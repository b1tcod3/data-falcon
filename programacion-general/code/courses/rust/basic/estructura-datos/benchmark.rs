#[path = "bubble-sort.rs"]
mod bubble_sort;

#[path = "selection-sort.rs"]
mod selection_sort;

#[path = "insert-sort.rs"]
mod insert_sort;

use std::time::{Duration, Instant};

fn generar_peor_caso(n: usize) -> Vec<i32> {
    (0..n as i32).rev().collect()
}

fn formatear_duracion(d: Duration) -> String {
    if d.as_secs() > 0 {
        format!("{:.4} s", d.as_secs_f64())
    } else if d.as_millis() > 0 {
        format!("{:.4} ms", d.as_millis())
    } else {
        format!("{:.4} µs", d.as_micros())
    }
}

fn benchmark<F>(n: usize, mut f: F) -> Duration
where
    F: FnMut(&mut [i32]),
{
    let mut lista = generar_peor_caso(n);
    let inicio = Instant::now();
    f(&mut lista);
    inicio.elapsed()
}

fn main() {
    let tamanyos = [100, 500, 1_000, 5_000, 10_000];

    println!("\n{:=^70}", " Benchmark de Algoritmos de Ordenamiento ");
    println!(
        "{:<15} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}",
        "Algoritmo", "100", "500", "1K", "5K", "10K"
    );
    println!("{:-<70}", "");

    println!(
        "{:<15} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}",
        "Bubble Sort",
        formatear_duracion(benchmark(100, |arr| bubble_sort::bubble_sort(arr))),
        formatear_duracion(benchmark(500, |arr| bubble_sort::bubble_sort(arr))),
        formatear_duracion(benchmark(1_000, |arr| bubble_sort::bubble_sort(arr))),
        formatear_duracion(benchmark(5_000, |arr| bubble_sort::bubble_sort(arr))),
        formatear_duracion(benchmark(10_000, |arr| bubble_sort::bubble_sort(arr)))
    );

    println!(
        "{:<15} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}",
        "Selection Sort",
        formatear_duracion(benchmark(100, |arr| selection_sort::selection_sort(arr))),
        formatear_duracion(benchmark(500, |arr| selection_sort::selection_sort(arr))),
        formatear_duracion(benchmark(1_000, |arr| selection_sort::selection_sort(arr))),
        formatear_duracion(benchmark(5_000, |arr| selection_sort::selection_sort(arr))),
        formatear_duracion(benchmark(10_000, |arr| selection_sort::selection_sort(arr)))
    );

    println!(
        "{:<15} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}",
        "Insert Sort",
        formatear_duracion(benchmark(100, |arr| insert_sort::insertion_sort(arr))),
        formatear_duracion(benchmark(500, |arr| insert_sort::insertion_sort(arr))),
        formatear_duracion(benchmark(1_000, |arr| insert_sort::insertion_sort(arr))),
        formatear_duracion(benchmark(5_000, |arr| insert_sort::insertion_sort(arr))),
        formatear_duracion(benchmark(10_000, |arr| insert_sort::insertion_sort(arr)))
    );
}