// gcc repl.c ../libs/persian_hex.c -o repl_c && ./repl_c
#include "persian_hex.h"

void init(PersianHex *hex) {
    hex->x_equivalent = malloc(5 * sizeof(char) + 1);
    strcpy(hex->x_equivalent, "ش");
    
    hex->digits = malloc(10 * sizeof(char *));
    hex->aliases = malloc(6 * sizeof(char *));
    
    for (int i = 0; i < 10; i++) {
        hex->digits[i] = NULL;
    }

    for (int i = 0; i < 6; i++) {
        hex->aliases[i] = (char *)malloc(5 * sizeof(char) + 1);
    }
    strcpy(hex->aliases[0], "پ");
    strcpy(hex->aliases[1], "چ");
    strcpy(hex->aliases[2], "ژ");
    strcpy(hex->aliases[3], "ف");
    strcpy(hex->aliases[4], "گ");
    strcpy(hex->aliases[5], "ل");

    set_mode(hex, ENGLISH);
}

void convert_to_persian_hex(int number, char *result, PersianHex *hex) {
    if (number == 0) {
        return;
    }

    int quotient = number / 16;
    int remainder = number % 16;

    convert_to_persian_hex(quotient, result, hex);

    if (remainder > 9) {
        strcat(result, hex->aliases[remainder - 10]);
    } else {
        strcat(result, hex->digits[remainder]);
    }
}

void reverse_string_utf8(char *str) {
    int length = strlen(str);
    int i = 0, j = length - 1;
    
    while (i < j) {
        while ((str[i] & 0xC0) == 0x80) {
            i++;
        }
        while ((str[j] & 0xC0) == 0x80) {
            j--;
        }

        char temp = str[i];
        str[i] = str[j];
        str[j] = temp;

        i++;
        j--;
    }
}

void show(PersianHex *hex) {
    char result[1000] = "";

    convert_to_persian_hex(hex->number, result, hex);

    printf("Hexadecimal: %s%s%s\n", hex->digits[0], hex->x_equivalent, result);
}

int validate(int number) {
    return number >= 0;
}

void set_mode(PersianHex *hex, Digits mode) {
    hex->mode = mode;

    for (int i = 0; i < 10; i++) {
        if (hex->digits[i] != NULL) {
            free(hex->digits[i]);
        }
        hex->digits[i] = (char *)malloc(5 * sizeof(char) + 1);
    }

    if (mode == ENGLISH) {
        for (int i = 0; i < 10; i++) {
            sprintf(hex->digits[i], "%d", i);
        }
    } else if (mode == PERSIAN) {
        strcpy(hex->digits[0], "۰");
        strcpy(hex->digits[1], "۱");
        strcpy(hex->digits[2], "۲");
        strcpy(hex->digits[3], "۳");
        strcpy(hex->digits[4], "۴");
        strcpy(hex->digits[5], "۵");
        strcpy(hex->digits[6], "۶");
        strcpy(hex->digits[7], "۷");
        strcpy(hex->digits[8], "۸");
        strcpy(hex->digits[9], "۹");
    } else if (mode == ARABIC) {
        strcpy(hex->digits[0], "٠");
        strcpy(hex->digits[1], "١");
        strcpy(hex->digits[2], "٢");
        strcpy(hex->digits[3], "٣");
        strcpy(hex->digits[4], "٤");
        strcpy(hex->digits[5], "٥");
        strcpy(hex->digits[6], "٦");
        strcpy(hex->digits[7], "٧");
        strcpy(hex->digits[8], "٨");
        strcpy(hex->digits[9], "٩");
    }

    for (int i = 0; i < 10; i++) {
        printf("1-[%d] => %s\n", i, hex->digits[i]);
    }

    for (int i = 0; i < 6; i++) {
        printf("2-[%d] => %s\n", i, hex->aliases[i]);
    }
}

void calculate(PersianHex *hex, int number) {
    if (!validate(number)) {
        printf("Error: Please enter a valid non-negative integer.\n");
        return;
    }

    hex->number = number;
    show(hex);
}

void cleanup(PersianHex *hex) {
    for (int i = 0; i < 10; i++) {
        if (hex->digits[i] != NULL) {
            free(hex->digits[i]);
        }
    }
    for (int i = 0; i < 6; i++) {
        if (hex->aliases[i] != NULL) {
            free(hex->aliases[i]);
        }
    }
}
