// Wait for the DOM to be fully loaded before running any code
document.addEventListener("DOMContentLoaded", function () {
    // Call the fetch_courses function to initially populate the course list
    fetch_courses();
});

// Event listener for the form submission to create a new course
document.getElementById('create-course-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the input values from the form
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    // Create a data object with the input values
    const data = {
        title: title,
        description: description,
    };

    // Send a POST request to create a new course
    fetch('/course', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to create course');
        }
    })
    .then(data => {
        // Reset the form and show an alert message
        document.getElementById('create-course-form').reset();
        alert(data.message);
        // Refresh the course list
        fetch_courses();
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Event listener for the form submission to update an existing course
document.getElementById('update-course-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the input values from the form
    const courseId = document.getElementById('update-id').value
    const new_title = document.getElementById('update-title').value;
    const new_description = document.getElementById('update-description').value;

    // Create a data object with the updated values
    const data = {
        title: new_title,
        description: new_description,
    };

    // Send a PUT request to update the course
    fetch(`/course/${courseId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to update course');
        }
    })
    .then(data => {
        // Reset the form and show an alert message
        document.getElementById('update-course-form').reset();
        alert(data.message);
        // Refresh the course list
        fetch_courses();
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Event listener for the form submission to delete an existing course
document.getElementById('delete-course-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the course ID to be deleted
    const courseId = document.getElementById('delete-id').value;

    // Send a DELETE request to delete the course
    fetch(`/delete/course/${courseId}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to delete course');
        }
    })
    .then(data => {
        // Reset the form and show an alert message
        document.getElementById('delete-course-form').reset();
        alert(data.message);
        // Refresh the course list
        fetch_courses();
    })
    .catch(error => {
        console.error(error);
    });
});

// Function to fetch and display the list of courses
function fetch_courses() {
    fetch("/courses") // Send a GET request to fetch course data
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const coursesList = document.getElementById("courses");
            coursesList.innerHTML = ''; // Clear the existing list

            // Iterate through the fetched data and create list items for each course
            data.forEach(course => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `<strong>${course.title} (${course.course_id})</strong>: ${course.description}`;
                coursesList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error("Error fetching course data:", error);
        });
};
