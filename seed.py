import sqlite3
import random
from faker import Faker

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

fake = Faker()

groups = ['Group 1', 'Group 2', 'Group 3']
for group_name in groups:
    cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group_name,))

teachers = []
for _ in range(4):
    name = fake.name()
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (name,))
    teachers.append(cursor.lastrowid)  # Зберігаємо ID викладачів

subjects = ['Math', 'Physics', 'Biology', 'History', 'Chemistry']
for subject in subjects:
    teacher_id = random.choice(teachers)
    cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

student_ids = []
for _ in range(50):
    name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

    student_id = cursor.lastrowid
    student_ids.append(student_id)

for student_id in student_ids:
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(random.randint(15, 20)):
            grade = random.randint(1, 5)
            date_value = fake.date_this_year()
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date_value))


conn.commit()
cursor.close()
conn.close()


