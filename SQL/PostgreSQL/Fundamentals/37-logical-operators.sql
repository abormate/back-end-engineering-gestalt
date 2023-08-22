--------------------------------------- //
--
-- Logical Operators -- AND
--
--------------------------------------- //

/*
We often need to use multiple conditions to retrieve the exact information we want. We can begin to structure much more complex queries by using 
multiple conditions together to narrow down the search results of our query.

The logical AND operator can be used to narrow down our result sets even more!

*/

-------------------------- //
-- AND operator
-------------------------- //

SELECT product_name, quantity, shipment_status
    FROM products
    WHERE shipment_status = 'pending'
    AND quantity BETWEEN 0 and 10;

/*
This only retrieves records where both the shipment_status is "pending" AND the quantity is between 0 and 10

*/

------------------------- //
-- Equality and inequality operators
------------------------- //

/*
All of the following operators are supported in SQL. The = is the main one to watch out for, it's not == like in many other languages!

=
<
>
<=
>=

*/
