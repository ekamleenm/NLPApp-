from flask import Flask, render_template, request
from db import Database

app = Flask(__name__)

dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_regis', methods=['post'])
def perform_regis():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    passw = request.form.get('user_password')
    response = dbo.insert(name, email, passw)
    if response == 1:
        return "registration successful!"
    else:
        return "email already exists"


app.run(debug=True)
