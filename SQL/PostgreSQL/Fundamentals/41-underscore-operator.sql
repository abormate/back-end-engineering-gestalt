--------------------------------------- //
--
-- Underscore Operator
--
--------------------------------------- //

/*
As discussed, the % wildcard operator matches zero or more characters. Meanwhile, the _ wildcard operator only matches a single character.

*/

SELECT * FROM products
    WHERE product_name LIKE '_oot';