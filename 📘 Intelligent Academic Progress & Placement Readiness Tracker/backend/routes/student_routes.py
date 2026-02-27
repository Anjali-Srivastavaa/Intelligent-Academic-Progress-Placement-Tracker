from flask import request, jsonify
from database import cursor, db

def student_routes(app):

    @app.route("/students", methods=["POST"])
    def create_student():
        data = request.json

        query = """
        INSERT INTO Students(name, branch, semester, cgpa)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(query, (
            data["name"],
            data["branch"],
            data["semester"],
            data["cgpa"]
        ))

        db.commit()
        return jsonify({"message": "Student added", "id": cursor.lastrowid}), 201

    @app.route("/students/<int:student_id>", methods=["GET"])
    def get_student(student_id):
        cursor.execute("SELECT * FROM Students WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        if student:
            return jsonify(student)
        return jsonify({"message": "Student not found"}), 404

    @app.route("/skills", methods=["POST"])
    def add_skill():
        data = request.json
        # Add skill to master Skills table
        query = "INSERT INTO Skills (skill_name, category) VALUES (%s, %s)"
        cursor.execute(query, (data["skill_name"], data.get("category", "General")))
        db.commit()
        return jsonify({"message": "Skill added", "skill_id": cursor.lastrowid}), 201

    @app.route("/student_skills", methods=["POST"])
    def add_student_skill():
        data = request.json
        # Associate skill with student
        query = "INSERT INTO Student_Skills (student_id, skill_id, level) VALUES (%s, %s, %s)"
        cursor.execute(query, (data["student_id"], data["skill_id"], data.get("level", "Beginner")))
        db.commit()
        return jsonify({"message": "Student skill added"}), 201
