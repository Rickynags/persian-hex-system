#include <stdio.h>
#include "persian_hex.h"

int main() {
    int number;
    printf("شماره وارد کنید: ");
    scanf("%d", &number);
    if (number < 0) {
        printf("خطا: عدد باید غیر منفی باشد.\n");
    } else {
        show_persian_hex(number);
    }
    return 0;
}
