import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from backend.database import cursor, db

def verify():
    try:
        cursor.execute("SELECT 1")
        print("Database connection successful.")
        
        # Check tables
        cursor.execute("SHOW TABLES")
        tables = [list(t.values())[0] for t in cursor.fetchall()]
        print(f"Tables: {tables}")
        
        if not tables:
            # Create tables
            with open("database/schema.sql", "r") as f:
                schema = f.read()
                for cmd in schema.split(';'):
                    if cmd.strip():
                        cursor.execute(cmd)
            db.commit()
            print("Schema created.")
            
        # Add sample student
        cursor.execute("SELECT COUNT(*) as count FROM Students")
        if cursor.fetchone()['count'] == 0:
            cursor.execute("INSERT INTO Students (name, branch, semester, cgpa) VALUES (%s, %s, %s, %s)", 
                          ("Test Student", "CS", 1, 9.0))
            sid = cursor.lastrowid
            
            # Master skill
            cursor.execute("INSERT INTO Skills (skill_name, category) VALUES (%s, %s)", ("Python", "Programming"))
            skid = cursor.lastrowid
            
            # Student skill
            cursor.execute("INSERT INTO Student_Skills (student_id, skill_id, level) VALUES (%s, %s, %s)", (sid, skid, "Intermediate"))
            db.commit()
            print("Sample data added.")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    verify()
