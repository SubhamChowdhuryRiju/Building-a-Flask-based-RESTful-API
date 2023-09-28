# Topic: Building-a-Flask-based-RESTful-API

Tech Stack:  HTML5, Bootstrap, JavaScript, Flask, RESTful-API

**To Run the Application:**

Only Run the app.py python file.
Default port is 5000
The database that is used is SQLite3 (integrated database of python) and the db file has also been updated.
Error handling for common scenarios such as course not found, invalid input, and server errors is also done.

**Routes (Tested using Postman) :**

GET /courses: This route should return a list of available courses in JSON format.

GET /course/<course_id>: This route should return details about a specific course identified by course_id. 

POST /course: This route should allow the creation of new courses. Users should be able to submit course data (e.g., title, description) via JSON and receive a response indicating success or failure. 

PUT /course/<course_id>: This route should allow updating the details of an existing course identified by course_id. 

DELETE /course/<course_id>: This route should allow the deletion of a course identified by course_id.
