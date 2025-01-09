#!/bin/bash

# Supported languages
LANGUAGES=("c" "cpp" "php" "python" "ruby" "sh")

# Paths
LIBS_DIR="libs"
EXAMPLES_DIR="examples"
BUILD_DIR="build"

# Create build directory if not exists
mkdir -p "$BUILD_DIR"

# Function to build C
build_c() {
  echo "Building C..."
  gcc "$LIBS_DIR/persian_hex.c" "$EXAMPLES_DIR/persian_hex.c" -o "$BUILD_DIR/persian_hex_c"
  echo "C build completed."
}

# Function to build C++
build_cpp() {
  echo "Building C++..."
  g++ "$LIBS_DIR/persian_hex.cpp" "$EXAMPLES_DIR/persian_hex.cpp" -o "$BUILD_DIR/persian_hex_cpp"
  echo "C++ build completed."
}

# Function for non-compiled languages (placeholder)
no_build_needed() {
  echo "No build needed for $1."
}

# Check argument or build all
if [[ $# -eq 1 ]]; then
  language=$(echo "$1" | tr '[:upper:]' '[:lower:]')
  if [[ " ${LANGUAGES[*]} " == *" $language "* ]]; then
    case $language in
      "c") build_c
