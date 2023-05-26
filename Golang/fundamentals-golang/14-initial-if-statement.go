// ----------------------------------- //
//
// Initial Statement for IF Loops
//
// ---------------------------------- //

/*
An if conditional can have an "initial" statement. The variable(s) created in the initial statement are 
only defined within the scope of the if body.
*/

if INITIAL_STATEMENT; CONDITION {
}

// ---------------------------------- //
//
// Example -- Initial
//
// ---------------------------------- //

// Instead of doing it like this...

length := getLength(email)
if length < 1 {
    fmt.Println("Email is invalid")
}

// We can shorten the code with an Initial statement for IF loops

if length := getLength(email); length < 1 {
    fmt.Println("Email is invalid")
}

