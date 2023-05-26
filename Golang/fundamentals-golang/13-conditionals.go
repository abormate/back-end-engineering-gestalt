// ------------------------------- //
//
// Golang Conditionals
//
// ------------------------------- //

// if statements in Go don't use parentheses around the condition:

if height > 4 {
    fmt.Println("You are tall enough!")
}

// else if and else are supported

if height > 6 {
    fmt.Println("You are super tall!")
} else if height > 4 {
    fmt.Println("You are tall enough!")
} else {
    fmt.Println("You are not tall enough!")
}

