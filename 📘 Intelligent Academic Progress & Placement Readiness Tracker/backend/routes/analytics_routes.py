from flask import jsonify
from database import cursor

def analytics_routes(app):

    @app.route("/analytics/readiness/<int:student_id>")
    def readiness(student_id):

        cursor.execute(
            "SELECT cgpa FROM Students WHERE id=%s",
            (student_id,)
        )

        student = cursor.fetchone()
        if not student:
            return jsonify({"message": "Student not found"}), 404
            
        cgpa = student["cgpa"]

        cursor.execute(
            "SELECT COUNT(*) as skills FROM Student_Skills WHERE student_id=%s",
            (student_id,)
        )

        skills = cursor.fetchone()["skills"]

        # Logic from README: score = cgpa * 10 + skills_count * 5
        score = cgpa * 10 + skills * 5

        return jsonify({
            "student_id": student_id,
            "cgpa": cgpa,
            "skills_count": skills,
            "placement_score": score
        })
