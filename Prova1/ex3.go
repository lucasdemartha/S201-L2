package main

import (
	"fmt"
)

func tabuada(a int) {
	array1 := [21]int{}
	for i := 20; i >= 0; i-- {
		array1[i] = a * i
	}

	for i := 20; i >= 0; i-- {
		fmt.Println("a*[", i, "] = ", array1[i])
	}

}

func main() {
	var a int
	fmt.Println("Entre com o valor de a: ")
	fmt.Scan(&a)
	tabuada(a)
}
