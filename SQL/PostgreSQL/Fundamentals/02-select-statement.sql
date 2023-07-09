---------------------------------------- //
--
-- SQL Select Statement
--
---------------------------------------- //

/*
Let's write our own SQL statement from scratch! A SELECT statement is the most common operation in SQL - often called a "query". 
SELECT retrieves data from one or more tables. Standard SELECT statements do not alter the state of the database.

*/

SELECT id from users;

/*
Select a Single Field 
----------------------

A SELECT statement begins with the keyword Select followed by the fields that you want to retrieve.


*/

SELECT id from users;

/*
Select from multiple fields
---------------------------
If you want to select more than one field you can specify multiple fields separated by commas


*/

SELECT id, age from users;

/*
Select All fields 
-----------------
If you want to select every field within a record you can denote this by using the shorthand * syntax

*/

SELECT * from users;

/*
After specifying fields, you need to indicate which table you want to pull the records from using the from statement followed by
the name of the table. We'll talk more about tables later, but for now, you can think about them like structs or objects. 

For example, the users table might have 3 fields:

id
name
balance

And finally, all statements end with a semi-colon ;

*/

------------------------- //
-- Assignment -- Practice
------------------------- //

/*
The state of our CashPal users table is as follows:

ID	NAME	AGE	BALANCE	IS ADMIN
1	John Smith	28	450	1
2	Darren Walker	27	200	1
2	Jane Morris	33	496.24	0


It's very common to write queries that only return specific portions of data from a table. Our HR team has requested a report asking for all the names and balances of all of our users.

Write a query that retrieves all of the user's names and balances.

*/

SELECT name, balance from users;