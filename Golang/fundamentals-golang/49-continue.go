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