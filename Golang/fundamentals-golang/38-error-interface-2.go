// ------------------------------------ //
//
// Error Interface -- Golang -- Part 2
//
// ------------------------------------ //

/*
Because errors are just interfaces, you can build your own custom types that implement the error interface. Here's an example of 
a userError struct that implements the error interface:

*/

type userError struct {
    name string
}

func (e userError) Error() string {
    return fmt.Sprintf("%v has a problem with their account", e.name)
}