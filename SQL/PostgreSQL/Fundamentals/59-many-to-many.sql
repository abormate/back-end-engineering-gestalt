---------------------------------------- //
--
-- Many to Many -- SQL LearnSpace 
--
---------------------------------------- //

/*
A many-to-many relationship occurs when multiple records in one table can be related to multiple records in another table.

*/

---------------------------- //
-- Examples of Many to Many relationships
---------------------------- //

/*
-- A products table and a suppliers table - Products may have 0 to many suppliers, and suppliers can supply 0 to many products.
-- A classes table and a students table - Students can take potentially many classes and classes can have many students enrolled.

*/

---------------------------- //
-- Joining Table
---------------------------- //

/*
Joining tables help define many-to-many relationships between data in a database. As an example when defining the relationship above between products and 
suppliers, we would define a joining table called products_suppliers that contains the primary keys from the tables to be joined.

*/

