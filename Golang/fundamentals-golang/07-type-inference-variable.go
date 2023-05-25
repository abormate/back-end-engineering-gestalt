// ---------------------------------
//
// Variable Type inference
//
// ---------------------------------

/*
To declare a variable without specifying an explicit type (either by using the := syntax or var = expression 
	syntax), the variable's type is inferred from the value on the right hand side.

When the right hand side of the declaration is typed, the new variable is of that same type:

*/

var i int
j := i // j is also an int

/*
However, when the right hand side is a literal value (an untyped numeric constant like 42 or 3.14), the new 
variable will be an int, float64, or complex128 depending on its precision:

*/