SELECT name
FROM students
WHERE group_id = (SELECT id FROM groups WHERE group_name = 'Group 1');
