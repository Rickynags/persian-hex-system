class PersianHex {
    static toPersianHex(number) {
      const hexDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
      let num = parseInt(number, 10);
      let result = '';
  
      if (isNaN(num)) {
        throw new Error('Input is not a valid number');
      }
  
      while (num > 0) {
        result = hexDigits[num % 16] + result;
        num = Math.floor(num / 16);
      }
  
      return result || hexDigits[0];
    }
  
    static validateInput(number) {
      if (isNaN(number)) {
        throw new Error('Input is not a valid number');
      }
    }
  
    static testCases() {
      const testCases = ['10', '255', '4095', '16'];
      testCases.forEach((test) => {
        const hex = PersianHex.toPersianHex(test);
        console.log(`Persian Hex of ${test} is: ${hex}`);
      });
    }
  }
  
  module.exports = PersianHex;
  