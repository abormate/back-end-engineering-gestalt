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

--------------------------- //
-- Assignment -- Practice --
--------------------------- //

/*
Let's begin building a table for CashPal database! Create the people table with the following fields:

id - Integer
handle - Text
name - Text
age - Integer
balance - Integer
is_admin - boolean


TIP
The pragma table_info(TABLENAME); command returns information about a table and its fields. You don't need to edit this line, 
I just thought you might be curious!

*/

CREATE TABLE people(
  id INTEGER,
  handle TEXT,
  name TEXT,
  age INTEGER,
  balance integer,
  is_admin boolean
  
);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

pragma table_info('people');