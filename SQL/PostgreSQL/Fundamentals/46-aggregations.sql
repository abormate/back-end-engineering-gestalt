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