---------------------------------------- //
--
-- In Statement -- SQL LearnSpace
--
---------------------------------------- //

/*
Another variation to the WHERE clause we can utilize is the IN operator. IN returns true or false if the first operand matches any of the values in the 
second operand. The IN operator is a shorthand for multiple OR conditions.

These two queries are equivalent:

*/

SELECT product_name, shipment_status
    FROM products
    WHERE shipment_status IN ('shipped', 'preparing', 'out of stock');

SELECT product_name, shipment_status
    FROM products
    WHERE shipment_status = 'shipped'
        OR shipment_status = 'preparing'
        OR shipment_status = 'out of stock';