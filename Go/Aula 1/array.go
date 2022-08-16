package main

import (
	"fmt"
)

func tabuada(a int) {
	array1 := [10]int{}
	for i := 0; i < 10; i++ {
		array1[i] = a * i
	}

	for i := 0; i < 10; i++ {
		fmt.Println("a*[", i, "] = ", array1[i])
	}

}

func main() {
	var a int
	fmt.Println("Entre com o valor de a: ")
	fmt.Scan(&a)
	tabuada(a)
}
