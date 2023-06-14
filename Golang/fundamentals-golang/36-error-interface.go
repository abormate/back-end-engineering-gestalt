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