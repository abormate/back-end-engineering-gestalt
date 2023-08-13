--------------------------------------- //
--
-- As Clause in SQL
--
--------------------------------------- //

/*
Sometimes we need to structure the data we return from our queries in a specific way. An AS clause allows 
us to "alias" a piece of data in our query. The alias only exists for the duration of the query.

*/

---------------------------- //
-- As Keyword
---------------------------- //

-- The following queries return the same data:

SELECT employee_id AS id, employee_name AS name
FROM employees;

SELECT employee_id, employee_name
FROM employees;

/*
The difference is that the results from the aliased query would have column names id and name instead of employee_id and employee_name.

*/

-------------------------- //
-- Assignment -- Practice
-------------------------- //

