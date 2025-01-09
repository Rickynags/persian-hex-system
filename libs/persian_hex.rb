# persian_hex.rb
class Digits
  ENGLISH = 0
  PERSIAN = 1
  ARABIC = 2
end

class PersianHex
  def initialize
    @number = nil
    @mode = Digits::ENGLISH
    @x_equivalent = 'ش'
    @english_digits = (0..9).to_a.map(&:to_s)
    @persian_digits = {
      0 => '۰', 1 => '۱', 2 => '۲', 3 => '۳', 4 => '۴',
      5 => '۵', 6 => '۶', 7 => '۷', 8 => '۸', 9 => '۹'
    }
    @arabic_digits = {
      0 => '٠', 1 => '١', 2 => '٢', 3 => '٣', 4 => '٤',
      5 => '٥', 6 => '٦', 7 => '٧', 8 => '٨', 9 => '٩'
    }
    @aliases = {
      10 => 'پ', 11 => 'چ', 12 => 'ژ', 13 => 'ف', 14 => 'گ', 15 => 'ل'
    }
    @digits = @english_digits
  end

  def calculate(number)
    if number.is_a?(String) && !number.match?(/\A\d+\z/)
      # Handle the case where number is not a digit
      number = replace_digits(number, @arabic_digits)
      number = replace_digits(number, @persian_digits)

      raise 'Invalid number. Please enter a non-negative integer.' unless number.match?(/\A\d+\z/)
    end

    number = number.to_i if number.is_a?(String)
    set_value(number)
    show
  end

  def set_mode(mode)
    raise 'Invalid mode. Use Digits.ENGLISH, Digits.PERSIAN, or Digits.ARABIC.' unless [Digits::ENGLISH, Digits::PERSIAN, Digits::ARABIC].include?(mode)

    @mode = mode
    case mode
    when Digits::ENGLISH
      @digits = @english_digits
    when Digits::PERSIAN
      @digits = @persian_digits
    when Digits::ARABIC
      @digits = @arabic_digits
    end
  end

  def set_value(number)
    @number = number
    check
  end

  private

  def check
    raise 'Number must be non-negative.' unless valid?
  end

  def valid?
    @number.is_a?(Integer) && @number >= 0
  end

  def convert_to_persian_hex(number)
    return '' if number == 0

    quotient, remainder = number.divmod(16)
    result = remainder > 9 ? @aliases[remainder] : digit(remainder)
    convert_to_persian_hex(quotient) + result
  end

  def digit(number)
    raise 'Invalid digit. Please enter a number between 0 and 9.' unless (0..9).include?(number)
    @digits[number]
  end

  def replace_digits(number, digit_map)
    digit_map.each do |key, value|
      number = number.gsub(value, key.to_s)
    end
    number
  end

  def show
    persian_hex = "#{digit(0)}#{@x_equivalent}#{convert_to_persian_hex(@number)}"
    persian_hex
  end
end
