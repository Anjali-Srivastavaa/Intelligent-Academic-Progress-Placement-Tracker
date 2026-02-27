# 📘 Intelligent Academic Progress & Placement Readiness Tracker

---

## 📌 Project Overview

The Intelligent Academic Progress & Placement Readiness Tracker is a database-driven web application designed to monitor student academic performance, track skill development, and evaluate placement readiness using analytics-based insights.

The system acts as a mini placement analytics platform used by academic institutions to identify skill gaps and measure student preparedness for job placements.

---

## 🎯 Project Objectives

The application performs the following tasks:

* Store student academic records
* Track skills and certifications
* Calculate placement readiness score
* Identify missing skills required for placement
* Display analytics dashboard with performance insights

---

## 🧱 Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)

### Backend

* Python Flask (REST API)

### Database

* MySQL

### Development Tools

* VS Code
* Git & GitHub
* Postman (API Testing)

---

## 🏗️ System Architecture

```
User Interface (Frontend)
          ↓
Flask REST API (Backend)
          ↓
MySQL Database
          ↓
Analytics Engine (SQL + Business Logic)
```

---

## 📂 Project Folder Structure

```
placement-tracker/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models/
│   │     ├── student.py
│   │     └── skill.py
│   └── routes/
│         ├── student_routes.py
│         └── analytics_routes.py
│
├── frontend/
│   ├── index.html
│   ├── dashboard.js
│   └── styles.css
│
├── database/
│   └── schema.sql
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Step-by-Step Installation Guide

### Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/placement-tracker.git
cd placement-tracker
```

---

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

Create `requirements.txt`

```
Flask
flask-cors
mysql-connector-python
```

Install:

```bash
pip install -r requirements.txt
```

---

### Step 4 — Setup MySQL Database

Login to MySQL:

```sql
CREATE DATABASE placement_tracker;
USE placement_tracker;
```

---

### Step 5 — Database Schema

Create file:

```
database/schema.sql
```

Copy-paste:

```sql
CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50),
    semester INT,
    cgpa FLOAT
);

CREATE TABLE Skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE Student_Skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    skill_id INT,
    level VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);

CREATE TABLE Placement_Criteria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    min_cgpa FLOAT,
    required_skills TEXT
);
```

Run:

```sql
SOURCE database/schema.sql;
```

---

### Step 6 — Backend Setup

Create:

```
backend/app.py
```

#### Basic Flask Server

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Placement Tracker API Running"}

if __name__ == "__main__":
    app.run(debug=True)
```

Run server:

```bash
python backend/app.py
```

Open:

```
http://127.0.0.1:5000
```

---

### Step 7 — Database Connection

Create:

```
backend/database.py
```

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="placement_tracker"
)

cursor = db.cursor(dictionary=True)
```

---

### Step 8 — Student API

Create:

```
backend/routes/student_routes.py
```

```python
from flask import request, jsonify
from database import cursor, db

def add_student(app):

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
        return jsonify({"message": "Student added"})
```

Import inside `app.py`.

---

### Step 9 — Placement Readiness Logic ⭐

Create:

```
backend/routes/analytics_routes.py
```

```python
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
        cgpa = student["cgpa"]

        cursor.execute(
            "SELECT COUNT(*) as skills FROM Student_Skills WHERE student_id=%s",
            (student_id,)
        )

        skills = cursor.fetchone()["skills"]

        score = cgpa * 10 + skills * 5

        return jsonify({
            "placement_score": score
        })
```

---

### Step 10 — Frontend Dashboard

Create:

```
frontend/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
  <title>Placement Dashboard</title>
</head>
<body>

<h2>Placement Readiness</h2>
<button onclick="loadScore()">Check Score</button>

<p id="result"></p>

<script src="dashboard.js"></script>

</body>
</html>
```

#### dashboard.js

```javascript
async function loadScore() {
  const res = await fetch(
    "http://127.0.0.1:5000/analytics/readiness/1"
  );

  const data = await res.json();
  document.getElementById("result").innerText =
      "Score: " + data.placement_score;
}
```

---

## 📊 Core Features

✅ Student profile management
✅ Academic tracking
✅ Skill monitoring
✅ Placement readiness analytics
✅ Skill gap identification
✅ Dashboard visualization

---

## 🚀 API Endpoints

| Method | Endpoint                  | Description     |
| ------ | ------------------------- | --------------- |
| POST   | /students                 | Add student     |
| GET    | /analytics/readiness/{id} | Placement score |

---

## 🔮 Future Enhancements

* AI-based placement prediction
* Resume analyzer
* Company eligibility filtering
* ML recommendation engine
