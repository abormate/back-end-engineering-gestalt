---------------------------------------- //
--
-- Min -- Aggregation -- SQL StudySpace
--
---------------------------------------- //

/*
The min function works the same as the max function but finds the lowest value instead of the highest value.

*/

SELECT product_name, min(price)
from products;

-- This query returns the product_name and the price fields of the record with the lowest price.

