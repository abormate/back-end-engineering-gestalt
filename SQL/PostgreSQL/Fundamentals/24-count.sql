--------------------------------------- //
--
-- Count -- SQL LearnSpace
--
--------------------------------------- //

/*
We can use a SELECT statement to get a count of the records within a table. This can be very useful when we 
need to know how many records there are, but we don't particularly care what's in them.

*/

SELECT count(*) from employees;

/*
Mechanics -- 

The * in this case refers to a column name. We don't care about the count of a specific column - we want to 
know the number of total records so we can use the wildcard (*).

*/