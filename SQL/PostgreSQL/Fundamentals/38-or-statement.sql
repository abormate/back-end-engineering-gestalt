---------------------------------------- //
--
-- OR statement
--
---------------------------------------- //

/*
As you've probably guessed, if the logical AND operator is supported, the OR operator is probably supported as well.

*/

SELECT product_name, quantity, shipment_status
    FROM products
    WHERE shipment_status = 'out of stock'
    OR quantity BETWEEN 10 and 100;

/*
This query retrieves records where either the shipment_status condition OR the quantity condition are met.

*/

----------------------------- //
-- Order of Ops
----------------------------- //

