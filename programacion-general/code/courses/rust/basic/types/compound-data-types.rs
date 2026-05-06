// compund data types
//
fn main() {
    // arraysº
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    println!("Array: {:?}", numbers);

    let fruits: [&str; 3] = ["apple", "banana", "cherry"];
    println!("All Fruits: {:?}", fruits);
    println!("First Fruit: {:}", fruits[0]);

    // tuples
    let human: (String, i32, bool) = ("Alice".to_string(), 30, true);
    println!("Human tuples: {:?}", human);

    //mix tuples
    let mix_tuples = ("Kratos", 23, true, [1, 2, 3]);
    println!("Mix tuples: {:?}", mix_tuples);

    // slices
    let number_slice: &[i32] = &[1, 2, 3, 4, 5];
    println!("Number Slice: {:?}", number_slice);

    let animals_slice: &[&str] = &["Lion", "Tiger", "Bear"];
    println!("Animal Slice: {:?}", animals_slice);

    let books_slice: &[&String] = &[
        &"IT".to_string(),
        &"Harry Potter".to_string(),
        &"Bible".to_string(),
    ];
    println!("Books Slice: {:?}", books_slice);

    let mut stone_cold: String = String::from("Hell, ");
    println!("Stone Cold Says: {}", stone_cold);
    stone_cold.push_str("YEAH!");
    println!("Stone Cold Says: {}", stone_cold);

    let string: String = String::from("Hello, World!");
    let string_slice: &str = &string[7..12];
    println!("String Slice: {}", string_slice);
}
