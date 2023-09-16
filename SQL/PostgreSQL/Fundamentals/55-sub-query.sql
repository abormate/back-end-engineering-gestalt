--------------------------------------- //
--
-- Sub Queries -- SQL LearnSpace
--
--------------------------------------- //

/*
Sometimes a single query is not enough to retrieve the specific records we need.

It is possible to run a query on the result set of another query - a query within a query! This is called "query-ception"... erm... I mean a "subquery".

Subqueries can be very useful in a number of situations when trying to retrieve specific data that wouldn't be accessible by simply querying a single table.

*/

--------------------------- //
-- Retrieving data from Multiple Tables
--------------------------- //

-- Here is an example of a subquery:

SELECT id, song_name, artist_id
FROM songs
WHERE artist_id IN (
    SELECT id
    FROM artists
    WHERE artist_name LIKE 'Rick%'
);

/*
In this hypothetical database, the query above selects all of the song_ids, song_names, and artist_ids from the songs table that are written by artists 
whose name starts with "Rick". Notice that the subquery allows us to use information from a different table - in this case the artists table.

*/

--------------------------- //
-- Subquery Syntax
--------------------------- //

/*
The only syntax unique to a subquery is the parentheses surrounding the nested query. The IN operator could be different, for example, we could use 
the = operator if we expect a single value to be returned.

*/

--------------------------- //
-- Assignment -- Practice
--------------------------- //

/*
One of CashPal's customer service representatives needs us to pull all the transactions for a specific user. Trouble is, they only know the user's name, 
not their id.


Use a subquery to get all of "David"s transactions.

TRANSACTIONS TABLE SCHEMA
id	user_id	recipient_id	sender_id	note	amount	was_successful


USERS TABLE SCHEMA
id	name	age	country_code	username	password	is_admin

*/

SELECT *
FROM transactions
WHERE user_id IN (
  SELECT id
  FROM users
  WHERE name LIKE 'David%'
);
