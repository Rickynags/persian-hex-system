#include <locale.h>
#include <stdio.h>
#include "../libs/persian_hex.h"

int main() {
    setlocale(LC_ALL, "en_US.UTF-8");

    PersianHex hex;

    int number;
    printf("Enter a non-negative integer: ");
    if (scanf("%d", &number) != 1 || number < 0) {
        printf("Error: Please enter a valid integer.\n");
        return 1;
    }

    init(&hex);

    set_mode(&hex, ENGLISH);
    // set_mode(&hex, PERSIAN);
    printf("Hexadecimal: ");
    calculate(&hex, number);

    return 0;
}
