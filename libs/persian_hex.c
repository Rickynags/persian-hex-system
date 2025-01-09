#include <stdio.h>
#include "persian_hex.h"

char *aliases[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "پ", "چ", "ژ", "ف", "گ", "ل"};

void convert_to_persian_hex_recursive(int number) {
    if (number == 0) return;
    convert_to_persian_hex_recursive(number / 16);
    int remainder = number % 16;
    printf("%s", aliases[remainder]);
}

void convert_to_persian_hex(int number) {
    if (number == 0) {
        printf("0");
    } else {
        convert_to_persian_hex_recursive(number);
    }
}

void show_persian_hex(int number) {
    printf("0ش");
    convert_to_persian_hex(number);
    printf("\n");
}
