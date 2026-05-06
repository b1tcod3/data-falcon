fn main() {
    hello_world();
    tell_height(1212);
    human_id("Alice", 30, 165.5);

    let _X: i32 = {
        let price: i32 = 5;
        let qty: i32 = 10;
        price * qty
    };
    println!("Total price is: {}", _X);
    println!("Sum is: {}", add(10, 20));
}

fn hello_world() {
    println!("Hello, world!");
}

fn tell_height(height: u32) {
    println!("Your height is {} cm", height);
}

fn human_id(name: &str, age: u8, height: f32) {
    println!("Name: {}, Age: {}, Height: {} cm", name, age, height);
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}
