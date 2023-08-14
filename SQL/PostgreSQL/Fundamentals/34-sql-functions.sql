---------------------------------------- //
--
-- SQL Functions -- SQL LearnSpace
--
---------------------------------------- //

/*
At the end of the day, SQL is a programming language, and it's one that supports functions. We can use functions and aliases to calculate new columns 
in a query. This is similar to how you might use formulas in excel.

*/

--------------------------- //
-- IIF Function
--------------------------- //

-- In SQLite, the IIF function works like a ternary. For example,

IIF(carA > carB, "Car a is bigger", "Car b is bigger")

/*
If a is greater than b, this statement evaluates to the string "Car a is bigger". Otherwise, it evaluates to "Car b is bigger".

Here's how we can use IIF() and a directive alias to add a new calculated column to our result set:

*/

SELECT quantity,
    IIF(quantity < 10, "Order more", "In Stock") AS directive
    from products

