// ------------------------------- //
// 
// Continue -- Golang
//
// ------------------------------- //

/*
The continue keyword stops the current iteration of a loop and continues to the next iteration. continue is a powerful way 
to use the "guard clause" pattern within loops.

*/

for i := 0; i < 10; i++ {
	if i % 2 == 0 {
	  continue
	}
	fmt.Println(i)
  }
  // 1
  // 3
  // 5
  // 7
  // 9

// ------------------- //
// Break
// ------------------- //

/*
The break keyword stops the current iteration of a loop and exits the loop.

*/

for i := 0; i < 10; i++ {
	if i == 5 {
	  break
	}
	fmt.Println(i)
  }
  // 0
  // 1
  // 2
  // 3
  // 4

// -------------------- //
// Assignment -- Practice
// -------------------- //

/*
As an easter egg, we decided to reward our users with a free text message if they send a prime number of text messages this year.

Complete the printPrimes function. It should print all of the prime numbers up to and including max. It should skip any numbers 
that are not prime.

Here's the psuedocode:

*/

printPrimes(max):
  for n in range(2, max+1):
    if n is 2:
      n is prime, print it
    if n is even:
      n is not prime, skip to next n
    for i in range (3, sqrt(n) + 1):
      if i can be multiplied into n:
        n is not prime, skip to next n
    n is prime, print it

/*
We skip even numbers because they can't be prime
We only check up to the square root because anything higher than the square root has no chance of multiplying evenly 
into n
We start checking at 2 because 1 is not prime

*/

package main

import (
	"fmt"
)

func printPrimes(max int) {
	// ?
}

// don't edit below this line

func test(max int) {
	fmt.Printf("Primes up to %v:\n", max)
	printPrimes(max)
	fmt.Println("===============================================================")
}

func main() {
	test(10)
	test(20)
	test(30)
}