#!/bin/bash

declare -A persian_digits=( [0]="۰" [1]="۱" [2]="۲" [3]="۳" [4]="۴" [5]="۵" [6]="۶" [7]="۷" [8]="۸" [9]="۹" )
declare -A arabic_digits=( [0]="٠" [1]="١" [2]="٢" [3]="٣" [4]="٤" [5]="٥" [6]="٦" [7]="٧" [8]="٨" [9]="٩" )
declare -A aliases=( [10]="پ" [11]="چ" [12]="ژ" [13]="ف" [14]="گ" [15]="ل" )

mode="ENGLISH"

convert_digit() {
    local digit=$1
    case "$mode" in
        "ENGLISH") echo -n "$digit" ;;
        "PERSIAN") echo -n "${persian_digits[$digit]}" ;;
        "ARABIC") echo -n "${arabic_digits[$digit]}" ;;
        *) echo "Invalid mode"; exit 1 ;;
    esac
}

convert_to_persian_hex() {
    local number=$1
    local quotient remainder result
    if [ "$number" -eq 0 ]; then
        echo -n ""
        return
    fi

    quotient=$((number / 16))
    remainder=$((number % 16))

    if [ "$remainder" -gt 9 ]; then
        result="${aliases[$remainder]}"
    else
        result=$(convert_digit "$remainder")
    fi

    convert_to_persian_hex "$quotient"
    echo -n "$result"
}

set_mode() {
    mode=$1
}

calculate() {
    local number=$1
    if ! [[ "$number" =~ ^[0-9]+$ ]]; then
        echo "Error: Please enter a valid non-negative integer."
        exit 1
    fi

    local persian_hex
    persian_hex=$(convert_to_persian_hex "$number")

    echo -n "$(convert_digit 0)ش$persian_hex"
}
