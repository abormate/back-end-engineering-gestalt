---------------------------------------- //
--
-- Finding Null Values -- SQL LearnSpace
--
---------------------------------------- //

-- You can use a WHERE clause to filter values by whether or not they're NULL

-- // Is Null
SELECT name FROM users WHERE first_name IS NULL;

-- // Is NOT Null
SELECT name FROM users WHERE first_name IS NOT NULL;