-- DDL (Data Definition Language)

CREATE DATABASE coding_temple;
USE coding_temple;

-- Instructors Table
CREATE TABLE instructors (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Students Table
CREATE TABLE students (
	id INT auto_increment PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    enrollment_date DATE,
    instructors_id INT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (instructors_id) REFERENCES instructors(id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Courses Table
CREATE TABLE courses (
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Courses_students table (Many-to-Many Relationship)
CREATE TABLE courses_students (
	student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	FOREIGN KEY (course_id) REFERENCES courses(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Add a new column to a table
ALTER TABLE instructors ADD office_location VARCHAR(100); -- Allan

-- Change the data type of a column
ALTER TABLE instructors MODIFY COLUMN department CHAR(50);

-- Rename a column name and/or update data type
ALTER TABLE instructors CHANGE COLUMN name instructors_name VARCHAR(50);

-- Rename a table
RENAME TABLE courses TO class_offerings;
RENAME TABLE class_offerings TO courses;

-- Drop a column (delete a column)
ALTER TABLE instructors DROP COLUMN office_location;

-- Add a foreign key to link to a table
ALTER TABLE students ADD COLUMN advisor_id INT,
	Add CONSTRAINT fk_student_advisor FOREIGN KEY (advisor_id) REFERENCES instructors(id)
		ON DELETE SET NULL
        ON UPDATE CASCADE;
        
SELECT * FROM students;