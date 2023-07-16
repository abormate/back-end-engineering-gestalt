------------------------------------------ //
--
-- SQL data types
--
------------------------------------------ //

/*
SQL as a language can support many different data types. However, the datatypes that your database management system (DBMS) 
supports will vary depending on the specific database you're using.

SQLite only supports the most basic types, and we're using SQLite in this course!

*/

---------------------------- //
-- SQLite Data Types
---------------------------- //

/*
Let's go over the data types supported by SQLite: and how they are stored.

NULL - Null value.
INTEGER - A signed integer stored in 0,1,2,3,4,6, or 8 bytes.
REAL - Floating point value stored as an 64-bit IEEE floating point number.
TEXT - Text string stored using database encoding such as UTF-8
BLOB - Short for Binary large object and typically used for images, audio or other multimedia.
Its important to note - SQLite does not have a separate BOOLEAN storage class. Instead boolean values are stored as integers:

0 is false
1 is true


SQLite will still let you write your queries using Boolean expressions and true/false keywords, but it will convert the booleans to integers under-the-hood.

*/

--------------------------- //
-- How is a "true" boolean value stored and presented in SQLite?
--------------------------- //

-- 1

