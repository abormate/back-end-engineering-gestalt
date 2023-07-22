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



