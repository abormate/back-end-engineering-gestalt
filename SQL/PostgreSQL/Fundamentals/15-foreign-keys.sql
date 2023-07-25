---------------------------------------- //
--
-- SQL LearnSpace -- Foreign Keys --
--
---------------------------------------- //

/*
Foreign keys are what makes relational databases relational! Foreign keys define the relationships between tables. Simply put, 
a FOREIGN KEY is a field in one table that references another table's PRIMARY KEY.

*/

----------------------------- //
-- Creating of Foreign Key
----------------------------- //

/*
Creating a FOREIGN KEY in SQLite happens at table creation! After we define the table fields and constraints we add an 
additional CONSTRAINT where we define the FOREIGN KEY and its REFERENCES.

*/

-- Here's an example ...

CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(id)
);