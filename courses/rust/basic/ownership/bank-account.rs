fn main() {
    println!("Bank Account Management System");
    let mut account = BankAccount {
        owner: String::from("Alice"),
        balance: 1000.0,
    };
    // immutable borrow occurs here
    account.check_balance();
    // mutable borrow occurs here
    account.withdraw(200.0);
    account.check_balance();
}

struct BankAccount {
    owner: String,
    balance: f64,
}
impl BankAccount {
    fn withdraw(&mut self, amount: f64) {
        println!("Withdrawing ${} from {}", amount, self.owner);
        self.balance -= amount;
    }

    fn check_balance(&self) {
        println!(
            "Checking owner by {} has a  balance of {}",
            self.owner, self.balance
        );
    }
}
