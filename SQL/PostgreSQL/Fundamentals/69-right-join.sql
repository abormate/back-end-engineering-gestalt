---------------------------------------- //
--
-- Right Join -- SQL LearnSpace
--
---------------------------------------- //

/*
A RIGHT JOIN is, as you may expect, the opposite of a LEFT JOIN. It returns all records from table_b regardless of matches, and all matching records 
between the two tables.

*/

-- image diagram  --> https://prnt.sc/rfVa6rxSFcRX

/*
SQLite does not support right joins, but many dialects of SQL do! If you think about it, a RIGHT JOIN is just a LEFT JOIN with the order of the tables 
switched, so it's not a big deal that SQLite doesn't support the syntax.

*/

----------------------------- //
-- Assignment -- Practice
----------------------------- //

/*
We can retrieve the same records with a RIGHT JOIN and a LEFT JOIN by...

*/

-- ANSWER 
/*
Flipping the position of the tables in the join statement 

*/