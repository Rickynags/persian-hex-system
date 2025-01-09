class PersianHex
    def initialize(number)
      raise ArgumentError, "Number must be non-negative." if number < 0
  
      @number = number
      @x_equivalent = 'ش'
      @aliases = {
        10 => 'پ',
        11 => 'چ',
        12 => 'ژ',
        13 => 'ف',
        14 => 'گ',
        15 => 'ل'
      }
    end
  
    def convert_to_persian_hex(number)
      return '' if number == 0
  
      quotient, remainder = number.divmod(16)
      digit = @aliases[remainder] || remainder.to_s
      convert_to_persian_hex(quotient) + digit
    end
  
    def show
      if @number == 0
        "0#{@x_equivalent}0"
      else
        "0#{@x_equivalent}" + convert_to_persian_hex(@number)
      end
    end
  end
  
  begin
    print "شماره وارد کنید: "
    input = gets.chomp.to_i
    persian_hex = PersianHex.new(input)
    puts persian_hex.show
  rescue ArgumentError => e
    puts "خطا: #{e.message}"
  end
  