#!/bin/bash

convert_to_persian_hex() {
  local number=$1
  local x_equivalent="ش"
  local aliases=("0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "پ" "چ" "ژ" "ف" "گ" "ل")
  local result=""

  while [ "$number" -gt 0 ]; do
    remainder=$((number % 16))
    result="${aliases[remainder]}$result"
    number=$((number / 16))
  done

  echo "$result"
}

show_persian_hex() {
  local number=$1

  if [ "$number" -lt 0 ]; then
    echo "خطا: عدد باید غیر منفی باشد."
    return
  fi

  local x_equivalent="ش"
  if [ "$number" -eq 0 ]; then
    echo "0${x_equivalent}0"
  else
    echo "0${x_equivalent}$(convert_to_persian_hex "$number")"
  fi
}

read -p "شماره وارد کنید: " input
if [[ "$input" =~ ^[0-9]+$ ]]; then
  show_persian_hex "$input"
else
  echo "خطا: لطفاً یک عدد صحیح معتبر وارد کنید."
fi
