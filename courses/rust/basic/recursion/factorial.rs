fn factorial(number: u64) -> u64 {
    match number {
        1 => 1,
        _ => number * factorial(number - 1),
    }
}

fn main() {
    println!("{}", factorial(5));
}