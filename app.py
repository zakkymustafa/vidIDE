from flask import Flask, render_template, request
import redis
import time
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)
#Extra protection
app.secret_key = os.getenv('SECRET_KEY')

#Database details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
    return render_template("signup.html")    


@app.route('/signin')
def signin():
    return render_template("signin.html")


# @app.route('/signout')



# @app.route('/join')


# @app.route('/host')


# @app.route('/codeIDE')




    


if __name__ == "__main__":
    app.run(debug=True)