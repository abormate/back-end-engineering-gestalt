---------------------------------------- //
--
-- Migration Practice
--
---------------------------------------- //

/*
When writing migrations that are reversible, we use the terms "up" and "down" migrations. An "up" migration is simply the 
set of changes you want to make, like altering/removing/adding/editing a table in some way. A "down" migration includes 
the changes that would revert any of the "up" migration's changes.

*/

---------------------------- //
-- Assignment -- Practice --
---------------------------- //

/*
We need to add an additional column to the transactions table. We want to know whether or not the transaction was successfully 
completed between two users. We also want our database to track the type of transaction.

Our transactions table looks like this at the moment:

*/

