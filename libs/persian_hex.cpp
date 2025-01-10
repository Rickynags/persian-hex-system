// g++ repl.cpp ../libs/persian_hex.cpp -o ./../persian_hex_cpp && ./../persian_hex_cpp
#include "persian_hex.hpp"

PersianHex::PersianHex() {
    number = 0;
    mode = Digits::ENGLISH;
    x_equivalent = "ش";
    digits.resize(10);
    aliases.resize(6);
}

void PersianHex::init() {
    aliases[0] = "پ";
    aliases[1] = "چ";
    aliases[2] = "ژ";
    aliases[3] = "ف";
    aliases[4] = "گ";
    aliases[5] = "ل";

    set_mode(Digits::ENGLISH);
}

void PersianHex::convert_to_persian_hex(int number, std::string &result) {
    if (number == 0) {
        return;
    }

    int quotient = number / 16;
    int remainder = number % 16;

    convert_to_persian_hex(quotient, result);

    if (remainder > 9) {
        result += aliases[remainder - 10];
    } else {
        result += digits[remainder];
    }
}

void PersianHex::reverse_string_utf8(std::string &str) {
    int i = 0, j = str.length() - 1;

    while (i < j) {
        while ((str[i] & 0xC0) == 0x80) {
            i++;
        }
        while ((str[j] & 0xC0) == 0x80) {
            j--;
        }

        std::swap(str[i], str[j]);

        i++;
        j--;
    }
}

void PersianHex::show() {
    std::string result = "";
    std::cout << digits[0] + x_equivalent;

    if (number == 0) {
        std::cout << digits[0] << std::endl;
    } else {
        convert_to_persian_hex(number, result);
        std::cout << result << std::endl;
    }
}

bool PersianHex::validate(int number) {
    return number >= 0;
}

void PersianHex::set_mode(Digits mode) {
    this->mode = mode;
    for (int i = 0; i < 10; i++) {
        digits[i].clear();
    }

    if (mode == Digits::ENGLISH) {
        for (int i = 0; i < 10; i++) {
            digits[i] = std::to_string(i);
        }
    } else if (mode == Digits::PERSIAN) {
        digits[0] = "۰";
        digits[1] = "۱";
        digits[2] = "۲";
        digits[3] = "۳";
        digits[4] = "۴";
        digits[5] = "۵";
        digits[6] = "۶";
        digits[7] = "۷";
        digits[8] = "۸";
        digits[9] = "۹";
    } else if (mode == Digits::ARABIC) {
        digits[0] = "٠";
        digits[1] = "١";
        digits[2] = "٢";
        digits[3] = "٣";
        digits[4] = "٤";
        digits[5] = "٥";
        digits[6] = "٦";
        digits[7] = "٧";
        digits[8] = "٨";
        digits[9] = "٩";
    }
}

void PersianHex::calculate(int number) {
    if (!validate(number)) {
        std::cout << "Error: Please enter a valid non-negative integer." << std::endl;
        return;
    }

    this->number = number;
    show();
}

void PersianHex::cleanup() {
    digits.clear();
    aliases.clear();
}
