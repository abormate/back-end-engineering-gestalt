---------------------------------------- //
--
-- 2nd Normal Form -- 2NF -- SQL LearnSpace
--
---------------------------------------- //

/*
A table in second normal form follows all the rules of 1st normal form, and one additional rule:

-- All columns that are not part of the primary key are dependent on the entire primary key, and not just one of the columns in the primary key.

*/

--------------------------- //
-- Example of 1NF, but NOT 2NF
--------------------------- //

/*
In this table, the primary key is a combination of first_name + last_name.

first_name	last_name	first_initial
Lane	    Wagner	    l
Lane	    Small	    l
Allan	    Wagner	    a


This table does not adhere to 2NF. The first_initial column is entirely dependent on the first_name column, rendering it redundant.


*/

-------------------------- //
-- Example of 2nd Normal Form
-------------------------- //

/*
One way to convert the table above to 2NF is to add a new table that maps a first_name directly to its first_initial. This removes any duplicates!

first_name	last_name
Lane	    Wagner
Lane	    Small
Allan	    Wagner


first_name	first_initial
Lane	    l
Allan   	a


*/


------------------------ //
-- 2NF is usually a good idea
------------------------ //

/*
You should probably default to keeping your tables in second normal form. That said, there are good reasons to deviate from it, particularly for performance 
reasons. The reason being that when you have query a second table to get additional data it can take a bit longer.

My rule of thumb is:

Optimize for data integrity and data de-duplication first. If you have speed issues, de-normalize accordingly.

*/


------------------------ //
-- Assignment -- Practice
------------------------ //

/*
Another developer on our team has created a joining table for the companies<->users many-to-many relationship. Unfortunately, they did it a bit... weird. 
They included meta information about companies on the joining table!

A good joining table simply has the ids of the entities in the relationship. It manages the relationship and nothing else. Any information about the entities 
themselves belongs on their respective tables.

Move the column that's out of place to its proper table. Be sure to add it as the last column to the table you add it to.

*/

CREATE TABLE users (
  id INTEGER PRIMARY KEY,ELea
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);

CREATE TABLE companies (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  num_employees INTEGER NOT NULL,
  company_revenue INTEGER
);

CREATE TABLE users_companies (
  user_id INTEGER,
  company_id INTEGER,
  UNIQUE(user_id, company_id)
);

-- Don't touch below this line --

pragma table_info('companies');
