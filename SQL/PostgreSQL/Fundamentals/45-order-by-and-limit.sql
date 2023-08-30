---------------------------------------- //
--
-- Order by AND Limit -- SQL LearnSpace
--
---------------------------------------- //

-- When using both ORDER BY and LIMIT, the ORDER BY clause must come first.

---------------------------- //
-- Assignment -- Practice
---------------------------- //

/*
An HR employee got into the Git repository where we store all the queries and tried to update one himself.

Fix the bug in the SQL query.

*/

-- buggy code
SELECT * FROM transactions
WHERE amount BETWEEN 10 AND 80
LIMIT 4
ORDER BY amount DESC;

-- corrected code
SELECT * FROM transactions
WHERE amount BETWEEN 10 AND 80
ORDER BY amount DESC
LIMIT 4;