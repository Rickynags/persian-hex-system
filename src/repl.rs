// cargo build --release
// cargo run
use std::io::{self, Write};

mod persian_hex;
use crate::persian_hex::persian_hex::{PersianHex, init_persian_hex, set_mode, Digits, calculate};

fn main() {
    let mut number = String::new();
    let mut hex = PersianHex::new();

    init_persian_hex(&mut hex);

    io::stdout().flush().unwrap();

    io::stdin().read_line(&mut number).unwrap();
    let number: i32 = match number.trim().parse() {
        Ok(n) if n >= 0 => n,
        _ => {
            println!("Error: Please enter a valid integer.");
            return;
        }
    };

    set_mode(&mut hex, &Digits::English);
    // set_mode(&mut hex, &Digits::Persian);

    calculate(&mut hex, number);
}
