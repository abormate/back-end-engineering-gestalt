---------------------------------------- //
--
-- Finding Null Values -- SQL LearnSpace
--
---------------------------------------- //

-- You can use a WHERE clause to filter values by whether or not they're NULL

-- // Is Null
SELECT name FROM users WHERE first_name IS NULL;

-- // Is NOT Null
SELECT name FROM users WHERE first_name IS NOT NULL;

--------------------------- //
-- Assignment -- Practice
--------------------------- //

/*
The way we store transactions at CashPal is interesting. We store a user_id field on the transactions table. 
That user is the "owner" of the transaction, and a user_id is never null.

Whenever the owner of the transaction receives money, the sender_id will not be null - it will be the user id 
of the sender. The recipient_id will be null.

Whenever the owner of the transaction sends money, the recipient_id will not be null - it will be the user id 
of the recipient. The sender_id will be null.

Select all the rows from the transactions table where the owner of the transactions is receiving money.

*/

SELECT * FROM transactions WHERE recipient_id is NULL;