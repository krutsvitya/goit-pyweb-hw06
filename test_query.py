import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

group_id = 1

with open('queries/query_7.sql', 'r') as file:
    sql_query = file.read().replace('GROUP_ID', str(group_id))

cursor.execute(sql_query)
students = cursor.fetchall()

print(students)

conn.close()
