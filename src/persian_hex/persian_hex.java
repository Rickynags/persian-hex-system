public class Digits {
    public static final int ENGLISH = 0;
    public static final int PERSIAN = 1;
    public static final int ARABIC = 2;
}

public class PersianHex {
    private int number;
    private int mode;
    private final String xEquivalent = "ش";
    private String[] digits;
    private final String[] englishDigits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
    private final String[] arabicDigits = {"٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"};
    private final String[] persianDigits = {"۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"};
    private final java.util.Map<Integer, String> aliases;

    public PersianHex() {
        aliases = new java.util.HashMap<>();
        aliases.put(10, "پ");
        aliases.put(11, "چ");
        aliases.put(12, "ژ");
        aliases.put(13, "ف");
        aliases.put(14, "گ");
        aliases.put(15, "ل");
        this.mode = Digits.ENGLISH;
    }

    public String calculate(Object number) {
        if (number instanceof String) {
            String strNumber = (String) number;
            if (!strNumber.matches("\\d+")) {
                for (int i = 0; i < arabicDigits.length; i++) {
                    strNumber = strNumber.replace(arabicDigits[i], String.valueOf(i));
                }
                for (int i = 0; i < persianDigits.length; i++) {
                    strNumber = strNumber.replace(persianDigits[i], String.valueOf(i));
                }
                if (!strNumber.matches("\\d+")) {
                    throw new IllegalArgumentException("Invalid number format.");
                }
            }
            number = Integer.parseInt(strNumber);
        }

        setValue((int) number);
        return show();
    }

    public void setMode(int mode) {
        if (mode == Digits.ENGLISH) {
            digits = englishDigits;
        } else if (mode == Digits.PERSIAN) {
            digits = persianDigits;
        } else if (mode == Digits.ARABIC) {
            digits = arabicDigits;
        } else {
            throw new IllegalArgumentException("Invalid mode.");
        }
        this.mode = mode;
    }

    private void setValue(int number) {
        this.number = number;
        check();
    }

    private void check() {
        if (!validate()) {
            throw new IllegalArgumentException("Number must be non-negative.");
        }
    }

    private boolean validate() {
        return number >= 0;
    }

    private String convertToPersianHex(int number) {
        if (number == 0) return "";

        int quotient = number / 16;
        int remainder = number % 16;

        String result = remainder > 9 ? aliases.getOrDefault(remainder, "") : digit(remainder);
        return convertToPersianHex(quotient) + result;
    }

    private String digit(int number) {
        if (number < 0 || number > 9) {
            throw new IllegalArgumentException("Invalid digit.");
        }
        return digits[number];
    }

    public String show() {
        String persianHex = digit(0) + xEquivalent;
        if (number == 0) {
            persianHex += digit(0);
        } else {
            persianHex += convertToPersianHex(number);
        }
        return persianHex;
    }
}
