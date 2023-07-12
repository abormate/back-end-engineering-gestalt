--------------------------------------- //
--
-- Comparing SQL databases
--
--------------------------------------- //

/*
Let's dive deeper and talk about some of the popular SQL Databases and what makes them different from one another. 
Some of the most popular SQL Databases right now are:

OracleDB
MySQL
Microsoft SQL Server
PostgreSQL
SQLite
Microsoft Access
And many others

While all of these Databases use SQL, each database defines specific rules, practices, and strategies that separate 
them from their competitors.

*/

--------------------------- //
-- SQLite vs PostgreSQL
--------------------------- //

/*
Personally, SQLite and PostgreSQL are my favorites from the list above. Postgres is a very powerful, open-source, 
production-ready SQL database. SQLite is a lightweight, embeddable, open-source database. I usually choose one of these 
technologies if I'm doing SQL work.

SQLite is a serverless database management system (DBMS) that has the ability to run within applications, whereas 
PostgreSQL uses a Client-Server model and requires a server to be installed and listening on a network, similar to an 
HTTP server.

For this course, we'll utilize SQLite
*/

--------------------------- //
-- Assignment -- Practice
--------------------------- //

/*
The CashPal codebase already has some logic that makes a table. Let's watch how SQLite does not enforce type checking. 
Notice that within the CREATE TABLE statement, name is defined as a TEXT field.

On line 3 change the text string 'Montgomery Burns' to the integer 1 and run the code!

Notice how even though we defined name as a TEXT field, SQLite allowed us to use an integer! Like Python and JavaScript, 
SQLite has a loose type system. Yet another reason PostgreSQL is often a better choice in production.

*/

CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);
INSERT into users (id, name, age) values (1, 'John Doe', 21);
INSERT into users (id, name, age) values (2, 'Montgomery Burns', 33);
SELECT * from users;

CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);
INSERT into users (id, name, age) values (1, 'John Doe', 21);
INSERT into users (id, name, age) values (2, '1', 33);
SELECT * from users;

/*
SQLite still runs the code with type name defined as TEXT, modified to become an integer 1

*/