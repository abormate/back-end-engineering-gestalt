---------------------------------------- //
--
-- 1st Normal Form (1NF) -- SQL LearnSpace
--
---------------------------------------- //

/*
To be compliant with first normal form, a database table simply needs to follow 2 rules:

-- It must have a unique primary key.
-- A cell can't have a nested table as its value (depending on the database you're using, this may not even be possible)

*/

---------------------------- //
-- Example of NOT 1st Normal Form
---------------------------- //

/*

name	age	email
Lane	27	lane@boot.dev
Lane	27	lane@boot.dev
Allan	27	allan@boot.dev


This table does not adhere to 1NF. It has two identical rows, so there isn't a unique primary key for each row.

*/

--------------------------- //
-- Example of 1st Normal Form
--------------------------- //

/*
The simplest way (but not the only way) to get into first normal form is to add a unique id column.

id	name	age	email
1	Lane	27	lane@boot.dev
2	Lane	27	lane@boot.dev
3	Allan	27	allan@boot.dev


It's worth noting that if you create a "primary key" by ensuring that two columns are always "unique together" that works too.

*/

------------------------- //
-- You should almost NEVER design a table that does not adhere to 1NF
------------------------- //

/*
First normal form is simply a good idea. I've never built a database schema where each table isn't at least in first normal form.

*/