<?php
require_once __DIR__ . "/../libs/persian_hex.php";

$res = [];
for ($i = 10000; $i >= 0; $i--) {
    $persianHex = new PersianHex($i);
    $res[$i . ""] = $persianHex->show();
}
file_put_contents('../persian_hex.txt', json_encode($res, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
