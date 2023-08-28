---------------------------------------- //
--
-- Limit break -- LearnSpace
--
---------------------------------------- //

/*
Sometimes we don't want to retrieve every record from a table. For example, it's common for a production database table to have millions of rows, 
and SELECTing all of them might crash your system! The LIMIT keyword has entered the chat.

*/

-- The LIMIT keyword can be used at the end of a select statement to reduce the number of records returned.

SELECT * FROM products
    WHERE product_name LIKE '%berry%'
    LIMIT 50;

/*
The query above retrieves all the records from the products table where the name contains the word berry. If we ran this query on the Facebook database, 
it would almost certainly return a lot of records.

*/

/*
The LIMIT statement only allows the database to return up to 50 records matching the query. This means that if there aren't that many records matching 
the query, the LIMIT statement will not have an effect.

*/

---------------------------- //
-- Assignment -- Practice
---------------------------- //

