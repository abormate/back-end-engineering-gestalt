---------------------------------------- //
--
-- Min -- Aggregation -- SQL StudySpace
--
---------------------------------------- //

/*
The min function works the same as the max function but finds the lowest value instead of the highest value.

*/

SELECT product_name, min(price)
from products;

-- This query returns the product_name and the price fields of the record with the lowest price.


-------------------------- //
-- Assignment -- Practice 
-------------------------- //

/*
Use a min aggregation to find the age of our youngest CashPal user in the United States in the users table.

USERS TABLE
| id | name | age | country_code | username | password | is_admin |


The country_code of the United States is US.

*/

SELECT min(age) FROM users WHERE country_code is 'US';