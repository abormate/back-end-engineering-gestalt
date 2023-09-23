---------------------------------------- //
--
-- Normal Forms -- StudySpace
--
---------------------------------------- //

/*
The creator of "database normalization", Edgar F. Codd described different "normal forms" a database can adhere to. We'll talk about the most common ones.

First normal form (1NF)
Second normal form (2NF)
Third normal form (3NF)
Boyce-Codd normal form (BCNF)


*/

/*
In short, 1st normal form is the least "normalized" form, and Boyce-Codd is the most "normalized" form.

The more normalized a database, the better its data integrity, and the less duplicate data you'll have.


*/


------------------------- //
-- Primary Keys in the context of Normal Forms are different
------------------------- //

/*
In the context of database normalization, we're going to use the term "primary key" slightly differently. When we're talking about SQLite, a "primary key" 
is a single column that uniquely identifies a row.

When we're talking more generally about data normalization, the term "primary key" means the collection of columns that uniquely identify a row. That can be 
a single column, but it can actually be any number of columns. A primary key is the minimum number of columns needed to uniquely identify a row in a table.

If you think back to the many-to-many joining table product_suppliers, that table's "primary key" was actually a combination of the 2 ids, product_id and 
supplier_id:

*/

