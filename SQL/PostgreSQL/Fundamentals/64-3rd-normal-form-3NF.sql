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

------------------------- //
-- 3NF is usually a good idea
------------------------ //

/*
The same exact rule of thumb applies to the second and third normal forms.

!important! --> Optimize for data integrity and data de-duplication first by adhering to 3NF. If you have speed issues, de-normalize accordingly.

*/

------------------------- //
-- Assignment -- Practice
------------------------- //

/*
This rollout of business accounts is really causing some headaches for our development team. The companies table has been a disaster. Our database architect 
pointed out that the idea behind the size field is redundant.

If a company has more than 100 employees, we consider it "large", otherwise we consider its size "small".

Remove the size column from the companies table and alter the SELECT statement to calculate a size field in the result set that works the same way. 
Return the other fields as normal.

*/