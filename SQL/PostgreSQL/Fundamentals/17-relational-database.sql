--------------------------------------- //
--
-- Relational Database -- SQL LearnSpace --
--
--------------------------------------- //

/*
We have been using the term relational quite a bit, it's time we actually go over what that means! A relational database is a 
type of database that stores data so that it can be easily related to other data. For example, a user can have many tweets. 
There's a relationship between a user and their tweet.

*/

/*
In a relational database:

1. Data is typically represented in "tables".
2. Each table has "columns" or "fields that hold attributes related to the record.
3. Each row or entry in the table is called a record.
4. Typically, each record has a unique Id called the primary key.

*/

-- Example relational database --> https://prnt.sc/CSbR7mjrBG_3

/*

Here is an example of a small relational database. This database has 3 tables, Students, Courses, and StudentCourses. 
The StudentCourses table manages the relationship between the Students and the Courses tables.

https://prnt.sc/CSbR7mjrBG_3

-- Example 1: Samantha

1. Samantha has an Id of 1
2. We can find Sam's courses by looking in the StudentCourses for the records that match his StudentId.

-- Example 2: MongoDB

1. MongoDB has an Id of 3
2. We can find all the students enrolled in the MongoDB course by checking the StudentCourses table

*/

