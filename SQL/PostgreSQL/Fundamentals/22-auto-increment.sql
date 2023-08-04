--------------------------------------- //
--
-- Auto Increment -- SQL LearnSpace
--
--------------------------------------- //

/**************************************

Many dialects of SQL support an AUTO INCREMENT feature. When inserting records into a table with AUTO INCREMENT enabled, 
the database will assign the next value automatically. In SQLite an integer id field that has the PRIMARY KEY constraint 
will auto increment by default!

**************************************/

/*

IDs

Depending on how your database is set up, you may be using traditional ids or you may be using UUIDs. SQL doesn't support auto 
incrementing a uuid so if your database is using them your server will have to handle the changing uuid's for each record.

*/

/*

Using Auto Increment with SQLite

We are using traditional ids in our database, so we can take advantage of the auto increment feature. Different dialects of 
SQL will implement this feature differently, but in SQLite any id field that has the PRIMARY KEY constraint will auto increment! 
So we can omit the id field within the INSERT statement and allow the database to automatically add that field for us!

*/


----------------------------- //
-- Assignment -- Practice --
----------------------------- //

/*
Let's add some more records but allow the database to automatically increment the id field. 
Add the following records to the database:

RECORD 1
name: Lance
age: 20
country_code: US
username: LanChr
password: b00tdevisbest
is_admin: false


RECORD 2
name: Tiffany
age: 28
country_code: US
username: Tifferoon
password: autoincrement
is_admin: true

*/

/* SETUP CODE */

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country_code TEXT NOT NULL,
    username TEXT UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN
);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (3, 'John', 39, 'CA', 'Jjdev21', 'welovebootdev', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (4, 'Ram', 42, 'IN', 'Ram11c', 'thisSQLcourserocks', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (5, 'Hunter', 30, 'US', 'Hdev92', 'backendDev', false);

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (6, 'Allan', 27, 'US', 'Alires', 'iLoveB00tdev', true);


/* END SETUP CODE */


/* ANSWER CODE */

INSERT INTO users (name, age, country_code, username, password, is_admin)
  VALUES ('Lance', 20, 'US', 'LanChr', 'b00tdevisbest', false), 
  ('Tiffany', 28, 'US', 'Tifferoon', 'autoincrement', true);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

SELECT * FROM users;
