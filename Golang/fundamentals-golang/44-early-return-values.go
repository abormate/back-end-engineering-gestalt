// ------------------------------------ //
//
// Early Returns Values -- Golang
//
// ------------------------------------ //

/*
Go supports the ability to return early from a function. This is a powerful feature that can clean up code, especially when 
used as guard clauses.

Guard Clauses leverage the ability to return early from a function (or continue through a loop) to make nested conditionals 
one-dimensional. Instead of using if/else chains, we just return early from the function at the end of each conditional block.

*/

func divide(dividend, divisor int) (int, error) {
	if divisor == 0 {
		return 0, errors.New("Can't divide by zero")
	}
	return dividend/divisor, nil
}

