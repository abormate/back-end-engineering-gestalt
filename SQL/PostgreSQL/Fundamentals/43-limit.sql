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

