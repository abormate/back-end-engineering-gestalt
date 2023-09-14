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