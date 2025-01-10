#include <locale.h>
#include <stdio.h>
#include "persian_hex/persian_hex.h"

int main() {
    setlocale(LC_ALL, "en_US.UTF-8");

    PersianHex hex;

    int number;
    if (scanf("%d", &number) != 1 || number < 0) {
        printf("Error: Please enter a valid integer.\n");
        return 1;
    }

    init(&hex);

    set_mode(&hex, ENGLISH);
    // set_mode(&hex, PERSIAN);
    calculate(&hex, number);

    cleanup(&hex);

    return 0;
}
