#include <iostream>
#include "persian_hex.hpp"

int main() {
    int number;
    std::cout << "شماره وارد کنید: ";
    std::cin >> number;
    if (number < 0) {
        std::cerr << "خطا: عدد باید غیر منفی باشد." << std::endl;
    } else {
        show_persian_hex(number);
    }
    return 0;
}
