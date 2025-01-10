pub enum Digits {
    English,
    Persian,
    Arabic,
}

pub struct PersianHex {
    x_equivalent: String,
    digits: Vec<String>,
    aliases: Vec<String>,
    number: i32,
    mode: Digits,
}

impl PersianHex {
    pub fn new() -> Self {
        PersianHex {
            x_equivalent: String::from("ش"),
            digits: vec![String::new(); 10],
            aliases: vec![String::from("پ"), String::from("چ"), String::from("ژ"), 
                          String::from("ف"), String::from("گ"), String::from("ل")],
            number: 0,
            mode: Digits::English,
        }
    }
}

pub fn init_persian_hex(hex: &mut PersianHex) {
    set_mode(hex, Digits::English);
}

pub fn set_mode(hex: &mut PersianHex, mode: Digits) {
    hex.mode = mode;
    hex.digits.iter_mut().for_each(|digit| *digit = String::new());

    match mode {
        Digits::English => {
            for i in 0..10 {
                hex.digits[i] = i.to_string();
            }
        }
        Digits::Persian => {
            hex.digits = vec![String::from("۰"), String::from("۱"), String::from("۲"),
                              String::from("۳"), String::from("۴"), String::from("۵"),
                              String::from("۶"), String::from("۷"), String::from("۸"),
                              String::from("۹")];
        }
        Digits::Arabic => {
            hex.digits = vec![String::from("٠"), String::from("١"), String::from("٢"),
                              String::from("٣"), String::from("٤"), String::from("٥"),
                              String::from("٦"), String::from("٧"), String::from("٨"),
                              String::from("٩")];
        }
    }
}

pub fn convert_to_persian_hex(number: i32, result: &mut String, hex: &PersianHex) {
    if number == 0 {
        return;
    }

    let quotient = number / 16;
    let remainder = number % 16;

    convert_to_persian_hex(quotient, result, hex);

    if remainder > 9 {
        result.push_str(&hex.aliases[(remainder - 10) as usize]);
    } else {
        result.push_str(&hex.digits[remainder as usize]);
    }
}

pub fn show(hex: &PersianHex) {
    let mut result = String::new();

    if hex.number == 0 {
        println!("{}{}", hex.digits[0], hex.x_equivalent);
        return;
    }

    convert_to_persian_hex(hex.number, &mut result, hex);
    println!("{}{}{}", hex.digits[0], hex.x_equivalent, result);
}

pub fn validate(number: i32) -> bool {
    number >= 0
}

pub fn calculate(hex: &mut PersianHex, number: i32) {
    if !validate(number) {
        println!("Error: Please enter a valid non-negative integer.");
        return;
    }

    hex.number = number;
    show(hex);
}
