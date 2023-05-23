// ---------------------------------
//
// Go programs are easy on memory
//
// ---------------------------------

/*
Go programs are fairly lightweight. Each program includes a small amount of "extra" code that's included in the 
executable binary. This extra code is called the Go Runtime. One of the purposes of the Go runtime is to 
cleanup unused memory at runtime.

In other words, the Go compiler includes a small amount of extra logic in every Go program to make it easier 
for developers to write code that's memory efficient.

*/ 

// --------------------------------
//
// Comparison with other languages
//
// --------------------------------

/*
As a general rule Java programs use more memory than comparable Go programs because Go doesn't use an entire 
virtual machine to run its programs, just a small runtime. The Go runtime is small enough that it is included 
directly in each Go program's compiled machine code.

As another general rule Rust and C++ programs use slightly less memory than Go programs because more control is 
given to the developer to optimize memory usage of the program. The Go runtime just handles it for us 
automatically.

*/

// graph chart comparison of memory usage of Go, Rust, and Java --> https://prnt.sc/Ezv3K8aMeZjl

