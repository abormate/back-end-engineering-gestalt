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
