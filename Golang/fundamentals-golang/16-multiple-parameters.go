// ---------------------------- //
//
// Multiple Parameters
//
// ---------------------------- //

/*
When multiple arguments are of the same type, the type only needs to be declared after the last one, 
assuming they are in order.
*/

func add(x, y int) int {
	return x + y
  }

// If they are not (arguments) in order they need to be defined separately.

// --------------------------- //
//
// Assignment -- Practice
//
// --------------------------- //

// Which of the following is the most succinct way to write a function signature?

func createUser(firstName, lastName, string, age int)