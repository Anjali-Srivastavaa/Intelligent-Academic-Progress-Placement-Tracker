import sys
import os

# Add the current directory to sys.path to find the backend package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import cursor, db

def verify_and_seed():
    try:
        # Check if tables exist
        cursor.execute("SHOW TABLES")
        tables = [list(t.values())[0] for t in cursor.fetchall()]
        print(f"Existing tables: {tables}")

        if not tables:
            print("Tables do not exist. Running schema.sql...")
            with open("database/schema.sql", "r") as f:
                schema = f.read()
                # Split schema into individual commands
                commands = schema.split(';')
                for command in commands:
                    if command.strip():
                        cursor.execute(command)
            db.commit()
            print("Schema executed successfully.")

        # Seed sample data if empty
        cursor.execute("SELECT COUNT(*) as count FROM Students")
        if cursor.fetchone()["count"] == 0:
            print("Seeding sample data...")
            # Add student
            cursor.execute("INSERT INTO Students (name, branch, semester, cgpa) VALUES (%s, %s, %s, %s)", 
                          ("John Doe", "Computer Science", 6, 8.5))
            student_id = cursor.lastrowid
            
            # Add some skills to the master Skills table
            skills = [("Python", "Programming"), ("Flask", "Web"), ("MySQL", "Database")]
            for skill_name, category in skills:
                cursor.execute("INSERT INTO Skills (skill_name, category) VALUES (%s, %s)", (skill_name, category))
                skill_id = cursor.lastrowid
                # Link skill to student
                cursor.execute("INSERT INTO Student_Skills (student_id, skill_id, level) VALUES (%s, %s, %s)", 
                              (student_id, skill_id, "Intermediate"))
            
            db.commit()
            print("Sample data seeded successfully.")
        else:
            print("Data already exists. Skipping seed.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    verify_and_seed()
