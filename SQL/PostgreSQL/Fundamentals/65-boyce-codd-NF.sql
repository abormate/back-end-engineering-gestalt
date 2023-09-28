----------------------------------------- //
--
-- Boyce-Codd Normal Form -- Highest NF -- backend SQL LearnSpace
--
----------------------------------------- //

/*
A table in Boyce-Codd normal form (created by Raymond F Boyce and Edgar F Codd) follows all the rules of 3rd normal form, plus one additional rule:

A column that's part of a primary key can not be entirely dependent on a column that's not part of that primary key.
This only comes into play when there are multiple possible primary key combinations that overlap. Another name for this is "overlapping candidate keys".

Only in rare cases does a table in third normal form not meet the requirements of Boyce-Codd normal form!

*/

---------------------------- //
-- Example of 3rd NF -- but NOT Boyce-Codd NF
---------------------------- //

/*
release_year	release_date	sales	name
2001	        2001-01-02	    100	    Kiss me tender
2001	        2001-02-04	    200	    Bloody Mary
2002	        2002-04-14	    100	    I wanna be them
2002	        2002-06-24	    200	    He got me

The interesting thing here is that there are 3 possible primary keys:

-- release_year + sales
-- release_date + sales
-- name

This means that by definition this table is in 2nd and 3rd normal form because those forms only restrict how dependent a column that is not part of a 
primary key can be.

This table is not in Boyce-Codd's normal form because release_year is entirely dependent on release_date.

*/