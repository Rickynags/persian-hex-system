#!/bin/bash

LANGUAGES=("c" "cpp" "php" "python" "ruby" "sh")

LIBS_DIR="libs"
EXAMPLES_DIR="examples"
BUILD_DIR="."

mkdir -p "$BUILD_DIR"

build_c() {
  echo "Building C..."
  gcc "$LIBS_DIR/persian_hex.c" "$EXAMPLES_DIR/repl.c" -o "$BUILD_DIR/persian_hex_c"
  echo "C build completed."
}

build_cpp() {
  echo "Building C++..."
  g++ "$LIBS_DIR/persian_hex.cpp" "$EXAMPLES_DIR/repl.cpp" -o "$BUILD_DIR/persian_hex_cpp"
  echo "C++ build completed."
}

no_build_needed() {
  echo "No build needed for $1."
}

if [[ $# -eq 1 ]]; then
  language=$(echo "$1" | tr '[:upper:]' '[:lower:]')
  if [[ " ${LANGUAGES[*]} " == *" $language "* ]]; then
    case $language in
      "c") build_c
