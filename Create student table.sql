CREATE DATABASE Class_activity;

GO

CREATE TABLE Student(
	ID INT IDENTITY(1,1) PRIMARY KEY,
	Name VARCHAR(50) NOT NULL,
	Age INT NULL,
	Major VARCHAR (60) NOT NULL,
)
GO

SET IDENTITY_INSERT Student ON;
INSERT INTO Student (ID, Name, Age, Major) VALUES
(1, 'John Smith', 20, 'computer science'),
(2, 'Maria Garcia', 17, 'Information Systems'),
(3, 'James Lee', 19, 'Software Engeneering'),
(4, 'Aisha patel', 21, 'Data Analytics')
;

GO

SELECT * FROM Student;

SELECT * FROM Student WHERE Age > 18; 
