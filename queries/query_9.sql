SELECT subjects.subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Doe');
