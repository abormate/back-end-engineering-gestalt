---------------------------------------- //
--
-- HTTP and CRUD database Lifecycle
--
---------------------------------------- //

-- It's important to understand how data flows through a typical web application.
-- Image diagram jpeg --> https://prnt.sc/YOIyIJ1rkI3S

/*
The front-end processes some data from user input - maybe a form is submitted.
The front-end sends that data to the server through an HTTP request - maybe a POST.
The server makes a SQL query to it's database to create an associated record - Probably using an INSERT statement.
Once the server has processed that the database query was successful, it responds to the front-end with a status code! 

Hopefully a 200-level code (success)!

*/