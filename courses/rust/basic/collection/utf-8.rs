fn main() {
    let s = "whatever".to_string();
    let s = String::from("initial text");
    let mut s = String::from("hello");
    s.push_str(" more text");
    s.push('!');

    println!("{}", s);

    let s2 = String::from(". Good");

    let s3 = s + &s2;

    println!("the value s3 is {}", s3);

    let salam = "السلام عليكم";
    let salut = "Salut";

    let full_message = format!("{salam} {salut}");
    println!("full message: {}", full_message);
}
