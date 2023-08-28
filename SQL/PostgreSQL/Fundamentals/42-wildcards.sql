--------------------------------------- //
--
-- Wildcards
--
--------------------------------------- //

SELECT * from users
    WHERE name LIKE 'or_%';


SELECT * from users
    WHERE name LIKE '__ing';


----------------------------- //
-- Assignment -- Practice
----------------------------- //

/*
Which describes the values that match example 1?

*/

-- Answer --> Values that start with 'or' and are at least 3 characters in length