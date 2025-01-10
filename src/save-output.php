<?php
require_once __DIR__ . "/persian_hex/persian_hex.php";

$res = [];
for ($i = 10000; $i >= 0; $i--) {
    $persianHex = new PersianHex($i);
    $res[$i . ""] = $persianHex->show();
}
file_put_contents('../data.txt', json_encode($res, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
