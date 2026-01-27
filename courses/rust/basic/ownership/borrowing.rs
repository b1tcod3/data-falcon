fn main() {
    let mut x: i32 = 10;
    let y: &mut i32 = &mut x;

    *y += 5;
    // println!("Value of x: {}", x);
    println!("Value of y (borrowed from x): {}", y);
}
