use cursive::views::Dialog;
use cursive::views::TextView;
use cursive::Cursive;

fn main() {
    let mut siv = cursive::default();

    siv.add_global_callback('q', |s| s.quit());
    siv.add_layer(
        Dialog::text("Have you finished working or not yet")
            .title("Personal Organizer")
            .button("Yes", |s| s.quit())
            .button("Not yet", |s| s.quit()),
    );

    siv.run();
}
