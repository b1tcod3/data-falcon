fn divide(numerator: f64, denominator: f64) -> Option<f64> {
    if denominator == 0.0 {
        None
    } else {
        Some(numerator / denominator)
    }
}

fn main() {
    let result = divide(232.3, 0.0);

    match result {
        Some(x) => println!("Result: {},", x),
        None => println!("Cannot divede by zero:!"),
    }
}
