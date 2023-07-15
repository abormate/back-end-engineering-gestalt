---------------------------------------- //
--
-- Making Changes on a Database without Deletion
--
---------------------------------------- //

/*
We often need to alter our database schema without deleting it and re-creating it. Imagine if Twitter deleted its database 
each time it needed to add a feature, that would be a disaster! Your account and all your tweets would be wiped out daily.

Instead, we can use use the ALTER TABLE statement to make changes in place without deleting any data.

*/

-- With SQLite an ALTER TABE statement allows you to:

--------------------------- //
-- Rename a Table or Column
--------------------------- //

ALTER TABLE employees
RENAME TO contractors;

ALTER TABLE contractors
RENAME COLUMN salary TO invoice;

-------------------------- //
-- Add or Drop a Column
-------------------------- //

ALTER TABLE contractors
ADD COLUMN job_title TEXT;

ALTER TABLE contractors
DROP COLUMN is_manager;