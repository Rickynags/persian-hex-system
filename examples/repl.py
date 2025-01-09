import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
libs_dir = os.path.join(parent_dir, "libs")
sys.path.append(libs_dir)

from persian_hex import PersianHex

def main():
    try:
        number = int(input("شماره وارد کنید: "))
        if number < 0:
            print("خطا: عدد باید غیر منفی باشد.")
        else:
            PersianHex(number).show()
    except ValueError:
        print("خطا: لطفاً یک عدد صحیح معتبر وارد کنید.")
    except ImportError as e:
        print(f"Error importing 'PersianHex': {e}")

if __name__ == "__main__":
    main()
