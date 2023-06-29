// ------------------------------------ //
//
// Fizzbuzz -- Golang
//
// ------------------------------------ //

// Go supports the standard modulo operator

7 % 3 // 1

// Logical AND operator

true && false // false
true && true // true

// Logical OR operator

true || false // true
false || false // false

// ------------------------- //
// Assignment -- Practice
// ------------------------- //

/*
We're hiring engineers at Textio, so time to brush up on the classic "Fizzbuzz" game, a coding exercise that has been dramatically 
overused in coding interviews across the world.

Complete the fizzbuzz function that prints the numbers 1 to 100 inclusive each on their own line, but substitutes multiples of 3 
for the text fizz and multiples of 5 for buzz. For multiples of 3 AND 5 print instead fizzbuzz.

*/

package main

func fizzbuzz() {
	for i := 1; i < 101; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("fizzbuzz")
		} else if i%3 == 0 {
			fmt.Println("fizz")
		} else if i%5 == 0 {
			fmt.Println("buzz")
		} else {
			fmt.Println(i)
		}
	}
}

// don't touch below this line

func main() {
	fizzbuzz()
}


