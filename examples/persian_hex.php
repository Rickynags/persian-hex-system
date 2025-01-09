<?php
require_once "../libs/persian_hex.php";

try {
    echo "شماره وارد کنید: ";
    $input = trim(fgets(STDIN));
    $number = (int)$input;

    $persianHex = new PersianHex($number);
    echo $persianHex->show() . PHP_EOL;
} catch (Exception $e) {
    echo "خطا: لطفاً یک عدد صحیح معتبر وارد کنید. " . $e->getMessage() . PHP_EOL;
}
