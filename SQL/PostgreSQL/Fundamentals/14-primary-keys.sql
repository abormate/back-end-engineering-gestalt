----------------------------------------- //
--
-- Primary Keys -- SQL learnspace
--
----------------------------------------- //

/*
A key defines and protects relationships between tables. A primary key is a special column that uniquely identifies records 
within a table. Each table can have one, and only one primary key.

*/

----------------------------- //
-- More into Primary Keys 
----------------------------- //

/*
It's very common to have a column named id on each table in a database, and that id is the primary key for that table. No two 
rows in that table can share an id.

A PRIMARY KEY constraint can be explicitly specified on a column to ensure uniqueness, rejecting any inserts where you attempt 
to create a duplicate ID.

*/

------------------------------ //
-- Assignment -- Practice
------------------------------ //

/*
Run the code. Notice that there's a bug - there is a violation of a PRIMARY KEY constraint on the id column. Fix the data that's 
being inserted.

When working with integer ids, it's best practice to increment the id by 1 for each successive insert. Follow this convention 
when fixing the bug.

*/

INSERT into users (
    id,
    name,
    age,
    username,
    password,
    is_admin
) values (
    0,
    "Rudolf",
    33,
    "rudolf1234",
    "thisisnotsecure",
    false
);

INSERT into users (
    id,
    name,
    age,
    username,
    password,
    is_admin
) values (
    1, --fixed id value
    "Jerry",
    25,
    "jerrysmith",
    "mypasswordis1234",
    true
);

select * from users;

