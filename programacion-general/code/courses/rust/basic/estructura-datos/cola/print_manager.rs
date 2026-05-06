struct PrintManager {
    queue: Vec<String>,
}

impl PrintManager {
    fn new() -> Self {
        PrintManager { queue: Vec::new() }
    }

    fn queue_print_job(&mut self, document: String) {
        self.queue.push(document);
    }

    fn run(&mut self) {
        while !self.queue.is_empty() {
            // The Rust equivalent of Ruby's shift is remove(0)
            let document = self.queue.remove(0);
            self.print(document);
        }
    }

    fn print(&self, document: String) {
        println!("{}", document);
    }
}

fn main() {
    let mut pm = PrintManager::new();
    pm.queue_print_job(String::from("Documento 1"));
    pm.queue_print_job(String::from("Documento 2"));
    pm.queue_print_job(String::from("Documento 3"));
    pm.run();
}
