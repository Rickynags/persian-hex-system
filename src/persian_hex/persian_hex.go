package persian_hex

import (
	"fmt"
	"strings"
)

type Digits int

const (
	ENGLISH Digits = iota
	PERSIAN
	ARABIC
)

type PersianHex struct {
	xEquivalent string
	digits      []string
	aliases     []string
	number      int
	mode        Digits
}

func InitPersianHex(hex *PersianHex) {
	hex.xEquivalent = "ش"
	hex.digits = make([]string, 10)
	hex.aliases = []string{"پ", "چ", "ژ", "ف", "گ", "ل"}

	SetMode(hex, ENGLISH)
}

func SetMode(hex *PersianHex, mode Digits) {
	hex.mode = mode

	for i := range hex.digits {
		hex.digits[i] = ""
	}

	switch mode {
	case ENGLISH:
		for i := 0; i < 10; i++ {
			hex.digits[i] = fmt.Sprintf("%d", i)
		}
	case PERSIAN:
		copy(hex.digits, []string{"۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"})
	case ARABIC:
		copy(hex.digits, []string{"٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"})
	}
}

func ConvertToPersianHex(number int, result *strings.Builder, hex *PersianHex) {
	if number == 0 {
		return
	}

	quotient := number / 16
	remainder := number % 16

	ConvertToPersianHex(quotient, result, hex)

	if remainder > 9 {
		result.WriteString(hex.aliases[remainder-10])
	} else {
		result.WriteString(hex.digits[remainder])
	}
}

func Show(hex *PersianHex) {
	var result strings.Builder

	if hex.number == 0 {
		fmt.Printf("%s%s\n", hex.digits[0], hex.xEquivalent)
		return
	}

	ConvertToPersianHex(hex.number, &result, hex)
	fmt.Printf("%s%s%s\n", hex.digits[0], hex.xEquivalent, result.String())
}

func Validate(number int) bool {
	return number >= 0
}

func Calculate(hex *PersianHex, number int) {
	if !Validate(number) {
		fmt.Println("Error: Please enter a valid non-negative integer.")
		return
	}

	hex.number = number
	Show(hex)
}
