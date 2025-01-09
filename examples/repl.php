<?php
require_once __DIR__ . "/../libs/persian_hex.php";

// try {
//     echo "شماره وارد کنید: ";
//     $input = trim(fgets(STDIN));
//     $number = (int)$input;

//     $persianHex = new PersianHex($number);
//     echo $persianHex->show() . PHP_EOL;
// } catch (Exception $e) {
//     echo "خطا: لطفاً یک عدد صحیح معتبر وارد کنید. " . $e->getMessage() . PHP_EOL;
// }

$res = [];
for ($i = 0; $i <= 10000; $i++) {
    $persianHex = new PersianHex($i);
    // echo $persianHex->show() . PHP_EOL;
    $res[$i] = $persianHex->show();
}
file_put_contents('../persian_hex.txt', json_encode($res));
