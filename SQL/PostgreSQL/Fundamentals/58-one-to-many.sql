---------------------------------------- //
--
-- One to Many -- SQL Table Relationship
--
---------------------------------------- //

/*
When talking about the relationships between tables, a one-to-many relationship is probably the most commonly used relationship.

A one-to-many relationship occurs when a single record in one table is related to potentially many records in another table.

Note that the one->many relation only goes one way, a record in the second table can not be related to multiple records in the first table!

*/

---------------------------- //
-- Examples of one to many relationships
---------------------------- //

/*
A customers table and a orders table. Each customer has 0, 1, or many orders that they've placed.
A users table and a transactions table. Each user has 0, 1, or many transactions that taken part in.

*/


---------------------------- //
-- Assignment -- Practice --
---------------------------- //

/*
It turns out that when we originally designed the CashPal database schema we assumed that users would only have a single country they lived in. 
With digital nomads becoming a thing, it turns out many users have dual citizenship.

*/
