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

