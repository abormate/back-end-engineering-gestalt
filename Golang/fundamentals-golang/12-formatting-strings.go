// ---------------------------- //
//
// Formatting Strings in Go
//
// ---------------------------- //

/*
Go follows the printf tradition from the C language. In my opinion, string formatting/interpolation in Go 
is currently less elegant than JavaScript and Python.

-->   fmt.Printf - Prints a formatted string to standard out.
-->   fmt.Sprintf() - Returns the formatted string

*/

// ----------------------------------------------------- //
/*
Examples --
These formatting verbs work with both fmt.Printf and fmt.Sprintf.

%V -- Interpolate the default representation

The %v variant prints the Go syntax representation of a value. You can usually use this if you're unsure 
what else to use. That said, it's better to use the type-specific variant if you can.
*/
// ----------------------------------------------------- //

s := fmt.Sprintf("I am %v years old", 10)
// I am 10 years old

s := fmt.Sprintf("I am %v years old", "way too many")
// I am way too many years old


// ----------------------------------------------------- //
//  %s -- Interpolate a String
// ----------------------------------------------------- //

s := fmt.Sprintf("I am %s years old", "way too many")
// I am way too many years old




// ----------------------------------------------------- //
// %D -- Interpolate an integer in decimal form
// ----------------------------------------------------- //

s := fmt.Sprintf("I am %d years old", 10)
// I am 10 years old



// ----------------------------------------------------- //
// %F -- Interpolate a decimal
// ----------------------------------------------------- //

s := fmt.Sprintf("I am %f years old", 10.523)
// I am 10.523000 years old

// The ".2" rounds the number to 2 decimal places
s := fmt.Sprintf("I am %.2f years old", 10.523)
// I am 10.53 years old


// ----------------------------------------------------- //
//
//  Assignment -- Practice
//
// ----------------------------------------------------- //

/*
Create a new variable called msg on line 9. It's a string that contains the following:

--> Hi NAME, your open rate is OPENRATE percent

Where NAME is the given name, and OPENRATE is the openRate rounded to the nearest "tenths" place.

*/

package main

import "fmt"

func main() {
	const name = "Saul Goodman"
	const openRate = 30.5

	msg := fmt.Sprintf("Hi %s, your open rate is %.1f percent", name, openRate) 

	// don't edit below this line

	fmt.Println(msg)


	
