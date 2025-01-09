require_relative '../libs/persian_hex'

def main
  puts "Enter a non-negative integer:"
  user_input = gets.chomp

  begin
    number = Integer(user_input)
    if number < 0
      puts "Error: Please enter a non-negative integer."
      return
    end
  rescue ArgumentError
    puts "Error: Please enter a valid integer."
    return
  end

  persian_hex = PersianHex.new
  persian_hex.set_mode(Digits::ENGLISH)
  # persian_hex.set_mode(Digits::PERSIAN)
  # persian_hex.set_mode(Digits::ARABIC)

  result = persian_hex.calculate(number)
  puts "Hexadecimal: #{result}"
end

main
