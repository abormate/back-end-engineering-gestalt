---------------------------------------- //
--
-- SQL Null Values
--
---------------------------------------- //

/*
In SQL a row with a NULL value represents that the value is missing. A NULL value within a row is very different than a 
zero value. When inserting records into a table, unless a constraint has been set, a record can be added with missing (NULL) 
fields.

*/

---------------------------- //
-- Constraints
---------------------------- //

/*
When creating a table we can define whether or not a field can or cannot be NULL, and that's a kind of constraint.

We will cover constraints in more detail soon, for now, let's focus on NULL values.

*/

---------------------------- //
-- Assignment -- Practice --
---------------------------- //

/*
We didn't force any constraints on our tables when we created them and it has allowed for NULL entries to make their way 
into our table! Let's take a look at our transactions table to see what those NULL values look like.

Complete the SELECT statement on the transactions table to return all columns and rows.

*/

---------------------------- //
-- Observe --
---------------------------- //

/*
Notice that both the transaction_type and was_successful fields have NULL values in all 3 records in the table. 
That's because we ran our migration in the previous exercise after the 3 records were created!

*/