// ---------------------------------
//
// Short Variable Declaration
//
// ---------------------------------

/*
Inside a function (even the main function), the := short assignment statement can be used in place of a var 
declaration. The := operator infers the type of the new variable based on the value.

*/

var empty string

// is the same as...

empty := ""

// furthermore

numCars := 10 // inferred to be an integer

temperature := 0.0 // temperature is inferred to be a floating point value because it has a decimal point

var isFunny = true // isFunny is inferred to be a boolean

/*
Outside of a function (in the global/package scope), every statement begins with a keyword (var, func, and so on)
 and so the := construct is not available.

*/

package main

import "fmt"

func main() {
	// declare here
	congrats := "happy birthday!"

	fmt.Println(congrats)
}

