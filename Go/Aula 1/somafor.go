package main

import (
	"fmt"
)

func main() {
	var a float32
	var b float32
	var resultado float32
	var flag bool

	fmt.Println("Deseja fazer uma soma? false == não true == sim ")
	fmt.Scan(&flag)

	for flag == true {
		fmt.Println("Entre com 2 valores: ")
		fmt.Scan(&a, &b)
		resultado = a + b
		fmt.Println("Resultado da soma: ", resultado)
		fmt.Println("Deseja fazer uma soma? false == não true == sim ")
		fmt.Scan(&flag)
	}
}
