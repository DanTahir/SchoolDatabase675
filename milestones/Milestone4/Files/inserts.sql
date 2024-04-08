USE Tahir_SchoolDB;

-- Tables with no foreign key

INSERT INTO Admin (username, password) VALUES ("root", "root");
INSERT INTO Admin (username, password) VALUES ("admin", "root");
INSERT INTO Admin (username, password) VALUES ("administrator", "root");

INSERT INTO Department (name, description) VALUES ("Computer Science", "Responsible for the computer science program");
INSERT INTO Department (name, description) VALUES ("Physics", "Responsible for topics in the physical sciences");
INSERT INTO Department (name, description) VALUES ("Math", "Responsible for overseeing the mathematics program");
INSERT INTO Department (name, description) VALUES ("Administration", "Administration of the university");

INSERT INTO Parking_Lot (name, spaces_available) VALUES ("Student Lot", 500);
INSERT INTO Parking_Lot (name, spaces_available) VALUES ("Teacher Lot", 200);
INSERT INTO Parking_Lot (name, spaces_available) VALUES ("Staff Lot", 100);

INSERT INTO Major (name, description) VALUES ("Computer Science", "A degree in computer science");
INSERT INTO Major (name, description) VALUES ("Physics", "A degree in physical science");
INSERT INTO Major (name, description) VALUES ("Math", "A degree in mathematics");

INSERT INTO Classroom (building_name, room_number, seats) VALUES("Hensill Hall", "543", 60);
INSERT INTO Classroom (building_name, room_number, seats) VALUES("HSS", "221", 50);
INSERT INTO Classroom (name, building_name, room_number, seats) VALUES("CS Lab", "Creative Arts", "128", 60);

INSERT INTO Classroom_Resource (category, name, description, quantity)
VALUES ("seating", "trapezoidal desk", "seats two students", 120);
INSERT INTO Classroom_Resource (category, name, description, quantity)
VALUES ("seating", "standard chair", "seats one student", 240);
INSERT INTO Classroom_Resource (category, name, description, quantity)
VALUES ("tech", "projector", "1000 lumens", 40);

INSERT INTO Semester (year, season, start_date, end_date) VALUES (2024, "Spring", "2024-01-29", "2024-05-31");
INSERT INTO Semester (year, season, start_date, end_date) VALUES (2023, "Fall", "2023-08-21", "2023-12-27");
INSERT INTO Semester (year, season, start_date, end_date) VALUES (2023, "Summer", "2023-06-05", "2023-08-15");

INSERT INTO Teacher_Role (name, payscale) 
VALUES ("Junior Teacher", 4000.00);
INSERT INTO Teacher_Role (name, payscale)
VALUES ("Senior Teacher", 5000.00);
INSERT INTO Teacher_Role (name, payscale)
VALUES ("Department Chair", 1000.00);
INSERT INTO Teacher_Role (name, payscale)
VALUES ("Teaching Assistant", 2000.00);

INSERT INTO Staff_Role (name, payscale) 
VALUES ("Department Assistant", 4000.00);
INSERT INTO Staff_Role (name, payscale) 
VALUES ("Administrator", 5000.00);
INSERT INTO Staff_Role (name, payscale) 
VALUES ("Counselor", 3000.00);

-- Tables with foreign keys that aren't associative

