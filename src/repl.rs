use std::io::{self, Write};
mod persian_hex;

fn main() {
    let mut number = String::new();
    let mut hex = persian_hex::PersianHex::new();

    persian_hex::init_persian_hex(&mut hex);

    print!("Enter a non-negative integer: ");
    io::stdout().flush().unwrap();

    io::stdin().read_line(&mut number).unwrap();
    let number: i32 = match number.trim().parse() {
        Ok(n) if n >= 0 => n,
        _ => {
            println!("Error: Please enter a valid integer.");
            return;
        }
    };

    persian_hex::set_mode(&mut hex, persian_hex::Digits::English);
    // persian_hex::set_mode(&mut hex, persian_hex::Digits::Persian);

    persian_hex::calculate(&mut hex, number);
}
