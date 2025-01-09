<?php
require_once __DIR__ . "/../libs/persian_hex.php";

function main() {
    try {
        echo "Enter a non-negative integer: ";
        $user_input = trim(fgets(STDIN));

        if (!is_numeric($user_input)) {
            echo "Error: Please enter a valid integer.\n";
            return;
        }

        $number = (int)$user_input;
        if ($number < 0) {
            echo "Error: Please enter a non-negative integer.\n";
            return;
        }

        $persianHex = new PersianHex();
        $persianHex->set_mode(Digits::ENGLISH);

        $result = $persianHex->calculate($number);
        echo "Hexadecimal: $result\n";

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

main();
