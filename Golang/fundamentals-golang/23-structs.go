// ------------------------------------ //
//
// Structs 
//
// ------------------------------------ //

/*
We use structs in Go to represent structured data. It's often convenient to group different types of variables 
together. For example, if we want to represent a car we could do the following:

*/

type car struct {
	Make string
	Model string
	Height int
	Width int
  }

/*
This creates a new struct type called car. All cars have a Make, Model, Height and Width.

*/

