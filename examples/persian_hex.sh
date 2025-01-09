#!/bin/bash

source ../libs/persian_hex.sh

read -p "شماره وارد کنید: " input

if [[ "$input" =~ ^[0-9]+$ ]]; then
  show_persian_hex "$input"
else
  echo "خطا: لطفاً یک عدد صحیح معتبر وارد کنید."
fi
