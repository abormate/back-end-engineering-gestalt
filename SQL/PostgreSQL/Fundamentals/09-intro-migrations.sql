--------------------------------------- //
--
-- Intro to Migrations
--
--------------------------------------- //

/*
A database migration is a set of changes to a relational database. In fact, the ALTER TABLE statements we did in the last 
exercise were examples of migrations!

Migrations are helpful when transitioning from the one state to another, fixing mistakes, or adapting a database to changes.

Good migrations are small, incremental and ideally reversible changes to a database. As you can imagine, when working with 
large databases, making changes can be a scary! We have to be careful when writing database migrations so that we don't break any systems that depend on the database schema.

*/

-------------------------- //
-- Example of Bad Migration
-------------------------- //

/*
EXAMPLE OF A BAD MIGRATION
If the CashPal backend connects to the production database, and runs a query like:


*/

SELECT * FROM people;

/*
And we run a database migration that alters the table name to users without updating the code, then the application will break! It will try to grab user data from a table that no longer exists.

A simple solution to this problem would be to deploy new code that uses a new query:

*/

SELECT * FROM users;

/*
And we would deploy that code to production immediately following the migration.

*/