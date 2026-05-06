fn main(){

    struct Color(u8, u8, u8);
    struct Point(i32, i32, i32);

    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);

    println!("Black color - R: {}, G: {}, B: {}", black.0, black.1, black.2);
    println!("Origin point - X: {}, Y: {}, Z: {}", origin.0, origin.1, origin.2);
}
