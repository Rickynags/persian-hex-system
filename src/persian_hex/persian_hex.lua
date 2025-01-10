Digits = {
    ENGLISH = 0,
    PERSIAN = 1,
    ARABIC = 2
}

PersianHex = {}
PersianHex.__index = PersianHex

function PersianHex.new()
    local self = setmetatable({}, PersianHex)
    self.x_equivalent = 'ش'
    self.digits = {}
    self.english_digits = {}
    self.arabic_digits = {}
    self.persian_digits = {}
    self.aliases = {}

    for i = 0, 9 do
        table.insert(self.digits, i)
        table.insert(self.english_digits, i)
    end

    self.arabic_digits = { '٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩' }
    self.persian_digits = { '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹' }
    self.aliases = { 'پ', 'چ', 'ژ', 'ف', 'گ', 'ل' }

    self.mode = Digits.ENGLISH
    return self
end

function PersianHex:set_mode(mode)
    if mode == Digits.ENGLISH or mode == Digits.PERSIAN or mode == Digits.ARABIC then
        self.mode = mode
        if mode == Digits.ENGLISH then
            self.digits = self.english_digits
        elseif mode == Digits.PERSIAN then
            self.digits = self.persian_digits
        elseif mode == Digits.ARABIC then
            self.digits = self.arabic_digits
        end
    else
        error("Invalid mode. Use Digits.ENGLISH, Digits.PERSIAN, or Digits.ARABIC.")
    end
end

function PersianHex:calculate(number)
    if type(number) == "string" then
        if not number:match("^%d+$") then
            for k, v in pairs(self.arabic_digits) do
                number = number:gsub(v, tostring(k-1))
            end
            for k, v in pairs(self.persian_digits) do
                number = number:gsub(v, tostring(k-1))
            end
        end
        if not number:match("^%d+$") then
            error("Invalid number. Please enter a non-negative integer.")
        end
    end

    if type(number) == "string" then
        number = tonumber(number)
    end

    self:set_value(number)
    return self:show()
end

function PersianHex:set_value(number)
    self.number = number
    self:_check()
end

function PersianHex:_check()
    if not self:_validate() then
        error("Number must be non-negative.")
    end
end

function PersianHex:_validate()
    return type(self.number) == "number" and self.number >= 0
end

function PersianHex:_convert_to_persian_hex(number)
    if number == 0 then
        return ''
    end

    local quotient = math.floor(number / 16)
    local remainder = number % 16

    local result
    if remainder > 9 then
        result = self.aliases[remainder - 9] or ''
    else
        result = self:_digit(remainder)
    end

    return self:_convert_to_persian_hex(quotient) .. result
end

function PersianHex:_digit(number)
    if number < 0 or number > 9 then
        error("Invalid digit. Please enter a number between 0 and 9.")
    end
    return self.digits[number + 1]
end

function PersianHex:show()
    local persian_hex = self:_digit(0) .. self.x_equivalent
    if self.number == 0 then
        persian_hex = persian_hex .. self:_digit(0)
    else
        persian_hex = persian_hex .. self:_convert_to_persian_hex(self.number)
    end
    return persian_hex
end
