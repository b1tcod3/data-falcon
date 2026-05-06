use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    let team_name = String::from("Blue");
    let score = scores.get(&team_name);

    match score {
        Some(&value) => println!("The score for {} is {}", team_name, value),
        None => println!("No score found for {}", team_name),
    }

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
}
