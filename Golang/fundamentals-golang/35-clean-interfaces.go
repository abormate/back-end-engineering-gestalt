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

// 1.
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

// 2.
/*
An interface should define what is necessary for other types to classify as a member of that interface. They shouldn’t be aware 
of any types that happen to satisfy the interface at design time.

*/

/*
For example, let’s assume we are building an interface to describe the components necessary to define a car.

*/

