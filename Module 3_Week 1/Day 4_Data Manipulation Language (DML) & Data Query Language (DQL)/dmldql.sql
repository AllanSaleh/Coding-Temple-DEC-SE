-- DML (Data Manipulation Language)
-- CRUD (Create, Read, Update, Delete)

-- Insert Instructors
INSERT INTO instructors (instructors_name, department) VALUES
	("John Doe", "Computer Science"),
    ("Jane Smith", "Data Science"),
	('Mark Taylor', 'Web Development'),
    ('Emily Davis', 'Mobile Development'),
    ('Laura Brown', 'Cybersecurity');
    
-- Insert Students
INSERT INTO students (name, enrollment_date, instructors_id) VALUES
	('Alice Johnson', "2023-09-10", 1),
	('Bob Carter', '2023-09-10', 2),
    ('Charlie Miller', '2023-09-15', 3),
    ('Diana Lee', '2023-09-20', 4),
    ('Evan White', '2023-09-25', NULL);
    
-- Insert Courses
INSERT INTO courses (title, credits) VALUES
	('Introduction to Programming', 3),
	('Data Structures', 4),
    ('Web Development Fundamentals', 3),
    ('Mobile App Development', 3),
    ('Cybersecurity Basics', 2);
    
-- Insert Courses_Students (Many-to-Many)
INSERT INTO courses_students (student_id, course_id) VALUES
	(1, 1), (1, 2),
	(2, 2), (2, 3),
    (3, 3), (3, 4),
    (4, 4), (4, 5),
    (5, 1), (5, 5);
    
-- Update Instructor's Department
UPDATE instructors
SET department = "Full Stack Development"
WHERE id = 1;

-- Update Student's name
UPDATE students
SET name = "Mary"
WHERE id = 2;

-- Delete a specific student
DELETE FROM students
WHERE id = 3;


-- DQL (Data Query Language)

-- Select All Instructors
SELECT instructors_name, department FROM instructors;

-- Select a specific instrutor by id
SELECT * FROM instructors
WHERE id = 2;

-- List Instructors Ordered by Name Alphabetically
SELECT * FROM instructors
ORDER BY instructors_name;

-- List Students Order by Enrollment Date desc
SELECT * FROM students
ORDER BY enrollment_date DESC;

-- Find students with Names containing 'Evan'
SELECT * FROM students
WHERE name LIKE '%va%';

-- Find Courses with Title starting with 'I'
SELECT * FROM courses
WHERE title LIKE 'I%';

-- Find students with names starting with any character followed by 'lic'
SELECT * FROM students
WHERE name LIKE '_lic%';

-- BONUS: Find all courses wnrolled by a specific student
SELECT * FROM courses
WHERE id IN (
	SELECT course_id FROM courses_students
    WHERE student_id = 1
);

-- List All Instructors with Their Students
SELECT *
FROM instructors i
LEFT JOIN students s ON i.id = s.instructors_id;

-- List All Students and their enrollment course
SELECT *
FROM students s
JOIN courses_students cs ON s.id = cs.student_id
JOIN courses c ON cs.course_id = c.id;

-- Count the Number of Students per Instructor
SELECT i.instructors_name AS Instructor, COUNT(s.id) AS StudentCount
FROM instructors i
LEFT JOIN students s ON i.id = s.instructors_id
GROUP BY i.instructors_name;

-- Bonus: Find Courses Taken by Students Under a Specific Instructor
SELECT c.title AS Course, c.credits AS Credits
FROM courses c
JOIN courses_students cs ON c.id = cs.course_id
JOIN students s ON cs.student_id = s.id
WHERE s.instructors_id = 1;