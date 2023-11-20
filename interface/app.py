from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "datawarehouse"
app.permanent_session_lifetime = timedelta(minutes=5)

MAJORS = [
    {
        'major_id': 1,
        'major_name':'Computer Sc'
    },
    {
        'major_id': 2,
        'major_name':'Information Sc'
    },
    {
        'major_id': 3,
        'major_name':'Applied Sc'
    },
    {
        'major_id': 4,
        'major_name':'Accounting'
    }
]

OLAP_COMMANDS = [
    {
        'olap_id': 1,
        'olap_command' : 'Roll Up'
    },
    {
        'olap_id': 2,
        'olap_command' : 'Roll Down'
    },
    {
        'olap_id': 3,
        'olap_command' : 'Dice'
    },
    {
        'olap_id': 4,
        'olap_command' : 'Slice'
    },
    {
        'olap_id': 5,
        'olap_command' : 'Pivot'
    },
]

DIMENSIONS = [
    {
        'dim_id': 1,
        'dim_name' : 'Dim College'
    },
    {
        'dim_id': 2,
        'dim_name' : 'Dim Degree'
    },
    {
        'dim_id': 3,
        'dim_name' : 'Dim College'
    },
    {
        'dim_id': 4,
        'dim_name' : 'Dim Year'
    },
    {
        'dim_id': 5,
        'dim_name' : 'Dim Semester'
    },
    {
        'dim_id': 6,
        'dim_name' : 'Dim Status'
    },
    {
        'dim_id': 7,
        'dim_name' : 'Dim GPARAnk'
    },
]

@app.route("/dashboard")
@app.route("/")
def dashboard():
    return render_template('dashboard.html', 
                            majors=MAJORS)

@app.route("/oldhome")
def home():
    return render_template('oldhome.html', 
                            majors=MAJORS)

@app.route("/olap")
def olap():
    return render_template('olap.html',
                           majors=MAJORS,
                           olap_commands=OLAP_COMMANDS,
                           dimensions=DIMENSIONS)

@app.route("/login", methods=["POST", "GET"]) # as second parameter add methods that can be used on the page
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        
        return render_template('login.html')


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template('user.html')
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)