--------------------------------------- //
--
-- Dangers of Deleting Data
--
--------------------------------------- //

/*
Deleting data can be a dangerous operation. Once removed, data can be really hard if not impossible to restore! 
Let's talk about a couple of common ways back-end engineers protect against losing valuable customer data.

STRATEGY 1 - BACKUPS
If you're using a cloud-service like GCP's Cloud SQL or AWS's RDS you should always turn on automated backups. 
They take an automatic snapshot of your entire database on some interval, and keep it around for some length 
of time.

For example, the Boot.dev database has a backup snapshot taken daily and we retain those backups for 30 days. 
If I ever accidentally run a query that deletes valuable data, I can restore it from the backup.

You should have a backup strategy for production databases.



STRATEGY 2 - SOFT DELETES
A "soft delete" is when you don't actually delete data from your database, but instead just "mark" the data as 
deleted. For example, you might set a deleted_at date on the row you want to delete. Then, in your queries you 
ignore anything that has a deleted_at date set. The idea is that this allows your application to behave as if 
it's deleting data, but you can always go back and restore any data that's been removed.

You should probably only soft-delete if you have a specific reason to do so. Automated backups should be 
"good enough" for most applications that are just interested in protecting against developer mistakes.


*/

---------------------------- //
-- Assignment -- Practice
---------------------------- //

/*
You should ___________ have automated backups being taken of a production database.

*/

-- Answer --> Almost always



/*
A soft-delete is where you ____

*/


/*
Answer --

Mark a row as deleted instead of actually removing the data

*/