---------------------------------------- //
--
-- Between -- SQL LearnSpace
--
---------------------------------------- //

/*
We can check if values are between two numbers using the WHERE clause in an intuitive way! The WHERE clause doesn't always have to be used to 
specify specific id's or values. We can also use it to help narrow down our result set. Here's an example:

*/

SELECT employee_name, salary
FROM employees
WHERE salary BETWEEN 30000 and 60000;

/*
This query returns all the employees name and salary fields for any rows where the salary is BETWEEN 30,000 and 60,000! We can also query results that 
are NOT BETWEEN two specified values.

*/

SELECT product_name, quantity
FROM products
WHERE quantity NOT BETWEEN 20 and 100;

