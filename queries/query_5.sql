SELECT subject_name
FROM subjects
WHERE teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe');
