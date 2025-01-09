import json

class persian_hex:
    def __init__(self, number: int):
        self.number = number
        self.x_equivalent = 'ش'

        self.aliases = {10: 'پ',
11: 'چ',
12: 'ژ',
13: 'ف',
14: 'گ',
15: 'ل'}


    def show(self, number = None, is_first = True):
        '''شماره دریافتی را به پایه شانزده نشان بده'''
        if not number:
            number = self.number
        if is_first:
            print(0)
            print(self.x_equivalent)
        for i in divmod(number, 16):
            if i > 15:
                return self.show(i, False)
            elif i in self.aliases:
                print(self.aliases[i])
            else:
                print(i)

    def result(self, number = None, is_first = True):
        '''شماره دریافتی را به پایه شانزده نشان بده'''
        if not number:
            number = self.number
        buffer = ""
        if is_first:
            buffer += "0"
            buffer += self.x_equivalent
        for i in divmod(number, 16):
            if i > 15:
                buffer += self.result(i, False)
            elif i in self.aliases:
                buffer += self.aliases[i]
            else:
                buffer += str(i)
        return buffer

def convert_range_to_persian_hex(start, end):
    """Convert a range of numbers to Persian hexadecimal."""
    results = {}
    for num in range(start, end + 1):
        persian_hex_instance = persian_hex(num)
        output = persian_hex_instance.result()
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
    end = 999999
    output_file = "persian_hex_output.json"

    persian_hex_data = convert_range_to_persian_hex(start, end)

    save_to_json(persian_hex_data, output_file)


if __name__ == "__main__":
    main()
