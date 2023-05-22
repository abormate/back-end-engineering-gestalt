// -------------------------------
//
// Compiled versus Interpreted?
//
// -------------------------------

/*
Compiled programs can be run without access to the original source code, and without access to a compiler. For 
example, when your browser executes the code you write in this course, it doesn't use the original code, just 
the compiled result.

Note how this is different than interpreted languages like Python and JavaScript. With Python and JavaScript 
the code is interpreted at runtime by a separate program known as the "interpreter". Distributing code for 
users to run can be a pain because they need to have an interpreter installed, and they need access to the 
original source code.
*/

// Examples of Compiled languages
// -- Go
// -- C
// -- C++
// -- Rust

// Examples of Interpreted languages
// -- JavaScript
// -- Python
// -- Ruby

// ----------------------------
// 
// Why build TextIO in a compiled language?
//
// ----------------------------

/*
One of the most convenient things about using a compiled language like Go for Textio is that when we deploy 
our server we don't need to include any runtime language dependencies like Node or a Python interpreter. We 
just add the pre-compiled binary to the server and start it up!
*/

