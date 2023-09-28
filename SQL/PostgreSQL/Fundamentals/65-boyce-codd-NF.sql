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

