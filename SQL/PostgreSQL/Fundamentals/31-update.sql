---------------------------------------- //
--
-- Update SQL statement
--
---------------------------------------- //

/*
Whenever you update your profile picture or change your password online, you are changing the data in a field 
on a table in a database! Imagine if every time you accidentally messed up a Tweet on Twitter you had to 
delete the entire tweet and post a new one instead of just editing it...

...Well, that's a bad example.

*/

-------------------------- //
-- Update Statement
-------------------------- //

/*
The UPDATE statement in SQL allows us to update the fields of a record. We can even update many records 
depending on how we write the statement.

An UPDATE statement specifies the table that needs to be updated, followed by the fields and their new values 
by using the SET keyword. Lastly a WHERE clause indicates the record(s) to update.

*/

UPDATE employees
SET job_title = 'Backend Engineer', salary = 15000
WHERE id = 251;


---------------------------- //
-- Assignment -- Practice --
---------------------------- //

/*
We need to update Lane's record in our user table, he founded CashPal but he's not even recognized as an admin!

UPDATE Lane's record within the users table so that the is_admin field is set to true!

Here is the current state of the USERS table for reference!

*/