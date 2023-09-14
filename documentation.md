Simple CRUD Flask API Documentation 
This documentation provides an overview of a Flask-based RESTful API for managing user data. 
This API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on user records stored in the database.

Table of Contents

Standard format
Create User
Get Users
Update User
Delete User
Database Schema
Usage




Create User
URL: /api
Method: POST
Request Body: JSON object with a name field.
Response: JSON response with a success message.

Get Users
URL: /api
Method: GET
Response: JSON response containing a list of users with their IDs and names.

Update User
URL: /api/<int:user_id>
Method: PUT
Request Body: JSON object with a name field to update the user's name.
Response: JSON response with a success message.

Delete User
URL: /api/<user_id>
Method: DELETE
Response: JSON response with a success message.
Database Schema
The API uses an SQLite database named project.db to store user information. 
The database schema consists of a User table with two columns: id (primary key) and name (a string field).

Usage
To interact with the API, you can use tools like curl, Postman, or write your own Python scripts. 
Here's a basic example using curl:

Create a user:
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5000/api


Get all users:
curl http://localhost:5000/api


Update a user:
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/1

Delete a user:
curl -X DELETE http://localhost:5000/api/1
Contributing
Contributions to this project are welcome! If you would like to contribute, please follow these guidelines:

