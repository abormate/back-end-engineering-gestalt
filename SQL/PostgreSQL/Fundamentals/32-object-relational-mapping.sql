---------------------------------------- //
--
-- ORMS -- Object Relational Mapping
--
---------------------------------------- //

/*
An Object-Relational Mapping or an ORM for short, is a tool that allows you to perform CRUD operations on a 
database using a traditional programming language. These typically come in the form of a library or framework 
that you would use in your backend code.

The primary benefit an ORM provides is that it maps your database records to in-memory objects. For example, 
in Go we might have a struct that we use in our code:

*/

type User struct {
    ID int
    Name string
    IsAdmin bool
}

/*
This struct definition conveniently represents a database table called users, and an instance of the struct 
represents a row in the table.


*/

----------------------------- //
-- Example -- Using an ORM
----------------------------- //
