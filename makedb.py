import sqlite3

conn = sqlite3.connect('makedb.db')
cur = conn.cursor()

cur.execute("create table if not exists courses(course_id int primary key, duration int)")
cur.execute("create table if not exists student (sap int primary key,name text not null, course_id text not null, semester int, foreign key(course_id) references courses(course_id))")

# insert into student va
cur.execute("insert into courses values (1,12)")
output = cur.execute("select * from courses")
for i in output:
    print (i)