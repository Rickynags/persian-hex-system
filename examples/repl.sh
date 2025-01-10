#!/bin/bash

source ../libs/persian_hex.sh

read user_input

if ! [[ "$user_input" =~ ^[0-9]+$ ]] || [ "$user_input" -lt 0 ]; then
    echo "Error: Please enter a valid non-negative integer."
    exit 1
fi

set_mode "ENGLISH"

result=$(calculate "$user_input")
echo "$result"
