// go build -o persian_hex_go.exe ./src
package main

import "fmt"
import "github.com/basemax/persian-hex-system/src/persian_hex"

func main() {
    var number int
    hex := &persian_hex.PersianHex{}

    persian_hex.InitPersianHex(hex)

    if _, err := fmt.Scanf("%d", &number); err != nil || number < 0 {
        fmt.Println("Error: Please enter a valid integer.")
        return
    }

    persian_hex.SetMode(hex, persian_hex.ENGLISH)
    // persian_hex.SetMode(hex, persian_hex.PERSIAN)

    persian_hex.Calculate(hex, number)
}
