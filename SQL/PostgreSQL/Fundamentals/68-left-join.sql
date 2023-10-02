---------------------------------------- //
--
-- Left Join -- SQL LearnSpace
--
---------------------------------------- //

/*
A LEFT JOIN will return every record from table_a regardless of whether or not any of those records have a match in table_b. A left join will also return any 
matching records from table_b. Here is a Venn diagram to help visualize the effect of a LEFT JOIN.

*/

-- diagram image --> https://prnt.sc/zlJEzWPBG1kM 

/*
A small trick you can do to make writing the SQL query easier is define an alias for each table. Here's an example:

*/

SELECT e.name, d.name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;

/*
Notice the simple alias declarations e and d for employees and departments respectively.

Some developers do this to make their queries less verbose. That said, I personally hate it because single-letter variables are harder to understand the 
meaning of.

*/