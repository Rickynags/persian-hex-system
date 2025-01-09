import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
libs_dir = os.path.join(parent_dir, "libs")
sys.path.append(libs_dir)

def main():
    try:
        from persian_hex import PersianHex
        from persian_hex import Digits

        user_input = input("Enter a non-negative integer: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Error: Please enter a non-negative integer.")
                return
        except ValueError:
            print("Error: Please enter a valid integer.")
            return

        persian_hex = PersianHex()
        # persian_hex.set_mode(Digits.ENGLISH)
        persian_hex.set_mode(Digits.PERSIAN)
        # persian_hex.set_mode(Digits.ARABIC)

        result = persian_hex.calculate(number)
        print(f"Persian Hexadecimal: {result}")
    except ImportError as e:
        print(f"Error importing 'PersianHex': {e}")

if __name__ == "__main__":
    main()
