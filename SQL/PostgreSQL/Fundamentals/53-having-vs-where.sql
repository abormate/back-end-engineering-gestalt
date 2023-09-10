---------------------------------------- //
--
-- Having vs Where -- SQL StudySpace
--
---------------------------------------- //

/*
It's fairly common for developers to get confused about the difference between the HAVING and the WHERE clauses - they're pretty similar after all.

The difference is fairly simple in actuality:

A WHERE condition is applied to all the data in a query before it's grouped by a GROUP BY clause.
A HAVING condition is only applied to the grouped rows that are returned after a GROUP BY is applied.

*/