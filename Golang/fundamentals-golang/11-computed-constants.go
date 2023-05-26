// ---------------------------------- //
//
// Computed Constants
//
// ---------------------------------- //

// Constants must be known at compile time. More often than not they will be declared with a static value.

const myInt = 15

// However, constants can be computed so long as the computation can happen at compile time.
// For example, this is valid:

const firstName = "Abe"
const lastName = "Bormate"
const fullName = firstName + " " + lastName

// That said, you cannot declare a constant that can only be computed at run-time.

// --------------------------------- //
//
// Assignment -- Practice
//
// --------------------------------- //

/*
Keeping track of time in a message sending application is critical. Imagine getting an appointment reminder an 
hour after your doctor's visit.

Complete the following code using a computed constant to print the number of seconds in an hour.
*/

package main

import "fmt"

func main() {
	const secondsInMinute = 60
	const minutesInHour = 60
	const secondsInHour = 60*60

	// don't edit below this line
	fmt.Println("number of seconds in an hour:", secondsInHour)
}

