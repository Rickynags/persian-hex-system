<?php
class Digits {
    const ENGLISH = 0;
    const PERSIAN = 1;
    const ARABIC = 2;
}

class PersianHex {
    private $number;
    private $mode;
    private $x_equivalent = 'ش';
    private $digits = [];
    private $english_digits = [];
    private $arabic_digits = [];
    private $persian_digits = [];
    private $aliases = [];

    public function __construct() {
        $this->digits = range(0, 9);
        $this->english_digits = $this->digits;
        $this->arabic_digits = [
            0 => '٠', 1 => '١', 2 => '٢', 3 => '٣', 4 => '٤',
            5 => '٥', 6 => '٦', 7 => '٧', 8 => '٨', 9 => '٩'
        ];
        $this->persian_digits = [
            0 => '۰', 1 => '۱', 2 => '۲', 3 => '۳', 4 => '۴',
            5 => '۵', 6 => '۶', 7 => '۷', 8 => '۸', 9 => '۹'
        ];
        $this->aliases = [
            10 => 'پ', 11 => 'چ', 12 => 'ژ', 13 => 'ف', 14 => 'گ', 15 => 'ل'
        ];

        $this->mode = Digits::ENGLISH;
    }

    public function calculate($number) {
        if (is_string($number) && !ctype_digit($number)) {
            foreach ($this->arabic_digits as $key => $value) {
                $number = str_replace($value, (string)$key, $number);
            }
            foreach ($this->persian_digits as $key => $value) {
                $number = str_replace($value, (string)$key, $number);
            }

            if (!ctype_digit($number)) {
                throw new Exception("Invalid number. Please enter a non-negative integer.");
            }
        }

        if (is_string($number)) {
            $number = (int)$number;
        }

        $this->set_value($number);
        return $this->show();
    }

    public function set_mode($mode) {
        if (in_array($mode, [Digits::ENGLISH, Digits::PERSIAN, Digits::ARABIC])) {
            $this->mode = $mode;
            if ($mode === Digits::ENGLISH) {
                $this->digits = $this->english_digits;
            } elseif ($mode === Digits::PERSIAN) {
                $this->digits = $this->persian_digits;
            } elseif ($mode === Digits::ARABIC) {
                $this->digits = $this->arabic_digits;
            }
        } else {
            throw new Exception("Invalid mode. Use Digits::ENGLISH, Digits::PERSIAN, or Digits::ARABIC.");
        }
    }

    public function set_value($number) {
        $this->number = $number;
        $this->_check();
    }

    private function _check() {
        if (!$this->_validate()) {
            throw new Exception("Number must be non-negative.");
        }
    }

    private function _validate() {
        return is_int($this->number) && $this->number >= 0;
    }

    private function _convert_to_persian_hex($number) {
        if ($number == 0) {
            return '';
        }

        $quotient = intdiv($number, 16);
        $remainder = $number % 16;

        if ($remainder > 9) {
            $result = $this->aliases[$remainder] ?? '';
        } else {
            $result = $this->_digit($remainder);
        }

        return $this->_convert_to_persian_hex($quotient) . $result;
    }

    private function _digit($number) {
        if ($number < 0 || $number > 9) {
            throw new Exception("Invalid digit. Please enter a number between 0 and 9.");
        }
        return $this->digits[$number];
    }

    public function show() {
        $persian_hex = $this->_digit(0) . $this->x_equivalent . $this->_convert_to_persian_hex($this->number);
        return $persian_hex;
    }
}
