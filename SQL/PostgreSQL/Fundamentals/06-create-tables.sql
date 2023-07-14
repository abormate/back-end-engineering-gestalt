---------------------------------------- //
--
-- SQL LearnSpace -- Creating a Table --
--
---------------------------------------- //

-- The CREATE TABLE statement is used to create a new table in a database.

/*
To create a table, use the CREATE TABLE statement followed by the name of the table and the fields you want in the table.

*/

CREATE TABLE employees (id INTEGER, name TEXT, age INTEGER, is_manager BOOLEAN, salary INTEGER);

-- Each field name is followed by its datatype. We'll get to data types in a minute.

/*
It's also acceptable and common to break up the CREATE TABLE statement with some whitespace like this:

*/

CREATE TABLE employees(
    id INTEGER,
    name TEXT,
    age INTEGER,
    is_manager BOOLEAN,
    salary INTEGER
);