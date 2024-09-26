// -------------------------------------- //
//
//
// -- Golang -- Packages -- 
//
// -------------------------------------- //

/*
Now that we understand how to compile and run Go programs, 
let’s take a look at Go packages.

Projects can contain many .go files, organized into packages. 
Each package is like a directory: .go files to do with one 
part of your program can go in one package, other .go files 
to do with something else can go into another package. If we 
were writing a calculator program, we could put the files for 
the calculation in package calc and the files for input & 
output in package io.

*/

package main 

import "fmt" 

func main () {
  fmt.Println("Hello World") 
}

/*


*/