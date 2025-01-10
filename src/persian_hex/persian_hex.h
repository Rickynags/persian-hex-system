#ifndef PERSIAN_HEX_H
#define PERSIAN_HEX_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {
    ENGLISH = 0,
    PERSIAN = 1,
    ARABIC = 2
} Digits;

typedef struct {
    int number;                // The number to be converted
    Digits mode;               // Current digit mode (ENGLISH, PERSIAN, ARABIC)
    char *x_equivalent;        // Equivalent of Persian "ش"
    char **digits;             // Array of digits for current mode
    char **aliases;            // Aliases for numbers 10 to 15 (allocated dynamically)
} PersianHex;

void init(PersianHex *hex);
void convert_to_persian_hex(int number, char *result, PersianHex *hex);
void show(PersianHex *hex);
int validate(int number);
void set_mode(PersianHex *hex, Digits mode);
void calculate(PersianHex *hex, int number);
void cleanup(PersianHex *hex);

#endif // PERSIAN_HEX_H
