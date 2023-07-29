----------------------------------------- //
--
-- Relational DBs and Non Relational DBs -- SQL LearnSpace
--
----------------------------------------- //

/*
The big difference between relational and non-relational databases is that non-relational databases nest their data. 
Instead of keeping records on separate tables, they store records within other records.

*/

/*
To over-simplify it, you can think of non-relational databases as giant JSON blobs. If a user can have multiple courses, 
you might just add all the courses to the user record.

*/

{
    "users": [
        {
            "id": 0,
            "name": "Elon",
            "courses": [
                {
                    "name": "Business",
                    "id": 0
                },
                {
                    "name": "Math",
                    "id": 0
                }
            ]
        }
    ]
}

/*
This often results in duplicate data within the database. That's obviously less than ideal, but it does have some benefits 
that we'll talk about later in the course.

*/

--------------------------- //
-- Diagrams -- Examples -- Explainer
--------------------------- //

-- Relational DB
-- Diagram capture --> https://prnt.sc/IkpBYPrHzK26


-- Non Relational DB
-- Diagram capture --> https://prnt.sc/sOmpxImOe-cg


--------------------------- //
-- Assignment -- Practice
--------------------------- //

