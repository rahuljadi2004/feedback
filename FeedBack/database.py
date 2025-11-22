import sqlite3
connection=sqlite3.connect('FeedBack.db')
cursor=connection.cursor()
cmd="""
CREATE TABLE IF NOT EXISTS FeedBack(
    id  integer primary key AUTOINCREMENT,
    fullname text not null,
    usn varchar(10) not null, 
    contact varchar(10) not null,
    email varchar(30) not null,
    message text not null
    )
    """
    
cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO FeedBack(fullname, usn, contact, email, message) VALUES (?, ?, ?, ?, ?)"
cursor.execute(cmd, ('RAHUL', '23ad032', '6364674021', 'rahul.23ad032@sode-edu.in', 'just learning'))

cursor.execute(cmd, ('SANJAY', '23ad038', '9651222222', 'sanjay.23ad038@sode-edu.in', 'have fun'))
cursor.execute("DELETE FROM Student")


connection.commit()

f=cursor.execute("select * from FeedBack").fetchall()
print(f)

# r=cursor.execute("select * from FeedBack where usn=?",('23ad032',)).fetchall()
# print(r)
connection.close()