INSERT INTO Student (first_name, last_name, date_of_birth, date_of_enroll, username, password, parking_lot_id)
VALUES ("John", "Smith", "2004-05-05", "2022-03-04", "jsmith1", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Student Lot'));
INSERT INTO Student (first_name, last_name, date_of_birth, date_of_enroll, username, password, parking_lot_id)
VALUES ("Kelly", "Vance", "2003-02-15", "2021-04-06", "kvance", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Student Lot'));
INSERT INTO Student (first_name, last_name, date_of_birth, date_of_enroll, username, password, parking_lot_id)
VALUES ("Michael", "Mathews", "2005-09-25", "2023-04-14", "mmathews", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Student Lot'));
INSERT INTO Student (first_name, last_name, date_of_birth, date_of_enroll, username, password, parking_lot_id)
VALUES ("Sheila", "Kelvert", "2004-11-25", "2022-05-17", "skelvert", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Student Lot'));


INSERT INTO Teacher (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("John", "Roberts", "2015-05-24", "jroberts1", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Teacher Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Computer Science'));
INSERT INTO Teacher (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Robert", "Bierman", "2012-08-13", "rbierman", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Teacher Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Computer Science'));
INSERT INTO Teacher (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Jessica", "Vilson", "2015-05-24", "jvilson2", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Teacher Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Math'));
INSERT INTO Teacher (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Allison", "Peterman", "2016-02-15", "apeterman", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Teacher Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Physics'));
INSERT INTO Teacher (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Darius", "Golvin", "2016-02-15", "dgolvin", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Teacher Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Physics'));

INSERT INTO Staff (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Valerie", "Vance", "2005-01-14", "vvance1", "default", 
(SELECT lot_id FROM Parking_Lot WHERE name = 'Staff Lot'), 
(SELECT dept_id FROM DEPARTMENT WHERE name = 'Computer Science'));
INSERT INTO Staff (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Steven", "Mervins", "2020-09-30", "smervins4", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Staff Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Administration'));
INSERT INTO Staff (first_name, last_name, date_of_hiring, username, password, parking_lot_id, dept_id)
VALUES ("Shaira", "Iqbal", "2009-02-22", "siqbal1", "default", (SELECT lot_id FROM Parking_Lot WHERE name = 'Staff Lot'), (SELECT dept_id FROM DEPARTMENT WHERE name = 'Administration'));

INSERT INTO Email (address, student_id) 
VALUES ("jsmith1@sfsu.edu", (SELECT student_id FROM Student WHERE username = 'jsmith1'));
INSERT INTO Email (address, student_id) 
VALUES ("kvance@sfsu.edu", (SELECT student_id FROM Student WHERE username = 'kvance'));
INSERT INTO Email (address, student_id) 
VALUES ("mmathews@sfsu.edu", (SELECT student_id FROM Student WHERE username = 'mmathews'));
INSERT INTO Email (address, teacher_id) 
VALUES ("jroberts1@sfsu.edu", (SELECT teacher_id FROM Teacher WHERE username = 'jroberts1'));
INSERT INTO Email (address, teacher_id) 
VALUES ("rbierman@sfsu.edu", (SELECT teacher_id FROM Teacher WHERE username = 'rbierman'));
INSERT INTO Email (address, teacher_id) 
VALUES ("jvilson2@sfsu.edu", (SELECT teacher_id FROM Teacher WHERE username = 'jvilson2'));
INSERT INTO Email (address, teacher_id) 
VALUES ("apeterman@sfsu.edu", (SELECT teacher_id FROM Teacher WHERE username = 'apeterman'));
INSERT INTO Email (address, staff_id) 
VALUES ("vvance1@sfsu.edu", (SELECT staff_id FROM Staff WHERE username = 'vvance1'));
INSERT INTO Email (address, staff_id) 
VALUES ("smervins4@sfsu.edu", (SELECT staff_id FROM Staff WHERE username = 'smervins4'));
INSERT INTO Email (address, staff_id) 
VALUES ("siqbal1@sfsu.edu", (SELECT staff_id FROM Staff WHERE username = 'siqbal1'));

INSERT INTO Organization (name, description, days, start_time, end_time, classroom_id)
VALUES ("Hacker Club", 
"Come learn to hack with your fellow SFSU CS students",
 "M,W", "19:00", "20:00", 
	(SELECT classroom_id FROM Classroom 
	WHERE building_name = 'Creative Arts' 
	AND room_number = '128')
 );
INSERT INTO Organization (name, description, days, start_time, end_time, classroom_id)
VALUES ("Mathletes", 
"Hone your math skills with your fellow students",
 "TH", "15:00", "17:00", 
	(SELECT classroom_id FROM Classroom 
	WHERE building_name = 'Hensill Hall' 
	AND room_number = '543')
 );
INSERT INTO Organization (name, description, days, start_time, end_time, classroom_id)
VALUES ("Physics Club", 
"Unlock the mysteries of the universe",
 "T", "12:00", "14:00", 
	(SELECT classroom_id FROM Classroom 
	WHERE building_name = 'HSS' 
	AND room_number = '221')
 );
 
INSERT INTO Subject (name, description, dept_id)
SELECT "CSC", "Computer Science", d.dept_id
FROM Department d
WHERE d.name = 'Computer Science';
INSERT INTO Subject (name, description, dept_id)
SELECT "MATH", "Mathematics", d.dept_id
FROM Department d
WHERE d.name = 'Math'; 
INSERT INTO Subject (name, description, dept_id)
SELECT "PHYS", "Physics", d.dept_id
FROM Department d
WHERE d.name = 'Physics'; 
 
INSERT INTO Class (name, number, credit_hours, subject_id)
SELECT "Introduction to Web Software Development", 
"317", 3.0, s.subject_id
FROM Subject s
WHERE s.name = 'CSC'; 
INSERT INTO Class (name, number, credit_hours, subject_id)
SELECT "Programming Methodology", 
"340", 3.0, s.subject_id
FROM Subject s
WHERE s.name = 'CSC'; 
INSERT INTO Class (name, number, credit_hours, subject_id)
SELECT "General Physics with Calculus I", 
"220", 3.0, s.subject_id
FROM Subject s
WHERE s.name = 'PHYS'; 
INSERT INTO Class (name, number, credit_hours, subject_id)
SELECT "General Physics with Calculus I Laboratory", 
"222", 1.0, s.subject_id
FROM Subject s
WHERE s.name = 'PHYS'; 
INSERT INTO Class (name, number, credit_hours, subject_id)
SELECT "Calculus I", 
"226", 4.0, s.subject_id
FROM Subject s
WHERE s.name = 'MATH';  


-- csc 317 01
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"CSC 317 Section 01", "M,W", "12:00", "1:15",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '317' AND s.name = "CSC") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'Creative Arts' 
	AND room_number = '128') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;
-- csc 317 02
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"CSC 317 Section 02", "M,W", "2:00", "3:15",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '317' AND s.name = "CSC") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'Creative Arts' 
	AND room_number = '128') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;
-- csc 340 01
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"CSC 340 Section 01", "T,TH", "12:00", "1:15",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '340' AND s.name = "CSC") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'Creative Arts' 
	AND room_number = '128') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;
-- PHYS 220 01
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"PHYS 220 Section 01", "T,TH", "2:00", "3:15",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '220' AND s.name = "PHYS") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'Hensill Hall' 
	AND room_number = '543') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;
-- PHYS 222 01
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"PHYS 222 Section 01", "TH", "4:00", "4:50",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '222' AND s.name = "PHYS") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'Hensill Hall' 
	AND room_number = '543') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;
-- MATH 226 01
INSERT INTO Class_Section (name, days, start_time, end_time, 
	class_id, classroom_id, semester_id)
SELECT 
	"MATH 226 Section 01", "M,T,W,TH", "11:00", "11:50",
	(SELECT c.class_id FROM Class c JOIN Subject s ON c.subject_id = s.subject_id 
	WHERE c.number = '226' AND s.name = "MATH") AS classid,
    (SELECT classroom_id FROM Classroom 
    WHERE building_name = 'HSS' 
	AND room_number = '221') AS classroomid,
    (SELECT semester_id FROM Semester 
    WHERE year = 2024 
	AND season = 'Spring') AS semesterid;

INSERT INTO Required_Resource (category, name, class_section_id)
SELECT
	'Book', 'Webdev Book', cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'CSC 317 Section 01' AND c.number = '317' AND s.name = 'CSC';
INSERT INTO Required_Resource (category, name, class_section_id)
SELECT
	'Book', 'Webdev Book 2', cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'CSC 317 Section 02' AND c.number = '317' AND s.name = 'CSC';
INSERT INTO Required_Resource (category, name, class_section_id)
SELECT
	'Book', 'Physics Book', cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'PHYS 220 Section 01' AND c.number = '220' AND s.name = 'PHYS';
INSERT INTO Required_Resource (category, name, class_section_id)
SELECT
	'Book', 'Calculus Book', cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'MATH 226 Section 01' AND c.number = '226' AND s.name = 'MATH';
    
INSERT INTO Module (name, description, class_section_id)
SELECT
	'CSC 317 Module 1', 'Documents and assignments for CSC 317', 
    cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'CSC 317 Section 01' AND c.number = '317' AND s.name = 'CSC';    
INSERT INTO Module (name, description, class_section_id)
SELECT
	'PHYS 220 Module 1', 'Documents and assignments for PHYS 220', 
    cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'PHYS 220 Section 01' AND c.number = '220' AND s.name = 'PHYS';    
INSERT INTO Module (name, description, class_section_id)
SELECT
	'MATH 226 Module 1', 'Documents and assignments for Math 226', 
    cs.class_section_id
FROM
	Class_Section cs
JOIN
	Class c ON cs.class_id = c.class_id
JOIN
	Subject s ON c.subject_id = s.subject_id
WHERE
	cs.name = 'MATH 226 Section 01' AND c.number = '226' AND s.name = 'MATH';    
    
INSERT INTO Document (name, description, link, module_id)
SELECT
	'CSC 317 Document 1', 'A class document for CSC 317', 'CSC317filename.pdf',
    m.module_id
FROM
	Module m
WHERE
	m.name = 'CSC 317 Module 1';
INSERT INTO Document (name, description, link, module_id)
SELECT
	'PHYS 220 Document 1', 'A class document for PHYS 220', 'PHYS220filename.pdf',
    m.module_id
FROM
	Module m
WHERE
	m.name = 'PHYS 220 Module 1';
INSERT INTO Document (name, description, link, module_id)
SELECT
	'MATH 226 Document 1', 'A class document for MATH 226', 'MATH226filename.pdf',
    m.module_id
FROM
	Module m
WHERE
	m.name = 'MATH 226 Module 1';
    
INSERT INTO Assignment (name, description, link, top_score, module_id)
SELECT
	'CSC 317 Assignment 1', 'A class assignment for CSC 317', 'CSC317filename.pdf',
    100, m.module_id
FROM
	Module m
WHERE
	m.name = 'CSC 317 Module 1';  
INSERT INTO Assignment (name, description, link, top_score, module_id)
SELECT
	'PHYS 220 Assignment 1', 'A class assignment for PHYS 220', 'PHYS220filename.pdf',
    100, m.module_id
FROM
	Module m
WHERE
	m.name = 'PHYS 220 Module 1';  
INSERT INTO Assignment (name, description, link, top_score, module_id)
SELECT
	'MATH 226 Assignment 1', 'A class assignment for MATH 226', 'MATH226filename.pdf',
    100, m.module_id
FROM
	Module m
WHERE
	m.name = 'MATH 226 Module 1';  
    
INSERT INTO Quiz (title, description, max_score, module_id)
SELECT
	'CSC 317 Quiz 1', 'A class quiz for CSC 317', 100, m.module_id
FROM
	Module m
WHERE
	m.name = 'CSC 317 Module 1';      
INSERT INTO Quiz (title, description, max_score, module_id)
SELECT
	'PHYS 220 Quiz 1', 'A class quiz for PHYS 220', 100, m.module_id
FROM
	Module m
WHERE
	m.name = 'PHYS 220 Module 1';      
INSERT INTO Quiz (title, description, max_score, module_id)
SELECT
	'MATH 226 Quiz 1', 'A class quiz for MATH 226', 100, m.module_id
FROM
	Module m
WHERE
	m.name = 'MATH 226 Module 1';      
    
INSERT INTO Quiz_Question (question, quiz_id)
SELECT
	"CSC 317 Quiz 1 Question 1", q.quiz_id
FROM
	Quiz q
WHERE
	q.title = "CSC 317 Quiz 1";
INSERT INTO Quiz_Question (question, quiz_id)
SELECT
	"PHYS 220 Quiz 1 Question 1", q.quiz_id
FROM
	Quiz q
WHERE
	q.title = "PHYS 220 Quiz 1";
INSERT INTO Quiz_Question (question, quiz_id)
SELECT
	"MATH 226 Quiz 1 Question 1", q.quiz_id
FROM
	Quiz q
WHERE
	q.title = "MATH 226 Quiz 1";
    
 INSERT INTO Quiz_Answer (answer, is_correct, quiz_question_id)
 SELECT
	"CSC 317 Quiz 1 Question 1 Answer 1", 1, qq.quiz_question_id
FROM
	Quiz_Question qq
WHERE
	qq.question = "CSC 317 Quiz 1 Question 1";
 INSERT INTO Quiz_Answer (answer, is_correct, quiz_question_id)
 SELECT
	"PHYS 220 Quiz 1 Question 1 Answer 1", 1, qq.quiz_question_id
FROM
	Quiz_Question qq
WHERE
	qq.question = "PHYS 220 Quiz 1 Question 1";
 INSERT INTO Quiz_Answer (answer, is_correct, quiz_question_id)
 SELECT
	"MATH 226 Quiz 1 Question 1 Answer 1", 1, qq.quiz_question_id
FROM
	Quiz_Question qq
WHERE
	qq.question = "MATH 226 Quiz 1 Question 1";
    
    
 
-- Associative tables

INSERT INTO `Org-Student` (student_id, org_id)
SELECT s.student_id, o.org_id
FROM Student s
CROSS JOIN Organization o
WHERE s.username = 'jsmith1' AND o.name = 'Hacker Club';
INSERT INTO `Org-Student` (student_id, org_id)
SELECT s.student_id, o.org_id
FROM Student s
CROSS JOIN Organization o
WHERE s.username = 'kvance' AND o.name = 'Mathletes';
INSERT INTO `Org-Student` (student_id, org_id)
SELECT s.student_id, o.org_id
FROM Student s
CROSS JOIN Organization o
WHERE s.username = 'mmathews' AND o.name = 'Physics Club';

INSERT INTO `Org-Teacher` (teacher_id, org_id)
SELECT t.teacher_id, o.org_id
FROM Teacher t
CROSS JOIN Organization o
WHERE t.username = 'rbierman' AND o.name = 'Hacker Club';
INSERT INTO `Org-Teacher` (teacher_id, org_id)
SELECT t.teacher_id, o.org_id
FROM Teacher t
CROSS JOIN Organization o
WHERE t.username = 'jvilson2' AND o.name = 'Mathletes';
INSERT INTO `Org-Teacher` (teacher_id, org_id)
SELECT t.teacher_id, o.org_id
FROM Teacher t
CROSS JOIN Organization o
WHERE t.username = 'apeterman' AND o.name = 'Physics Club';

INSERT INTO `Major_Requirement` (major_id, class_id)
SELECT m.major_id, c.class_id
FROM Major m
CROSS JOIN Class c
WHERE m.name = "Computer Science" AND c.name = "Introduction to Web Software Development";
INSERT INTO `Major_Requirement` (major_id, class_id)
SELECT m.major_id, c.class_id
FROM Major m
CROSS JOIN Class c
WHERE m.name = "Physics" AND c.name = "General Physics with Calculus I";
INSERT INTO `Major_Requirement` (major_id, class_id)
SELECT m.major_id, c.class_id
FROM Major m
CROSS JOIN Class c
WHERE m.name = "Math" AND c.name = "Calculus I";

INSERT INTO `Student-Major` (student_id, major_id)
SELECT s.student_id, m.major_id
FROM Student s
CROSS JOIN Major m
WHERE s.username = "jsmith1" AND m.name = "Computer Science";
INSERT INTO `Student-Major` (student_id, major_id)
SELECT s.student_id, m.major_id
FROM Student s
CROSS JOIN Major m
WHERE s.username = "skelvert" AND m.name = "Computer Science";
INSERT INTO `Student-Major` (student_id, major_id)
SELECT s.student_id, m.major_id
FROM Student s
CROSS JOIN Major m
WHERE s.username = "kvance" AND m.name = "Math";
INSERT INTO `Student-Major` (student_id, major_id)
SELECT s.student_id, m.major_id
FROM Student s
CROSS JOIN Major m
WHERE s.username = "mmathews" AND m.name = "Physics";

INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "jsmith1" AND cs.name = "CSC 317 Section 01";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "skelvert" AND cs.name = "CSC 317 Section 02";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "jsmith1" AND cs.name = "CSC 340 Section 01";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "skelvert" AND cs.name = "CSC 340 Section 01";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "kvance" AND cs.name = "MATH 226 Section 01";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "mmathews" AND cs.name = "PHYS 220 Section 01";
INSERT INTO `Class_Section-Student` (student_id, class_section_id)
SELECT s.student_id, cs.class_section_id
FROM Student s
CROSS JOIN Class_Section cs
WHERE s.username = "mmathews" AND cs.name = "PHYS 222 Section 01";

INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "rbierman" AND cs.name = "CSC 317 Section 01";
INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "rbierman" AND cs.name = "CSC 317 Section 02";
INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "jroberts1" AND cs.name = "CSC 340 Section 01";
INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "jvilson2" AND cs.name = "MATH 226 Section 01";
INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "apeterman" AND cs.name = "PHYS 220 Section 01";
INSERT INTO `Class_Section-Teacher` (teacher_id, class_section_id)
SELECT t.teacher_id, cs.class_section_id
FROM Teacher t
CROSS JOIN Class_Section cs
WHERE t.username = "dgolvin" AND cs.name = "PHYS 222 Section 01";

INSERT INTO `Student-Completed-Assignment` (student_id, assignment_id, score, submittal_link)
SELECT s.student_id, a.assignment_id, 100, "assignment.pdf"
FROM Student s
CROSS JOIN Assignment a
WHERE s.username = "jsmith1" AND a.name = "CSC 317 Assignment 1";
INSERT INTO `Student-Completed-Assignment` (student_id, assignment_id, score, submittal_link)
SELECT s.student_id, a.assignment_id, 95, "assignment.pdf"
FROM Student s
CROSS JOIN Assignment a
WHERE s.username = "kvance" AND a.name = "MATH 226 Assignment 1";
INSERT INTO `Student-Completed-Assignment` (student_id, assignment_id, score, submittal_link)
SELECT s.student_id, a.assignment_id, 90, "assignment.pdf"
FROM Student s
CROSS JOIN Assignment a
WHERE s.username = "mmathews" AND a.name = "PHYS 220 Assignment 1";

INSERT INTO `Student-Quiz_Answer` (student_id, quiz_answer_id)
SELECT s.student_id, qa.quiz_answer_id
FROM Student s
CROSS JOIN Quiz_Answer qa
WHERE s.username = "jsmith1" AND qa.answer = "CSC 317 Quiz 1 Question 1 Answer 1";
INSERT INTO `Student-Quiz_Answer` (student_id, quiz_answer_id)
SELECT s.student_id, qa.quiz_answer_id
FROM Student s
CROSS JOIN Quiz_Answer qa
WHERE s.username = "kvance" AND qa.answer = "MATH 226 Quiz 1 Question 1 Answer 1";
INSERT INTO `Student-Quiz_Answer` (student_id, quiz_answer_id)
SELECT s.student_id, qa.quiz_answer_id
FROM Student s
CROSS JOIN Quiz_Answer qa
WHERE s.username = "mmathews" AND qa.answer = "PHYS 220 Quiz 1 Question 1 Answer 1";


INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "jroberts1" AND tr.name = "Junior Teacher";
INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "rbierman" AND tr.name = "Senior Teacher";
INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "rbierman" AND tr.name = "Department Chair";
INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "jvilson2" AND tr.name = "Junior Teacher";
INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "apeterman" AND tr.name = "Senior Teacher";
INSERT INTO `Teacher-Teacher_Role` (teacher_id, teacher_role_id)
SELECT t.teacher_id, tr.teacher_role_id
FROM Teacher t
CROSS JOIN Teacher_Role tr
WHERE t.username = "dgolvin" AND tr.name = "Teaching Assistant";

INSERT INTO `Staff-Staff_Role` (staff_id, staff_role_id)
SELECT s.staff_id, sr.staff_role_id
FROM Staff s
CROSS JOIN Staff_Role sr
WHERE s.username = "vvance1" AND sr.name = "Department Assistant";
INSERT INTO `Staff-Staff_Role` (staff_id, staff_role_id)
SELECT s.staff_id, sr.staff_role_id
FROM Staff s
CROSS JOIN Staff_Role sr
WHERE s.username = "smervins4" AND sr.name = "Administrator";
INSERT INTO `Staff-Staff_Role` (staff_id, staff_role_id)
SELECT s.staff_id, sr.staff_role_id
FROM Staff s
CROSS JOIN Staff_Role sr
WHERE s.username = "siqbal1" AND sr.name = "Counselor";

INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 30
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "Hensill Hall"
AND cr.room_number = "543"
AND crr.name = "trapezoidal desk";
INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 60
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "Hensill Hall"
AND cr.room_number = "543"
AND crr.name = "standard chair";
INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 30
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "HSS"
AND cr.room_number = "221"
AND crr.name = "trapezoidal desk";
INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 60
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "HSS"
AND cr.room_number = "221"
AND crr.name = "standard chair";
INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 30
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "Creative Arts"
AND cr.room_number = "128"
AND crr.name = "trapezoidal desk";
INSERT INTO `Classroom-Classroom_Resource` (classroom_id, classroom_resource_id, quantity_assigned)
SELECT cr.classroom_id, crr.classroom_resource_id, 60
FROM Classroom cr 
CROSS JOIN Classroom_Resource crr
WHERE cr.building_name = "Creative Arts"
AND cr.room_number = "128"
AND crr.name = "standard chair";



-- Payment inserts

INSERT INTO Teacher_Payment (teacher_id, payment_amount, date_made)
SELECT t.teacher_id, sum(tr.payscale), CURDATE()
FROM Teacher t 
JOIN `Teacher-Teacher_Role` ttr ON t.teacher_id = ttr.teacher_id
JOIN Teacher_Role tr ON ttr.teacher_role_id = tr.teacher_role_id
WHERE t.username = "jroberts1"
GROUP BY t.teacher_id;
INSERT INTO Teacher_Payment (teacher_id, payment_amount, date_made)
SELECT t.teacher_id, sum(tr.payscale), CURDATE()
FROM Teacher t 
JOIN `Teacher-Teacher_Role` ttr ON t.teacher_id = ttr.teacher_id
JOIN Teacher_Role tr ON ttr.teacher_role_id = tr.teacher_role_id
WHERE t.username = "rbierman"
GROUP BY t.teacher_id;
INSERT INTO Teacher_Payment (teacher_id, payment_amount, date_made)
SELECT t.teacher_id, sum(tr.payscale), CURDATE()
FROM Teacher t 
JOIN `Teacher-Teacher_Role` ttr ON t.teacher_id = ttr.teacher_id
JOIN Teacher_Role tr ON ttr.teacher_role_id = tr.teacher_role_id
WHERE t.username = "jvilson2"
GROUP BY t.teacher_id;
INSERT INTO Teacher_Payment (teacher_id, payment_amount, date_made)
SELECT t.teacher_id, sum(tr.payscale), CURDATE()
FROM Teacher t 
JOIN `Teacher-Teacher_Role` ttr ON t.teacher_id = ttr.teacher_id
JOIN Teacher_Role tr ON ttr.teacher_role_id = tr.teacher_role_id
WHERE t.username = "apeterman"
GROUP BY t.teacher_id;
INSERT INTO Teacher_Payment (teacher_id, payment_amount, date_made)
SELECT t.teacher_id, sum(tr.payscale), CURDATE()
FROM Teacher t 
JOIN `Teacher-Teacher_Role` ttr ON t.teacher_id = ttr.teacher_id
JOIN Teacher_Role tr ON ttr.teacher_role_id = tr.teacher_role_id
WHERE t.username = "dgolvin"
GROUP BY t.teacher_id;

INSERT INTO Staff_Payment (staff_id, payment_amount, date_made)
SELECT s.staff_id, sum(sr.payscale), CURDATE()
FROM Staff s 
JOIN `Staff-Staff_Role` ssr ON s.staff_id = ssr.staff_id
JOIN Staff_Role sr ON ssr.staff_role_id = sr.staff_role_id
WHERE s.username = "vvance1"
GROUP BY s.staff_id;
INSERT INTO Staff_Payment (staff_id, payment_amount, date_made)
SELECT s.staff_id, sum(sr.payscale), CURDATE()
FROM Staff s 
JOIN `Staff-Staff_Role` ssr ON s.staff_id = ssr.staff_id
JOIN Staff_Role sr ON ssr.staff_role_id = sr.staff_role_id
WHERE s.username = "smervins4"
GROUP BY s.staff_id;
INSERT INTO Staff_Payment (staff_id, payment_amount, date_made)
SELECT s.staff_id, sum(sr.payscale), CURDATE()
FROM Staff s 
JOIN `Staff-Staff_Role` ssr ON s.staff_id = ssr.staff_id
JOIN Staff_Role sr ON ssr.staff_role_id = sr.staff_role_id
WHERE s.username = "siqbal1"
GROUP BY s.staff_id;

INSERT INTO Student_Payment (student_id, payment_amount, date_made, semester_id)
SELECT 
	(SELECT s.student_id 
    FROM Student s 
    WHERE s.username = "jsmith1") AS studentid,
    (SELECT SUM(c.credit_hours) * 300
    FROM Student s 
    JOIN `Class_Section-Student` css ON s.student_id = css.student_id
    JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
    JOIN Class c ON cs.class_id = c.class_id
    WHERE s.username = "jsmith1"
    GROUP BY s.student_id) AS paymentamount,
    CURDATE(),
    (SELECT semester_id 
    FROM Semester 
    WHERE year = 2024 AND season = 'Spring') AS semesterid;
INSERT INTO Student_Payment (student_id, payment_amount, date_made, semester_id)
SELECT 
	(SELECT s.student_id 
    FROM Student s 
    WHERE s.username = "kvance") AS studentid,
    (SELECT SUM(c.credit_hours) * 300
    FROM Student s 
    JOIN `Class_Section-Student` css ON s.student_id = css.student_id
    JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
    JOIN Class c ON cs.class_id = c.class_id
    WHERE s.username = "kvance"
    GROUP BY s.student_id) AS paymentamount,
    CURDATE(),
    (SELECT semester_id 
    FROM Semester 
    WHERE year = 2024 AND season = 'Spring') AS semesterid;    
INSERT INTO Student_Payment (student_id, payment_amount, date_made, semester_id)
SELECT 
	(SELECT s.student_id 
    FROM Student s 
    WHERE s.username = "mmathews") AS studentid,
    (SELECT SUM(c.credit_hours) * 300
    FROM Student s 
    JOIN `Class_Section-Student` css ON s.student_id = css.student_id
    JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
    JOIN Class c ON cs.class_id = c.class_id
    WHERE s.username = "mmathews"
    GROUP BY s.student_id) AS paymentamount,
    CURDATE(),
    (SELECT semester_id 
    FROM Semester 
    WHERE year = 2024 AND season = 'Spring') AS semesterid;
INSERT INTO Student_Payment (student_id, payment_amount, date_made, semester_id)
SELECT 
	(SELECT s.student_id 
    FROM Student s 
    WHERE s.username = "skelvert") AS studentid,
    (SELECT SUM(c.credit_hours) * 300
    FROM Student s 
    JOIN `Class_Section-Student` css ON s.student_id = css.student_id
    JOIN Class_Section cs ON css.class_section_id = cs.class_section_id
    JOIN Class c ON cs.class_id = c.class_id
    WHERE s.username = "skelvert"
    GROUP BY s.student_id) AS paymentamount,
    CURDATE(),
    (SELECT semester_id 
    FROM Semester 
    WHERE year = 2024 AND season = 'Spring') AS semesterid;
