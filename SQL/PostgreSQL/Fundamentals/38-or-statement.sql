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

-- You can group logical operations with parentheses to specify the order of operations

(this AND that) OR the_other


----------------------------- //
-- Assignment -- Practice
----------------------------- //

/*
The laws have changed again! Now we need to see how many affected users meet this criteria:

 >>-->> Users who are from the United States or Canada, and are under 18

Write a query that retrieves the count of every user that matches the conditions above.
*/

SELECT count(*)
FROM users
WHERE (country_code = ('US') OR country_code = ('CA'))
    AND age < 18;