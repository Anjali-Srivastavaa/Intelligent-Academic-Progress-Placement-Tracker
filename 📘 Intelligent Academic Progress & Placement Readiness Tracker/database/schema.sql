-- Database Schema
CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50),
    semester INT,
    cgpa FLOAT
);

CREATE TABLE IF NOT EXISTS Skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Student_Skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    skill_id INT,
    level VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);

CREATE TABLE IF NOT EXISTS Placement_Criteria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    min_cgpa FLOAT,
    required_skills TEXT
);

-- Sample Data
INSERT INTO Students (name, branch, semester, cgpa) VALUES ('John Doe', 'Computer Science', 6, 8.5) ON DUPLICATE KEY UPDATE name=name;
INSERT INTO Skills (skill_name, category) VALUES ('Python', 'Programming') ON DUPLICATE KEY UPDATE skill_name=skill_name;
INSERT INTO Student_Skills (student_id, skill_id, level) VALUES (1, 1, 'Intermediate') ON DUPLICATE KEY UPDATE level=level;
