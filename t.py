import json

class PersianHex:
    def __init__(self, number: int):
        """Initialize the PersianHex object."""
        self.number = number
        self.x_equivalent = 'ش'
        self.aliases = {10: 'پ', 11: 'چ', 12: 'ژ', 13: 'ف', 14: 'گ', 15: 'ل'}

    def convert_to_persian_hex(self, number=None, is_first=True):
        """Convert the number to Persian hexadecimal."""
        if number is None:
            number = self.number

        result = []
        if is_first:
            result.append('0')
            result.append(self.x_equivalent)

        for i in divmod(number, 16):
            if i > 15:
                result.extend(self.convert_to_persian_hex(i, False))
            elif i in self.aliases:
                result.append(self.aliases[i])
            else:
                result.append(str(i))

        return result


def convert_range_to_persian_hex(start, end):
    """Convert a range of numbers to Persian hexadecimal."""
    results = {}
    for num in range(start, end + 1):
        persian_hex_instance = PersianHex(num)
        output = persian_hex_instance.convert_to_persian_hex()
        results[num] = ''.join(output)
    return results


def save_to_json(data, file_path):
    """Save the dictionary to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    print(f"Data successfully saved to {file_path}")


def main():
    """Main function to convert numbers and save to JSON."""
    start = 0
    end = 99999
    output_file = "persian_hex_output.json"

    persian_hex_data = convert_range_to_persian_hex(start, end)

    save_to_json(persian_hex_data, output_file)


if __name__ == "__main__":
    main()
