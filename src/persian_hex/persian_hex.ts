export class Digits {
    static ENGLISH = 0;
    static PERSIAN = 1;
    static ARABIC = 2;
}

export class PersianHex {
    private number: number;
    private mode: number;
    private x_equivalent = 'ش';
    private digits: string[] = [];
    private english_digits: string[] = [];
    private arabic_digits: string[] = [];
    private persian_digits: string[] = [];
    private aliases: { [key: number]: string } = {};

    constructor() {
        this.english_digits = Array.from({ length: 10 }, (_, i) => String(i));
        this.arabic_digits = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'];
        this.persian_digits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
        this.aliases = {
            10: 'پ', 11: 'چ', 12: 'ژ', 13: 'ف', 14: 'گ', 15: 'ل'
        };
        this.mode = Digits.ENGLISH;
    }

    calculate(number: string | number): string {
        if (typeof number === 'string' && !/^\d+$/.test(number)) {
            for (let [key, value] of Object.entries(this.arabic_digits)) {
                number = number.replace(new RegExp(value, 'g'), key);
            }
            for (let [key, value] of Object.entries(this.persian_digits)) {
                number = number.replace(new RegExp(value, 'g'), key);
            }

            if (!/^\d+$/.test(number)) {
                throw new Error('Invalid number. Please enter a non-negative integer.');
            }
        }

        number = parseInt(number as string, 10);
        this.setValue(number);
        return this.show();
    }

    setMode(mode: number): void {
        if ([Digits.ENGLISH, Digits.PERSIAN, Digits.ARABIC].includes(mode)) {
            this.mode = mode;
            if (mode === Digits.ENGLISH) {
                this.digits = this.english_digits;
            } else if (mode === Digits.PERSIAN) {
                this.digits = this.persian_digits;
            } else if (mode === Digits.ARABIC) {
                this.digits = this.arabic_digits;
            }
        } else {
            throw new Error('Invalid mode. Use Digits.ENGLISH, Digits.PERSIAN, or Digits.ARABIC.');
        }
    }

    setValue(number: number): void {
        this.number = number;
        this._check();
    }

    private _check(): void {
        if (!this._validate()) {
            throw new Error('Number must be non-negative.');
        }
    }

    private _validate(): boolean {
        return Number.isInteger(this.number) && this.number >= 0;
    }

    private _convertToPersianHex(number: number): string {
        if (number === 0) return '';
        
        const quotient = Math.floor(number / 16);
        const remainder = number % 16;

        let result = remainder > 9 ? this.aliases[remainder] || '' : this._digit(remainder);
        return this._convertToPersianHex(quotient) + result;
    }

    private _digit(number: number): string {
        if (number < 0 || number > 9) {
            throw new Error('Invalid digit. Please enter a number between 0 and 9.');
        }
        return this.digits[number];
    }

    show(): string {
        let persian_hex = this._digit(0) + this.x_equivalent;
        if (this.number === 0) {
            persian_hex += this._digit(0);
        } else {
            persian_hex += this._convertToPersianHex(this.number);
        }
        return persian_hex;
    }
}
