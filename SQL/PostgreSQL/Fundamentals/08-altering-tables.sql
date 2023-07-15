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

-------------------------- //
-- Assignment -- Practice --
-------------------------- //

/*
We need to make some changes to the people table! At the moment, we have these five columns (shown as rows so we can 
display datatypes):

CID	NAME	TYPE	NOTNULL	DFLT VALUE	PK
0	id	    INTEGER	0		             0
1	handle	TEXT	0		             0
2	name	TEXT	0		             0
3	age	    INTEGER	0		             0
4	balance	INTEGER	0		             0
5	is_admin	BOOLEAN	0	             0


Rename the table to users
Rename the handle column to username.
Add the password (TEXT) column.

*/

alter table people
rename to users;

alter table users
rename column handle to username;

alter table users
add column password TEXT;

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

pragma table_info('users');