---------------------------------------- //
--
-- NameSpacing -- SQL LearnSpace
--
---------------------------------------- //

/*
When working with multiple tables, you can specify which table a field exists on using a dot (.) For example:

*/

table_name.column_name

SELECT students.name, classes.name
FROM students
INNER JOIN classes on classes.class_id = students.class_id;

-- The above query returns the name field from the students table and the name field from the classes table.

-------------------------- //
-- Assignment -- Practice
-------------------------- //

/*
Adjust the query to:

Return the name, and age fields from the users table.
Return the name field from the countries table and rename it to country_name.
Sort by the country_name in ascending order.

*/