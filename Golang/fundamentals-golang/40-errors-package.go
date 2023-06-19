// -------------------------------------- //
//
// Errors Package -- Golang
//
// -------------------------------------- //

/*
The Go standard library provides an "errors" package that makes it easy to deal with errors.

Read the godoc for the errors.New() function, but here's a simple example:

*/

var err error = errors.New("something went wrong")

// -------------------------- //
//  Assignment -- Practice
// -------------------------- //

/*
Textio's software architects may have overcomplicated the requirements from the last coding assignment... oops. 
All we needed was a new generic error message that returns the string no dividing by 0 when a user attempts to get us to perform 
the taboo.

Complete the divide function. Use the errors.New() function to return an error when y == 0 that reads "no dividing by 0".

*/

package main

import (
	"errors"
	"fmt"
)

func divide(x, y float64) (float64, error) {
	if y == 0 {
		// ?
	}
	return x / y, nil
}

// don't edit below this line

func test(x, y float64) {
	defer fmt.Println("====================================")
	fmt.Printf("Dividing %.2f by %.2f ...\n", x, y)
	quotient, err := divide(x, y)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Quotient: %.2f\n", quotient)
}

func main() {
	test(10, 0)
	test(10, 2)
	test(15, 30)
	test(6, 3)
}