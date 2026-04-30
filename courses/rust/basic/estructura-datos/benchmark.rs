#[path = "bubble-sort.rs"]
mod bubble_sort;

use std::time::{Duration, Instant};

fn generar_pero_caso(n: usize) -> Vec<i32> {
    (0..n as i32).rev().collect()
}
fn formatear_duracion(d: Duration) -> String {
    if d.as_secs() > 0 {
        format!("{:.4 } s", d.as_secs_f64())
    } else if d.as_millis() > 0 {
        format!("{} ms", d.as_millis())
    } else {
        format!("{} ms", d.as_micros())
    }
}

fn main() {
    let tamanyos = [10, 100, 1000, 10_000, 100_000];

    // Encabezados de la tabla
    println!("\n{:=^45}", " Benchmark de Bubble Sort ");
    println!("{:<15} | {:<20}", "Elementos (N)", "Tiempo de ejecución");
    println!("{:-<45}", "");

    for &n in tamanyos.iter() {
        let mut lista = generar_pero_caso(n);
        let inicio = Instant::now();
        bubble_sort::bubble_sort(&mut lista);
        let duracion = inicio.elapsed();

        //formatear el tiempo para que sea legible
        let tiempo_formateado = formatear_duracion(duracion);

        //  Imprimir fila con alineación precisa
        println!("{:<15} | {:<25}", n, tiempo_formateado);
    }
}
