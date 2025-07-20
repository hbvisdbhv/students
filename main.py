import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT, 
age INTEGER,
major TEXT                
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
course_id INTEGER PRIMARY KEY AUTOINCREMENT,
course_name TEXT
               
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
corse_id INTEGER, 
student_id INTEGER,
FOREIGN KEY (course_id) REFERENCES courses(id)     
FOREIGN KEY (students_id) REFERENCES students(id)                 
)
""")

