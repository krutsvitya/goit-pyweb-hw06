SELECT groups.group_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = (SELECT id FROM subjects WHERE subject_name = 'Math')
GROUP BY groups.id;
