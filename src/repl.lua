local current_dir = "src/persian_hex"
-- local current_dir = "C:\\Files\\Projects\\persian-hex-system\\src\\persian_hex"
package.path = package.path .. ";" .. current_dir .. "\\?.lua"

require("persian_hex")

function main()
    local user_input = io.read("*line"):gsub("^%s*(.-)%s*$", "%1")

    if not user_input:match("^%d+$") then
        print("Error: Please enter a valid integer.")
        return
    end

    local number = tonumber(user_input)
    if number < 0 then
        print("Error: Please enter a non-negative integer.")
        return
    end

    local persianHex = PersianHex.new()
    persianHex:set_mode(Digits.ENGLISH)

    local result = persianHex:calculate(number)
    print(result)
end

main()
