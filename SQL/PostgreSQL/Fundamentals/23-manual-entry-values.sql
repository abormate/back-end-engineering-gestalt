---------------------------------------- //
--
-- Manual Entry of Values
--
---------------------------------------- //

/*
Manually INSERTing every single record in a database would be an extremely time-consuming task! Working with 
raw SQL as we are now is not super common when designing backend systems.

When working with SQL within a software system, like a backend web application, you'll typically have access 
to a programming language such as Go or Python. For example, a backend server written in Go can use string 
concatenation to dynamically create SQL statements, and that's usually how it's done!

*/

sqlQuery := fmt.Sprintf(`
INSERT INTO users(name, age, country_code)
VALUES ('%s', %v, %s);
`, user.Name, user.Age, user.CountryCode)

--------------------------- //
-- SQL Injection
--------------------------- //

/*
The example above is an oversimplification of what really happens when you access a database using Go code. 
In essence, it's correct. String interpolation is how production systems access databases. That said, it 
must be done carefully to not be a security vulnerability. We'll talk more about that later!

*/

/***************************
-- Assignment -- Practice --
***************************/

/*
Question No. 1 -- Every time someone creates an account on boot.dev Allan or Lane has to manually add them to the database 
by hand-writing a SQL query

*/

-- >> Answer --> False 

/*
Question No. 2 -- Within backend systems, SQL queries are typically ... 

*/










