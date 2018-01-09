from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ["GET"])
def index():
    return render_template('home.html')


@app.route("/validate", methods = ["POST", "GET"])
def validate():
    username = request.form["username"]
    username_error = ""
    password = request.form["password"]
    password_error = ""
    verify = request.form["verify"]
    verify_error = ""
    email = request.form["email"]
    email_error = ""

    if len(username) < 3:
        username_error = "Username must be 3 or more characters"
    elif len(username) > 20:
        username_error = "Username must be less than 20 characters"
    elif " " in username:
        username_error = "No spaces are allowed in username"
    else:
        username_error = ""

    if len(password) < 3:
        password_error = "Password must be 3 or more characters"
    elif len(password) > 20:
        password_error = "Password must be less than 20 characters"
    elif " " in password:
        password_error = "No spaces are allowed in password"
    else:
        password_error = ""

    if password != verify:
        verify_error = "Passwords does not match"

    if email != "":
        if "." not in email or "@" not in email or " " in email:
            email_error = "Please enter a valid email"
        elif len(email) < 3:
            email_error = "Email cant be less than 3 characters"
        elif len(email) > 20:
            email_error = "Email cant be greater than 20 characters"
    else:
        email_error = ""

    if username_error or password_error or verify_error or email_error:
        return render_template("home.html", username = username, username_error = username_error, password_error = password_error, verify_error = verify_error, email = email, email_error = email_error)
    else:
        return render_template("welcome.html", username=username)


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)

app.run()