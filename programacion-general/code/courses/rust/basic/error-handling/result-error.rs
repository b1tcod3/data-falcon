fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero error"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    let result = divide(10.0, 0.0);

    match result {
        Ok(x) => println!("Result is {}", x),
        Err(e) => println!("Error: {}", e),
    }
}
