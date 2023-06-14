// ------------------------------------ //
//
// Error Interface -- Golang
//
// ------------------------------------ //

/*
Go programs express errors with error values. An Error is any type that implements the simple built-in error interface:

*/

type error interface {
    Error() string
}

/*
When something can go wrong in a function, that function should return an error as its last return value. 
Any code that calls a function that can return an error should handle errors by testing whether the error is nil.

*/

// Atoi converts a stringified number to an integer
i, err := strconv.Atoi("42b")
if err != nil {
    fmt.Println("couldn't convert:", err)
    // because "42b" isn't a valid integer, we print:
    // couldn't convert: strconv.Atoi: parsing "42b": invalid syntax
    // Note:
    // 'parsing "42b": invalid syntax' is returned by the .Error() method
    return
}
// if we get here, then
// i was converted successfully