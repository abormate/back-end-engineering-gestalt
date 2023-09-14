--------------------------------------- //
--
-- Round -- SQL LearnSpace
--
--------------------------------------- //

/*
Sometimes we need to round some numbers, particularly when working with the results of an aggregation. We can use the ROUND() function to get the job done.

The SQL round() function allows you to specify both the value you wish to round and the precision to which you wish to round it:

*/

round(value, precision)

-- If no precision is given, SQL will round the value to the nearest whole value:

select song_name, round(avg(song_length), 1)
from songs

