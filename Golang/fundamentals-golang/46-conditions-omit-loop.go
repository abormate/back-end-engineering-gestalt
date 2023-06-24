// -------------------------------------- //
//
// Omitting Conditions from a FOR Loop in Golang
//
// -------------------------------------- //

/*
Loops in Go can omit sections of a for loop. For example, the CONDITION (middle part) can be omitted 
which causes the loop to run forever.

*/

for INITIAL; ; AFTER {
	// do something forever
  }

// ------------------------ //
// Assignment -- Practice
// ------------------------ //

/*
Complete the maxMessages function. Given a cost threshold, it should calculate the maximum number of messages that can be sent.

Each message costs 1.0, plus an additional fee. The fee structure is:

1st message: 1.0 + 0.00
2nd message: 1.0 + 0.01
3rd message: 1.0 + 0.02
4th message: 1.0 + 0.03

*/

package main

import (
	"fmt"
)

func maxMessages(thresh float64) int {
	// ?
}

// don't edit below this line

func test(thresh float64) {
	fmt.Printf("Threshold: %.2f\n", thresh)
	max := maxMessages(thresh)
	fmt.Printf("Maximum messages that can be sent: = %v\n", max)
	fmt.Println("===============================================================")
}

func main() {
	test(10.00)
	test(20.00)
	test(30.00)
	test(40.00)
	test(50.00)
}