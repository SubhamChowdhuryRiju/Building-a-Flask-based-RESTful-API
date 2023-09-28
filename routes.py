from flask import Flask, render_template, jsonify, request, Blueprint
import sqlite3

# Create a Flask Blueprint named 'views'
views = Blueprint(__name__, "/")

# Initialize a global variable to store the CourseId
CourseId = 0

# Function to convert query result into a list of dictionaries
def fetch_database(result):
    course_list = [{'course_id': item[1], 'title': item[2], 'description': item[3]} for item in result]
    return course_list

# Function to create a connection to the SQLite database
def create_connection():
    try:
        con = sqlite3.connect("course_data.db")
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id TEXT,
                title TEXT,
                description TEXT
            )
        ''')
        return con
    except sqlite3.Error as e:
        print("SQLite Error:", e)
        return None

# Route to the index page
@views.route("/")
def index():
    global CourseId 
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM courses ORDER BY id DESC LIMIT 1")
    result = cursor.fetchall()
    if result:
        course_list = fetch_database(result)
        c_id = int(course_list[0]['course_id'][1:])
        CourseId = c_id
    return render_template("index.html")

# Route to fetch all courses
@views.route("/courses")
def courses():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM courses")
    result = cursor.fetchall()
    course_list = fetch_database(result)
    cursor.close()
    con.close()
    return jsonify(course_list)

# Route to get a specific course by course_id
@views.route("/course/<course_id>", methods=['GET'])
def get_specific_course(course_id):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    if result:
        course_list = fetch_database(result)
        return jsonify(course_list)
    return jsonify({'message': 'Error: Course not found'})

# Route to add a new course
@views.route("/course", methods=["POST"])
def add_new_course():
    global CourseId
    if CourseId == 0:
        CourseId = 99

    data = request.json
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM courses")
    result = cursor.fetchall()
    course_list = fetch_database(result)
    for course_data in course_list:
        if course_data['title'] == data.get('title', ''):
            return jsonify({'message': 'Error: Course with the same title already exists'})

    CourseId = CourseId + 1
    cursor.execute("INSERT INTO courses (course_id, title, description) VALUES (?, ?, ?)",
               (f"C{CourseId}", data.get("title", ""), data.get("description", ""),))
    con.commit()
    cursor.close()
    con.close()

    return jsonify({'message': 'Course created successfully'})

# Route to update an existing course
@views.route("/course/<course_id>", methods=["PUT"])
def update_course(course_id):
    update_data = request.json
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("UPDATE courses SET title=?, description=? WHERE course_id = ?", 
                   (update_data.get("title", ""), update_data.get("description", ""), course_id,))
    rows_updated = cursor.rowcount
    con.commit()
    cursor.close()
    con.close()
    if rows_updated == 0:
        return jsonify({'message': 'Error: Course not found'})
    
    return jsonify({'message': 'Course updated successfully'})

# Route to delete a course
@views.route('/delete/course/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = ?", (course_id,))
    rows_deleted = cursor.rowcount
    con.commit()
    cursor.close()
    con.close()
    if rows_deleted == 0:
        return jsonify({'message': 'Error: Course not found'})
    return jsonify({'message': f'{course_id} deleted'})
