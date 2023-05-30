// ------------------------------------ //
//
// Nested Structs 
//
// ------------------------------------ //

// Structs can be nested to represent more complex entities:

type car struct {
	Make string
	Model string
	Height int
	Width int
	FrontWheel Wheel
	BackWheel Wheel
  }
  
  type Wheel struct {
	Radius int
	Material string
  }

// The fields of a struct can be accessed using the dot . operator.

myCar := car{}
myCar.FrontWheel.Radius = 5