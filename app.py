from flask import Flask
from routes import views  # Assuming 'views' is the blueprint for your routes

# Create a Flask application instance
app = Flask(__name__)

# Register the 'views' blueprint for routing
app.register_blueprint(views, url_prefix="/")

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask application in debug mode disabled
    app.run(debug=False)
