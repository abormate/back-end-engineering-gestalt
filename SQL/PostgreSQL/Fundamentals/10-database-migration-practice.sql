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

/*
CID	NAME	         TYPE	NOTNULL	DFLT VALUE	PK
0	id	             INTEGER	0		        0
1	recipient_id	 INTEGER	0		        0
2	sender_id	     INTEGER	0		        0
3	note	         TEXT	    0		        0
4	amount	         INTEGER	0		        0

*/

/*
Complete the following up migration:

Add the boolean was_successful column to the transactions table.
Add the TEXT transaction_type column to the transactions table.

*/

ALTER TABLE transactions
ADD COLUMN was_successful boolean;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT; 

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

pragma table_info('transactions');