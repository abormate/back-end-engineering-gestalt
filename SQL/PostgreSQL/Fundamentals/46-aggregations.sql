---------------------------------------- //
--
-- Aggregations -- SQL LearnSpace
--
---------------------------------------- //

/*
An "aggregation" is a single value that's derived by combining several other values. We performed an aggregation earlier when we used the count statement 
to count the number of records in a table.


*/

--------------------------- //
-- Why Aggregations
--------------------------- //

/*
Data stored in a database should generally be stored raw. When we need to calculate some additional data from the raw data, we can use an aggregation.

Take the following count aggregation as an example:

*/


SELECT COUNT(*)
FROM products
WHERE quantity = 0;

/*
This query returns the number of products that have a quantity of 0. We could store a count of the products in a separate database table, and 
increment/decrement it whenever we make changes to the products table - but that would be redundant.

It's much simpler to store the products in a single place (we call this a single source of truth) and run an aggregation when we need to derive 
additional information from the raw data.

*/

------------------------- //
-- Assignment -- Practice
------------------------- //

/*
The front-end team is building a dashboard page in CashPal. We need to be able to provide them the number of successful transactions for a given user.

Return the number of transactions where the user_id is 7, and was_successful is true.

*/

SELECT COUNT(*) FROM transactions WHERE user_id IS 7 AND was_successful is TRUE;