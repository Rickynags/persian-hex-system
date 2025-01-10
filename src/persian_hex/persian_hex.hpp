#ifndef PERSIAN_HEX_H
#define PERSIAN_HEX_H

#include <iostream>
#include <string>
#include <vector>

enum class Digits {
    ENGLISH = 0,
    PERSIAN = 1,
    ARABIC = 2
};

class PersianHex {
public:
    int number;                    // The number to be converted
    Digits mode;                   // Current digit mode (ENGLISH, PERSIAN, ARABIC)
    std::string x_equivalent;      // Equivalent of Persian "ش"
    std::vector<std::string> digits; // Array of digits for current mode
    std::vector<std::string> aliases; // Aliases for numbers 10 to 15

    PersianHex();
    void init();
    void convert_to_persian_hex(int number, std::string &result);
    void show();
    bool validate(int number);
    void set_mode(Digits mode);
    void calculate(int number);
    void cleanup();
};

#endif // PERSIAN_HEX_H
