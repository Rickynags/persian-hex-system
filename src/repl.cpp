#include <iostream>
#include <locale>
#include "persian_hex/persian_hex.hpp"

int main() {
    std::setlocale(LC_ALL, "en_US.UTF-8");

    PersianHex hex;
    hex.init();

    int number;
    if (std::cin >> number && number >= 0) {
        hex.calculate(number);
    } else {
        std::cout << "Error: Please enter a valid integer." << std::endl;
    }

    hex.cleanup();

    return 0;
}
