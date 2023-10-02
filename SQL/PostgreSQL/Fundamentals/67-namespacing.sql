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