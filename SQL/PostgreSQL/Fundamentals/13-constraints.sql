--------------------------------------- //
--
-- SQL -- Constraints --
--
--------------------------------------- //

/*
A constraint is a rule we create on a database that enforces some specific behavior. For example, setting a NOT NULL 
constraint on a column ensures that the column will not accept NULL values.

If we try to insert a NULL value into a column with the NOT NULL constraint, the insert will fail with an error message. 
Constraints are extremely useful when we need to ensure that certain kinds of data exist within our database.

*/

------------------------------ //
-- Defining a Not Null Constraint
------------------------------ //

-- The NOT NULL constraint can be added directly to the CREATE TABLE statement.

CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name UNIQUE,
    title TEXT NOT NULL
)

------------------------------ //
-- Constraint Limitations with SQLite
------------------------------ //

/*
In other dialects of SQL you can ADD CONSTRAINT within an ALTER TABLE statement. SQLite does not support this feature so 
when we create our tables we need to make sure we specify all the constraints we want!

*/

------------------------------ //
-- Assignment -- Practice
------------------------------ //

/*
Thankfully all the tables we have created for CashPal up to this point have been for testing purposes! Now that we have a 
better understanding of constraints, let's rebuild our database with the proper constraints and tables!

Create the USERS table with the following fields and constraints:

id - INTEGER, PRIMARY KEY
name - TEXT, NOT NULL
age - INTEGER, NOT NULL
country_code - TEXT, NOT NULL
username - TEXT, UNIQUE
password - TEXT, NOT NULL
is_admin - BOOLEAN

*/

CREATE TABLE users (
  id INTEGER PRIMARY KEY, 
  name TEXT NOT NULL, 
  age INTEGER NOT NULL, 
  country_code TEXT NOT NULL,
  username TEXT UNIQUE,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

pragma table_info('users');
