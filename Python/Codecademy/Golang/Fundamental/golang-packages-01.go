// -------------------------------------- //
//
//
// -- Golang -- Packages -- Functions --
//
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
------------------------------
-- main Function --
------------------------------

We use the func keyword to declare the Go function main:

-- The func keyword denotes the start of a function declaration.
-- func is followed by the name of the function: main.
-- After the name there follows a pair of parentheses () and a set of curly braces {}.
-- The function code is written inside the set of curly braces.

------------------------------
-- Function Code --
------------------------------

The code inside a function is indented. The code here invokes 
the Println function in the fmt package (that we imported 
earlier) to print the message "Hello World".

------------------------------
-- Invoking Functions --
------------------------------

Normally when we write functions, you need to write code to 
invoke them, otherwise they are unused. However, the main 
function is different if it resides in the main package.

When we have a main function in the main package, this is 
special to Go. When compiled, an executable is produced, 
and when run, the executable uses the main function as the 
starting point.

------------------------------
*/

package main

import "fmt"

