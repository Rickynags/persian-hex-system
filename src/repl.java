import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String userInput = scanner.nextLine();

        try {
            int number = Integer.parseInt(userInput.trim());
            if (number < 0) {
                System.out.println("Error: Please enter a valid non-negative integer.");
                return;
            }

            PersianHex persianHex = new PersianHex();
            persianHex.setMode(Digits.ENGLISH);
            String result = persianHex.calculate(number);
            System.out.println(result);
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format.");
        }
    }
}
