SELECT students.name, grades.grade, grades.date
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = (SELECT id FROM groups WHERE group_name = 'Group 1')
AND grades.subject_id = (SELECT id FROM subjects WHERE subject_name = 'Math');
