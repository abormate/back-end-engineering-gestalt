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


*/