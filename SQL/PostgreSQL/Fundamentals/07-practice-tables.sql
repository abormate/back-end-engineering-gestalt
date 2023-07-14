---------------------------------------- //
--
-- Create Table -- Practice
--
---------------------------------------- //

/*
In most relational databases a single table isn't enough to hold all the data we need! We usually use a table-per-entity 
that we want to store. For example, a social media application might have the following tables:

users
posts
comments
likes


Our people table we created last exercise is a good start, but we have a lot more data to store!

----------------------------- //
-- ASSIGNMENT --
----------------------------- //

We need a table that tracks the transactions between our CashPal users.

Create the transactions table with the following fields:

id - Integer
recipient_id - Integer
sender_id - Integer
note - Text
amount - Integer

*/

create table transactions (
  id integer,
  recipient_id integer,
  sender_id integer,
  note text,
  amount integer
);

-- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

pragma table_info('transactions');