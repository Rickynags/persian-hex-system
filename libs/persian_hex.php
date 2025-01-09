<?php
class PersianHex {
    private int $number;
    private string $x_equivalent = 'ش';
    private array $aliases = [
        10 => 'پ',
        11 => 'چ',
        12 => 'ژ',
        13 => 'ف',
        14 => 'گ',
        15 => 'ل'
    ];

    public function __construct(int $number) {
        if ($number < 0) {
            throw new InvalidArgumentException("Number must be non-negative.");
        }
        $this->number = $number;
    }

    private function convertToPersianHex(int $number): string {
        if ($number === 0) {
            return '';
        }

        $quotient = intdiv($number, 16);
        $remainder = $number % 16;
        $digit = $this->aliases[$remainder] ?? (string)$remainder;

        return $this->convertToPersianHex($quotient) . $digit;
    }

    public function show(): string {
        if ($this->number === 0) {
            return "0{$this->x_equivalent}0";
        }

        return "0{$this->x_equivalent}" . $this->convertToPersianHex($this->number);
    }
}

try {
    echo "شماره وارد کنید: ";
    $input = trim(fgets(STDIN));
    $number = (int)$input;

    $persianHex = new PersianHex($number);
    echo $persianHex->show() . PHP_EOL;
} catch (Exception $e) {
    echo "خطا: لطفاً یک عدد صحیح معتبر وارد کنید. " . $e->getMessage() . PHP_EOL;
}
