const readline = require('readline');
const PersianHex = require('./persian_hex');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (number) => {
  try {
    const hex = PersianHex.toPersianHex(number);
    console.log(`Persian Hex of ${number} is: ${hex}`);
  } catch (error) {
    console.error(error.message);
  } finally {
    rl.close();
  }
});
