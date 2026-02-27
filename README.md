# Intelligent Academic Progress & Placement Readiness Tracker

## Project Overview

The Intelligent Academic Progress & Placement Readiness Tracker is a database-driven web application designed to monitor student academic performance, track skill development, and evaluate placement readiness using analytics-based insights.

The system functions as a placement analytics platform that helps academic institutions analyze student preparedness, identify skill gaps, and support data-driven placement readiness evaluation.

---

## Objectives

The application provides the following capabilities:

* Store and manage student academic records
* Track technical skills and certifications
* Calculate placement readiness scores
* Identify missing skills required for placement eligibility
* Present analytics through a simple dashboard interface

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python Flask (REST API)

### Database

* MySQL

### Development Tools

* Visual Studio Code
* Git and GitHub
* Postman (API testing)

---

## System Architecture

```
Frontend (User Interface)
        ↓
Flask REST API (Backend Server)
        ↓
MySQL Database
        ↓
Analytics Engine (Business Logic + SQL)
```

---

## Project Structure

```
placement-tracker/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models/
│   └── routes/
│       ├── student_routes.py
│       └── analytics_routes.py
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
├── progress.md
└── README.md
```

---

## Installation and Setup

### 1. Clone Repository

```
git clone https://github.com/yourusername/intelligent-academic-progress-placement-tracker.git
cd intelligent-academic-progress-placement-tracker
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment:

**Windows**

```
venv\Scripts\activate
```

**Linux/Mac**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure MySQL Database

Create database:

```sql
CREATE DATABASE placement_tracker;
USE placement_tracker;
```

Run schema file:

```sql
SOURCE database/schema.sql;
```

---

### 5. Configure Database Credentials

Update database configuration in:

```
backend/database.py
```

Example configuration:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="placement_tracker"
)
```

---

### 6. Run Backend Server

```
python backend/app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

### 7. Launch Frontend

Open the following file in a browser:

```
frontend/index.html
```

---

## Core Features

* Student profile management
* Academic performance tracking
* Skill monitoring and evaluation
* Placement readiness score calculation
* Skill gap identification
* Dashboard-based visualization

---

## API Endpoints

| Method | Endpoint                  | Description                   |
| ------ | ------------------------- | ----------------------------- |
| POST   | /students                 | Add student record            |
| GET    | /students/{id}            | Fetch student details         |
| GET    | /analytics/readiness/{id} | Calculate placement readiness |

---

## Placement Readiness Logic

The readiness score is calculated using academic and skill metrics:

```
placement_score = (cgpa * 10) + (number_of_skills * 5)
```

This scoring model provides a simplified analytical indicator of placement preparedness.

---

## Future Enhancements

* Machine learning–based placement prediction
* Resume analysis integration
* Company-specific eligibility filtering
* Recommendation system for skill improvement

---

## License

This project is licensed under the MIT License.
