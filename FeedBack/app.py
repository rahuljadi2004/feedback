# from flask import Flask,render_template,request 
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     fullname = request.form.get('fullname')
#     usn= request.form.get('usn')
#     contact= request.form.get('contact')
#     email= request.form.get('email')
#     message= request.form.get('message')
#     return "hello "+ fullname 
    
    
# if __name__ == '__main__':
#     app.run(debug=True)



import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form.get('fullname')
    usn = request.form.get('usn')
    contact = request.form.get('contact')
    email = request.form.get('email')
    message = request.form.get('message')
    
    
    connection=sqlite3.connect('FeedBack.db')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO FeedBack(fullname, usn, contact, email, message) VALUES (?, ?, ?, ?, ?)", 
                   (fullname, usn, contact, email, message))
    connection.commit()
    feedbacks=cursor.execute("SELECT fullname,message,id FROM FeedBack").fetchall()
    connection.close()
    return render_template('success.html', feedbacks=feedbacks,
                           name=fullname)

if __name__ == '__main__':
    app.run(debug=True)
