import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
libs_dir = os.path.join(parent_dir, "libs")
sys.path.append(libs_dir)

def main():
    try:
        from persian_hex import PersianHex

        number = int(input())
        if number < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            result = PersianHex().set_mode().calculate(number)
            print(result)
    except ValueError:
        print("Error: Please enter a valid integer.", number)
    except ImportError as e:
        print(f"Error importing 'PersianHex'")

if __name__ == "__main__":
    main()
