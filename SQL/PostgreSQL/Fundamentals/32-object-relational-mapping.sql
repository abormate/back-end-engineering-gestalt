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

-- Using an ORM we might be able to write simple code like this:

user := User{
    ID: 10,
    Name: "Lane",
    IsAdmin: false,
}

// generates a SQL statement and runs it,
// creating a new record in the users table
db.Create(user)

---------------------------- //
-- Example -- Using straight SQL
---------------------------- //

-- Using straight SQL we might have to do something a bit more manual:

user := User{
    ID: 10,
    Name: "Lane",
    IsAdmin: false,
}

db.Exec("INSERT INTO users (id, name, is_admin) VALUES (?, ?, ?);",
    user.ID, user.Name, user.IsAdmin)

--------------------------- //
-- Should you use an ORM?
--------------------------- //

/*


*/