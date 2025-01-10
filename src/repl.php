<?php
require_once __DIR__ . "/persian_hex/persian_hex.php";

function main() {
    try {
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
        echo "$result\n";

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

main();
