package main

import "fmt"
import "persian-hex/persianhex"

func main() {
	var number int
	hex := &PersianHex{}

	initPersianHex(hex)

	fmt.Println("Enter a non-negative integer:")
	if _, err := fmt.Scanf("%d", &number); err != nil || number < 0 {
		fmt.Println("Error: Please enter a valid integer.")
		return
	}

	setMode(hex, ENGLISH)
	// setMode(hex, PERSIAN)

	calculate(hex, number)
}
