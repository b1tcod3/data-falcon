fn main() {
    struct Book {
        title: String,
        author: String,
        pages: u32,
        available: bool,
    }

    struct User {
        username: String,
        email: String,
        active: bool,
        sing_in_count: u32,
    }

    let mut user1: User = User {
        username: String::from("john_doe"),
        email: String::from("john_doe@gmail.com"),
        active: true,
        sing_in_count: 1,
    };

    user1.email = String::from("john_doe2@gmail.com");
    println!("User email: {}", user1.email);

    fn build_user(username: String, email: String) -> User {
        User {
            username,
            email,
            active: true,
            sing_in_count: 1,
        }
    }

    let user2: User = User {
        email: String::from("mynewemail.com"),
        ..user1
    };
}
