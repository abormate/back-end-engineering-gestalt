// -------------------------------- //
//
// Return Values
//
// -------------------------------- //

/*
A function can return a value that the caller doesn't care about. We can explicitly ignore variables 
by using an underscore: _

For example:

*/

func getPoint() (x int, y int) {
	return 3, 4
  }
  
  // ignore y value
  x, _ := getPoint()