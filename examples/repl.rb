require_relative 'persian_hex'

puts 'شماره وارد کنید:'
input = gets.chomp

if input =~ /^\d+$/
  number = input.to_i
  PersianHex.new(number).show
else
  puts 'خطا: لطفاً یک عدد صحیح معتبر وارد کنید.'
end
