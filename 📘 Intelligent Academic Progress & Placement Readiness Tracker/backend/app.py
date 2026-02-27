from flask import Flask, jsonify
from flask_cors import CORS
from routes.student_routes import student_routes
from routes.analytics_routes import analytics_routes

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Placement Tracker API Running"}

# Initialize routes
student_routes(app)
analytics_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
