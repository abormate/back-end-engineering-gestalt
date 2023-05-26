// ---------------------------------- //
//
// Declaration Syntax
//
// ---------------------------------- //

/*
Developers often wonder why the declaration syntax in Go is different from the tradition established in the C 
family of languages.

*/

// ---------------------------- //
//  C-style syntax
// ---------------------------- //

/*
The C language describes types with an expression including the name of to be declared, and states 
what type that expression will have.

*/

int y;

/*
Interestingly, the creators of the Go language agreed that the C-style of declaring types in 
signatures gets confusing really fast - take a look at this nightmare.

*/

int (*fp)(int (*ff)(int x, int y), int b)

// ---------------------------- //
//  Go-style syntax
// ---------------------------- //

// GO's declaration are clear. You need to read them left to right, just like you would English.

x int
p *int
a [3]int

// It's nice for more complex signatures, it makes them easier to read.

f func(func(int,int) int, int) int

// -------------------------- //
//  Assignment -- Practice
// -------------------------- //

/*
What are we talking about when we discuss declaration syntax?
*/

// The style of language used to create new variables, types, functions, et ceterra...

