---------------------------------------- //
--
-- Having -- SQL StudySpace --
--
---------------------------------------- //

/*
When we need to filter the results of a GROUP BY query even further, we can use the HAVING clause. The HAVING clause specifies a search condition for a group.

The HAVING clause is similar to the WHERE clause, but it operates on groups after they've been grouped, rather than rows before they've been grouped.

*/

SELECT album_id, count(id) as count
FROM songs
GROUP BY album_id
HAVING count > 5;

/*
This query returns the album_id and count of its songs, but only for albums with more than 5 songs.

*/

--------------------------- //
-- Assignment -- Practice
--------------------------- //

/*
A new page in the CashPal app allows users to see how much money they've spent on a specific kind of transaction, and alerts them if that amount is fairly 
large. Let's write a query that returns the total amount spent by each user on lunch when that balance is greater than 20

*/