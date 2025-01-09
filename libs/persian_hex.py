class PersianHex:
    def __init__(self, number: int):
        """
        Initialize the PersianHex object with a number.
        :param number: Integer number to be converted to Persian hexadecimal.
        """
        self.number = number
        self.x_equivalent = 'ش'
        self.aliases = {
            10: 'پ',
            11: 'چ',
            12: 'ژ',
            13: 'ف',
            14: 'گ',
            15: 'ل'
        }

    def _convert_to_persian_hex(self, number: int) -> str:
        """
        Recursively convert a number to its Persian hexadecimal representation.
        :param number: Integer number to be converted.
        :return: String representation of the number in Persian hexadecimal.
        """
        if number == 0:
            return ''

        quotient, remainder = divmod(number, 16)
        digit = self.aliases.get(remainder, str(remainder))
        return self._convert_to_persian_hex(quotient) + digit

    def show(self) -> str:
        """
        Convert the number to Persian hexadecimal and return the formatted result.
        :return: Persian hexadecimal representation as a string.
        """
        if self.number < 0:
            raise ValueError("Number must be non-negative.")

        persian_hex = f"0{self.x_equivalent}" + self._convert_to_persian_hex(self.number)
        return persian_hex


if __name__ == "__main__":
    try:
        prompt = 'شماره وارد کنید: '
        user_input = int(input(prompt))

        persian_hex_converter = PersianHex(user_input)
        print(persian_hex_converter.show())
    except ValueError as e:
        print(f"خطا: لطفاً یک عدد صحیح معتبر وارد کنید. {e}")
