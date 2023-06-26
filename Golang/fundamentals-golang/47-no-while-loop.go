// ------------------------------------ //
//
// There is no WHILE Loop in Golang
//
// ------------------------------------ //

/*
Most programming languages have a concept of a while loop. Because Go allows for the omission of sections of a for loop, a while 
loop is just a for loop that only has a CONDITION.

*/

for CONDITION {
	// do some stuff while CONDITION is true
  }

// For example ...

plantHeight := 1
for plantHeight < 5 {
  fmt.Println("still growing! current height:", plantHeight)
  plantHeight++
}
fmt.Println("plant has grown to ", plantHeight, "")



// --------------------- //
// Assignment -- Practice
// --------------------- //

/*
We have an interesting new cost structure from our SMS vendor. They charge exponentially more money for each consecutive text we send! 
Let's write a function that can calculate how many messages we can send in a given batch given a costMultiplier and a maxCostInPennies.

In a nutshell, the first message costs a penny, and each message after that costs the same as the previous message multiplied by 
the costMultiplier. That gets expensive!

There is an infinite loop in the code! Let's add a condition to fix the bug. The loop should exit before incrementing 
maxMessagesToSend if the cost of the next message would go over the max cost.

*/

package main

import (
	"fmt"
)

func getMaxMessagesToSend(costMultiplier float64, maxCostInPennies int) int {
	actualCostInPennies := 1.0
	maxMessagesToSend := 0
	for actualCostInPennies <= float64(maxCostInPennies) {
		maxMessagesToSend++
		actualCostInPennies *= costMultiplier
	}
	return maxMessagesToSend
}

// don't touch below this line

func test(costMultiplier float64, maxCostInPennies int) {
	maxMessagesToSend := getMaxMessagesToSend(costMultiplier, maxCostInPennies)
	fmt.Printf("Multiplier: %v\n",
		costMultiplier,
	)
	fmt.Printf("Max cost: %v\n",
		maxCostInPennies,
	)
	fmt.Printf("Max messages you can send: %v\n",
		maxMessagesToSend,
	)
	fmt.Println("====================================")
}

func main() {
	test(1.1, 5)
	test(1.3, 10)
	test(1.35, 25)
}