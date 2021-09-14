from flask import Flask, render_template, request
import redis
import time
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
from flask_ckeditor import CKEditor
from forms import PostForm




app = Flask(__name__)
ckeditor = CKEditor(app)
#Extra protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# app.secret_key = os.getenv('SECRET_KEY')

#Database details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vid@123'
app.config['MYSQL_DB'] = 'vididedb'




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and "email" in request.form and "password" in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            msg = "Account already exists"
        elif not re.match (r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Invalid email address"
        elif not email or not password:
            msg = "Please fill out the form!"
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (password,email,))
            mysql.connection.commit()
            msg = "You have successfully registered!"

    elif request.method == 'POST':
        msg = "Please fill out the form"

    return render_template("signup.html")    


@app.route('/signin')
def signin():
    if request.method == 'POST' and "email" in request.form and "password" in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()

        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session["email"] = account["email"]
            msg = "Logged in Successfully!"
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect email or password"

    return render_template("signin.html")




# @app.route('/signout')
# def signout():
#     session.pop("loggedin", None)
#     session.pop('id', None)
#     session.pop('email', None)
#     return redirect(url_for('signin')



# @app.route('/join')


# @app.route('/host')



@app.route('/codeIDE')
def codeIDE():
    form = PostForm()
    if request.method == 'POST':
        data = request.form.get('body')  

    return render_template("code.html",form=form)    


if __name__ == "__main__":
    app.run(debug=True)