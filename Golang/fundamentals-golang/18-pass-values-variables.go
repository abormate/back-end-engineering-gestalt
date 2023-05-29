// ------------------------------ //
//
// Passing Variables by value
//
// ------------------------------ //

/*
Variables in Go are passed by value (except for a few data types we haven't covered yet). "Pass by value" means 
that when a variable is passed into a function, that function receives a copy of the variable. The function is 
unable to mutate the caller's original data

*/

func main(){
    x := 5
    increment(x)

    fmt.Println(x)
    // still prints 5,
    // because the increment function
    // received a copy of x
}

func increment(x int){
    x++
}

// ------------------------ //
//  Assignment -- Practice
// ------------------------ //

/*
It's critical in Textio that we keep track of how many SMS messages we send on behalf of our clients. 
Fix the bug to accurately track the number of SMS messages sent.

Modify the incrementSends function so that it returns the result after incrementing the sendsSoFar.
Fix main() to capture the return value from incrementSends() and overwrite the previous sendsSoFar value.

*/

package main

import "fmt"

func main() {
	sendsSoFar := 430
	const sendsToAdd = 25
	sendsSoFar = incrementSends(sendsSoFar, sendsToAdd)
	fmt.Println("you've sent", sendsSoFar, "messages")
}

func incrementSends(sendsSoFar, sendsToAdd int) int {
	return sendsSoFar + sendsToAdd
}
