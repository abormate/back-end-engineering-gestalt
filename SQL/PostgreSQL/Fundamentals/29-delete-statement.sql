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

/*
CURRENT STATE OF THE USERS TABLE
ID	NAME	AGE	country_code	USERNAME	PASSWORD	is_admin
1	David	34	US	DavidDev	insertPractice	0
2	Samantha	29	BR	Sammy93	addingRecords!	0
3	John	39	CA	Jjdev21	welovebootdev	0
4	Ram	42	IN	Ram11c	thisSQLcourserocks	0
5	Hunter	30	US	Hdev92	backendDev	0
6	Allan	27	US	Alires	iLoveB00tdev	1
7	Lance	20	US	LanChr	b00tdevisbest	0
8	Tiffany	28	US	Tifferoon	autoincrement	1
9	Lane	27	US	wagslane	update_me	0

*/

DELETE from users WHERE id = 2;

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

SELECT * from users;