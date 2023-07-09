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

