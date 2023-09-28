---------------------------------------- //
--
-- 3rd Normal Form -- SQL LearnSpace
--
---------------------------------------- //

/*
A table in 3rd normal form follows all the rules of 2nd normal form, and one additional rule:

All columns that aren't part of the primary are dependent solely on the primary key.

Notice that this is only slightly different from second normal form. In second normal form we can't have a column completely dependent on a part of the 
primary key, and in third normal form we can't have a column that is entirely dependent on anything that isn't the entire primary key.

*/

------------------------- //
-- Example of 2NF -- but not 3NF
------------------------- //

/*
In this table, the primary key is simply the id column.

id	name	first_initial	email
1	Lane	l	            lane.works@example.com
2	Breanna	b	            breanna@example.com
3	Lane	l	            lane.right@example.com

This table is in 2nd normal form because first_initial is not dependent on a part of the primary key. However, because it is dependent on the name column 
it doesn't adhere to 3rd normal form.

*/

