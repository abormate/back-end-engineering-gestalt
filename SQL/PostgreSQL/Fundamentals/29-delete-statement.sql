---------------------------------------- //
--
-- Delete -- Statement -- 
--
---------------------------------------- //

/*
When a user deletes their account on Twitter, or deletes a comment on a YouTube video, that data needs to be 
removed from its respective database.

*/

--------------------------- //
-- Delete Statement 
--------------------------- //

/*
A DELETE statement removes a record from a table that match the WHERE clause. As an example:

*/

DELETE from employees
    WHERE id = 251;

/*
This DELETE statement removes all records from the employees table that have an id of 251!

*/

------------------------------ //
-- Assignment -- Practice
------------------------------ //

/*
Samantha, one of our CashPal users, has opted to delete her account and stop using our app... 
which makes us sad. Anyways, we need to remove her record from the database!

Delete Samantha's record from the user table.

*/

