fn main() {
    let v: Vec<i32> = Vec::new();
    let v2: Vec<i32> = vec![1, 2, 3];

    let mut number_vectors: Vec<i32> = Vec::new();
    number_vectors.push(5);
    number_vectors.push(2);

    println!("{:?}", number_vectors);

    let third: &i32 = &v2[2];
    println!("The third element is: {}", third);

    let two = number_vectors.get(1);

    match two {
        Some(value) => println!("The second element is: {}", value),
        None => println!("There is no second element."),
    }
}
