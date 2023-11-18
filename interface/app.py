from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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
                           majors=MAJORS)
 
if __name__ == '__main__':
    app.run(debug=True)