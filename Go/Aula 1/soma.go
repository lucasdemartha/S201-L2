package main

import (
	"fmt"
)

func main() {
	var a float32
	var b float32
	var resultado float32
	fmt.Println("Entre com 2 valores: ")
	fmt.Scan(&a, &b)
	resultado = a + b
	fmt.Println("Resultado da soma: ", resultado)
}
