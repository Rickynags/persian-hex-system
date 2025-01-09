import os
import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
sys.path.append(os.path.join(parent_dir, "libs"))

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

if __name__ == "__main__":
    main()
