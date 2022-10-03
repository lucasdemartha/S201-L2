package main

import (
	"fmt"
)

func main() {
	var x int
  fmt.Print("Entre com o raio do circulo: ")
  fmt.Scan(&x)
  fmt.Println(diametro(x))
  fmt.Println(area(float32(x)))
}

func diametro (x int) int{
  return x*2
}
func area(y float32) float32{
  return (3.14*(y*y))
}
