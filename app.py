from flask import Flask, render_template, request, redirect
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
        return render_template('login.html', message='Registration successful! Now Login ⤵')
    else:
        return render_template('register.html', message='Email already exists try again ⤵')


@app.route("/perform_login", methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email, password)
    if response == 1:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Credentials, Try Again ⤵')


@app.route('/profile')
def profile():
    return render_template('profile.html', message='Welcome')


@app.route('/ner')
def ner():
    return "NER is here"


app.run(debug=True)
