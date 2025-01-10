#!/bin/bash

LANGUAGES=("c" "cpp" "php" "python" "ruby" "sh")

BUILD_DIR="."
EXAMPLES_DIR="examples"

run_c() {
  echo "Running C..."
  "$BUILD_DIR/persian_hex_c"
}

run_cpp() {
  echo "Running C++..."
  "$BUILD_DIR/persian_hex_cpp"
}

run_php() {
  echo "Running PHP..."
  php "$EXAMPLES_DIR/repl.php"
}

run_python() {
  echo "Running Python..."
  python3 "$EXAMPLES_DIR/repl.py"
}

run_ruby() {
  echo "Running Ruby..."
  ruby "$EXAMPLES_DIR/repl.rb"
}

run_sh() {
  echo "Running Shell..."
  bash "$EXAMPLES_DIR/repl.sh"
}

if [[ $# -eq 1 ]]; then
  language=$(echo "$1" | tr '[:upper:]' '[:lower:]')
  if [[ " ${LANGUAGES[*]} " == *" $language "* ]]; then
    case $language in
      "c") run_c ;;
      "cpp") run_cpp ;;
      "php") run_php ;;
      "python") run_python ;;
      "ruby") run_ruby ;;
      "sh") run_sh ;;
    esac
  else
    echo "Error: Unsupported language '$1'. Supported languages are: ${LANGUAGES[*]}."
    exit 1
  fi
else
  echo "Running all examples..."
  run_c
  run_cpp
  run_php
  run_python
  run_ruby
  run_sh
fi

echo "Execution process completed."
