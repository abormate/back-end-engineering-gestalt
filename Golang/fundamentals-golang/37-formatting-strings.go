// ------------------------------------ //
//
// Formatting Strings
//
// ------------------------------------ //

/*
A convenient way to format strings in Go is by using the standard library's fmt.Sprintf() function. It's a string interpolation 
function, similar to JavaScript's built-in template literals. The %v substring uses the type's default formatting, which is often 
what you want.

*/

// Default Values
const name = "Kim"
const age = 22
s := fmt.Sprintf("%v is %v years old.", name, age)
// s = "Kim is 22 years old."

// Equivalent in JavaScript code:
const name = 'Kim'
const age = 22
s = `${name} is ${age} years old.`
// s = "Kim is 22 years old."

// Rounding Float values
fmt.Printf("I am %f years old", 10.523)
// I am 10.523000 years old

// The ".2" rounds the number to 2 decimal places
fmt.Printf("I am %.2f years old", 10.523)
// I am 10.53 years old