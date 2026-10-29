CREATE DATABASE Student_database5;
GO
--CREATE A DATABASE
CREATE DATABASE StudentDatabase;
GO
--SELECT THE DATABASE
USE Student_Database;
GO
--CREATE THE STUDENTS TABLE
CREATE TABLE Students(
	StudentID INT PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	Email VARCHAR(100),
	Status VARCHAR(20),
	RegistrastionDate DATE
);
GO

--ADD STUDENT RECORDS
INSERT INTO Students
	(StudentID,Firstname,lastName, Email,Status, RegistrastionDate)
VALUES 
(2026001.'Lerato', 'Dlamini', 'lerato@example.org','Active', '2026-01-05'),

GO
--DISPLAY ALL FROM STUDENTS
SELECT * FROM Students;
GO
