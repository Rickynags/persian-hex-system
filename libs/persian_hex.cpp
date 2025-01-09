#include <iostream>
#include "persian_hex.hpp"

std::string aliases[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "پ", "چ", "ژ", "ف", "گ", "ل"};

std::string convert_to_persian_hex_recursive(int number) {
    if (number == 0) return "";
    return convert_to_persian_hex_recursive(number / 16) + aliases[number % 16];
}

std::string convert_to_persian_hex(int number) {
    if (number == 0) {
        return "0";
    } else {
        return convert_to_persian_hex_recursive(number);
    }
}

void show_persian_hex(int number) {
    std::cout << "0ش" << convert_to_persian_hex(number) << std::endl;
}
