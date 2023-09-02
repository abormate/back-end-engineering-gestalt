---------------------------------------- //
--
-- SUM -- SQL LearnSpace 
--
---------------------------------------- //

/*
The sum aggregation function returns the sum of a set of values.

For example, the query below returns a single record containing a single field. The returned value is equal to the total salary being collected by all of the 
employees in the employees table.

*/

SELECT sum(salary)
FROM employees;

