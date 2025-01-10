import * as readline from 'readline';
import { Digits, PersianHex } from './persian_hex/persian_hex';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function main() {
    rl.question('', (user_input: string) => {
        try {
            const number = parseInt(user_input.trim());
            if (isNaN(number) || number < 0) {
                console.log('Error: Please enter a valid non-negative integer.');
                return;
            }

            const persianHex = new PersianHex();
            persianHex.setMode(Digits.ENGLISH);
            const result = persianHex.calculate(number);
            console.log(result);
        } catch (error) {
            console.log(`Error: ${error.message}`);
        } finally {
            rl.close();
        }
    });
}

main();
