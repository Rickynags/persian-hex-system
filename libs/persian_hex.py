from enum import Enum
from typing import Union

class Digits(Enum):
    ENGLISH = 0
    PERSIAN = 1
    ARABIC = 2

class PersianHex:
    def __init__(self):
        """
        Initialize the PersianHex object.
        """
        self.number = None
        self.mode = Digits.ENGLISH
        self.x_equivalent = 'ش'
        self.digits = [str(i) for i in range(10)]
        self.english_digits = self.digits
        self.arabic_digits = {
            0: '٠',
            1: '١',
            2: '٢',
            3: '٣',
            4: '٤',
            5: '٥',
            6: '٦',
            7: '٧',
            8: '٨',
            9: '٩'
        }
        self.persian_digits = {
            0: '۰',
            1: '۱',
            2: '۲',
            3: '۳',
            4: '۴',
            5: '۵',
            6: '۶',
            7: '۷',
            8: '۸',
            9: '۹'
        }
        self.aliases = {
            10: 'پ',
            11: 'چ',
            12: 'ژ',
            13: 'ف',
            14: 'گ',
            15: 'ل'
        }
        
    def calculate(self, number: Union[str, int]):
        """
        Calculate the Persian hexadecimal representation of a number.
        :param number: Integer number to be converted.
        :return: Persian hexadecimal representation as a string.
        """
        if isinstance(number, str) and not number.isdigit():
            # Handle the case where number is not a digit
            for key, value in self.arabic_digits.items():
                number = number.replace(value, str(key))
            for key, value in self.persian_digits.items():
                number = number.replace(value, str(key))

            if not number.isdigit():
                raise ValueError("Invalid number. Please enter a non-negative integer.")

        if isinstance(number, str):  # If it's a string, convert it to int
            number = int(number)

        self.set_value(number)
        return self.show()
    
    def set_mode(self, mode: Digits):
        """
        Set the mode for the PersianHex object.
        :param mode: Digits.ENGLISH for English digits, Digits.PERSIAN for Persian digits, Digits.ARABIC for Arabic digits.
        """
        # check if mode is valid
        if mode in Digits:
            self.mode = mode
            if mode == Digits.ENGLISH:
                self.digits = self.english_digits
            elif mode == Digits.PERSIAN:
                self.digits = self.persian_digits
            elif mode == Digits.ARABIC:
                self.digits = self.arabic_digits
        else:
            raise ValueError("Invalid mode. Use Digits.ENGLISH, Digits.PERSIAN, or Digits.ARABIC.")

    def set_value(self, number: int):
        """
        Set the number to a new value.
        :param number: New integer number to be converted to Persian hexadecimal.
        """
        self.number = number
        self._check()
    
    def _check(self):
        """
        Private method to check the validity of the number.
        """
        if not self._validate():
            raise ValueError("Number must be non-negative.")

    def _validate(self) -> bool:
        """
        Private method to validate the number.
        :return: True if the number is valid, False otherwise.
        """
        return isinstance(self.number, int) and self.number >= 0

    def _convert_to_persian_hex(self, number: int) -> str:
        """
        Recursively convert a number to its Persian hexadecimal representation.
        :param number: Integer number to be converted.
        :return: String representation of the number in Persian hexadecimal.
        """
        if number == 0:
            return ''

        quotient, remainder = divmod(number, 16)
        if remainder > 9:
            result = self.aliases.get(remainder)
        else:
            result = self._digit(remainder)
        return self._convert_to_persian_hex(quotient) + result

    def _digit(self, number: int) -> str:
        """
        Private method to convert a single digit to Persian.
        :param number: Integer digit to be converted.
        :return: Persian representation of the digit.
        """
        if number < 0 or number > 9:
            raise ValueError("Invalid digit. Please enter a number between 0 and 9.")
        return self.digits[number]

    def show(self) -> str:
        """
        Convert the number to Persian hexadecimal and return the formatted result.
        :return: Persian hexadecimal representation as a string.
        """
        persian_hex = f"{self._digit(0)}{self.x_equivalent}" + self._convert_to_persian_hex(self.number)
        return persian_hex
