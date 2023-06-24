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
fmt.Println("plant has grown to ", plantHeight, "inches")

