// ----------------------------------- //
//
// Clean Interfaces -- Golang
// 
// ----------------------------------- //

/*
Writing clean interfaces is hard. Frankly, anytime you’re dealing with abstractions in code, the simple can become complex 
very quickly if you’re not careful. Let’s go over some rules of thumb for keeping interfaces clean.

*/

// ---------------------------------- //

// 1. KEEP INTERFACES SMALL
/*
If there is only one piece of advice that you take away from this article, make it this: keep interfaces small! Interfaces are 
meant to define the minimal behavior necessary to accurately represent an idea or concept.

*/

/*
Here is an example from the standard HTTP package of a larger interface thats a good example of defining minimal behavior:

*/

type File interface {
    io.Closer
    io.Reader
    io.Seeker
    Readdir(count int) ([]os.FileInfo, error)
    Stat() (os.FileInfo, error)
}

/*
Any type that satisfies the interface’s behaviors can be considered by the HTTP package as a File. This is convenient because the 
HTTP package doesn’t need to know if it’s dealing with a file on disk, a network buffer, or a simple []byte

*/

// ----------------------------------- //

// 2. INTERFACES SHOULD HAVE NO KNOWLEDGE OF SATISFYING TYPES
/*
An interface should define what is necessary for other types to classify as a member of that interface. They shouldn’t be aware 
of any types that happen to satisfy the interface at design time.

*/

/*
For example, let’s assume we are building an interface to describe the components necessary to define a car.

*/

type car interface {
	Color() string
	Speed() int
	IsFiretruck() bool
}

/*
Color() and Speed() make perfect sense, they are methods confined to the scope of a car. IsFiretruck() is an anti-pattern. 
We are forcing all cars to declare whether or not they are firetrucks. In order for this pattern to make any amount of sense, 
we would need a whole list of possible subtypes. IsPickup(), IsSedan(), IsTank()… where does it end??

Instead, the developer should have relied on the native functionality of type assertion to derive the underlying type when given 
an instance of the car interface. Or, if a sub-interface is needed, it can be defined as:

*/

type firetruck interface {
	car
	HoseLength() int
}

/*
Which inherits the required methods from car and adds one additional required method to make the car a firetruck.


// 3. Interfaces are NOT classes

-- Interfaces are not classes, they are slimmer.
-- Interfaces don’t have constructors or deconstructors that require that data is created or destroyed.
-- Interfaces aren’t hierarchical by nature, though there is syntactic sugar to create interfaces that happen to be supersets of other 
interfaces.

-- Interfaces define function signatures, but not underlying behavior. Making an interface often won’t DRY up your code in regards to 
struct methods. For example, if five types satisfy the fmt.Stringer interface, they all need their own version of the String() function.
*/

// --------------------------- //
// Interfaces should have as _ methods as possible
// --------------------------- //

// Initial
// Few

// --------------------------- //
// It's okay for types to be aware of the interfaces they satisfy
// --------------------------- //

// Initial
// True

// -------------------------- //
// It's okay for interfaces to be aware of the types that satisfy them
// -------------------------- //

// Initial
// False

// -------------------------- //
// Interfaces allow you to define a method's behavior once and use it for many different types
// -------------------------- //

// Initial
// False

