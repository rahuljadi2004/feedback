# import sqlite3
# connection=sqlite3.connect('FeedBack.db')
# cursor=connection.cursor()
# cmd="""create table if not exists Student(
#     fullname text not null,
#     usn varchar(10) primary key not null,
#     semester integer not null,
#     branch varchar(10) not null,
#     cgpa float not null
    
#     )
    
# """
# cursor.execute(cmd)
# connection.commit()
# cmd = "INSERT INTO Student(fullname, usn, semester, branch, cgpa) VALUES (?, ?, ?, ?, ?)"
# cursor.execute(cmd, ('RAHUL', '23ad032', 5, 'AI-DS', 8.5))
# cursor.execute(cmd, ('SANJAY', '23ad038', 5, 'MECH', 9.9))
# cursor.execute(cmd, ('AMIT', '23cs125', 5, 'CSE', 7.8))


# connection.commit()

# f=cursor.execute("select * from student").fetchall()
# print(f)
# connection.close()


import sqlite3

connection = sqlite3.connect('FeedBack.db')
cursor = connection.cursor()

cmd = """
create table if not exists Student(
    fullname text not null,
    usn varchar(10) primary key not null,
    semester integer not null,
    branch varchar(10) not null,
    cgpa float not null
)
"""
cursor.execute(cmd)
connection.commit()

# Insert Data
cmd = "INSERT INTO Student(fullname, usn, semester, branch, cgpa) VALUES (?, ?, ?, ?, ?)"
# cursor.execute(cmd, ('RAHUL', '2332', 5, 'AI-DS', 8.5))
# cursor.execute(cmd, ('SANJAY', '238', 5, 'MECH', 9.9))
# cursor.execute(cmd, ('AMIT', '23125', 5, 'CSE', 7.8))

connection.commit()


f = cursor.execute("SELECT * FROM Student").fetchall()
print(f)



connection.close()
