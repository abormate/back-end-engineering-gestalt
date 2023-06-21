// ------------------------------------ //
//
// Named Return Values -- 2
//
// ------------------------------------ //

// Even though a function has named return values, we can still explicitly return values if we want to.

func getCoords() (x, y int){
	return x, y // this is explicit
  }

// Using this explicit pattern we can even overwrite the return values:
