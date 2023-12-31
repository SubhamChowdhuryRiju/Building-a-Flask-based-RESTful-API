# Topic: Building-a-Flask-based-RESTful-API

**Tech Stack:**  HTML5, Bootstrap, JavaScript, Flask, RESTful-API

# **Starting Steps:**

1.**Step 1:**  Delete the venv folder.

2.**Step 2:** Then create a new virtual environment by using the command prompt: **python -m venv venv**.

3.**Step 3:** Then install flask using the command: **pip3 install flask**.

4.**Step 4:** Then run the app.py file.


# **To Run the Application:**

1. Only Run the app.py python file.
2. Default port is 5000.
3. The database that is used is SQLite3 (integrated database of python) and the db file has also been updated.
4. Error handling for common scenarios such as course not found, invalid input, and server errors is also done.

# **Routes (Tested using Postman) :**

1. **GET /courses:** This route should return a list of available courses in JSON format.

2. **GET /course/<course_id>:** This route should return details about a specific course identified by course_id. 

3. **POST /course:** This route should allow the creation of new courses. Users should be able to submit course data (e.g., title, description) via JSON and receive a response indicating success or failure. 

4. **PUT /course/<course_id>:** This route should allow updating the details of an existing course identified by course_id. 

5. **DELETE /course/<course_id>:** This route should allow the deletion of a course identified by course_id.
