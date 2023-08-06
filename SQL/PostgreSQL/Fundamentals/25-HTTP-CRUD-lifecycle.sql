---------------------------------------- //
--
-- HTTP -- CRUD -- Database Lifecycle
--
---------------------------------------- //

/*
We talked about how a "create" operation flows through a web application. Let's talk about a "read".

*/

-- visual diagram of how it works, lifecycle --> https://prnt.sc/4xO5FEFrD-d-

/*
Let's talk through an example using the CashPal app. Our product manager wants to show profile data on a 
user's settings page. Here's how we could engineer that feature request:

First, the front-end webpage loads.
The front-end sends an HTTP GET request to a /users endpoint on the back-end server.
The server receives the request.
The server uses a SELECT statement to retrieve the user's record from the users table in the database.
The server converts the row of SQL data into a JSON object and sends it back to the front-end.

*/