---------------------------------------- //
--
-- Average
--
---------------------------------------- //

/*
Just like we may want to find the minimum or maximum values within a dataset, sometimes we need to know the average!

SQL offers us the AVG() function. Similar to MAX(), AVG() calculates the average of all non-NULL values.

*/

select song_name, avg(song_length)
from songs

-- This query returns the average song_length in the songs table!