import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from database import engine
from sqlalchemy import text
from sqlalchemy import MetaData

# import mysql.connector
from sqlalchemy import create_engine, inspect



app = Flask(__name__)
#add database


#ADD MySQLDatabase
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysq+pymysql:///root:.1038368@localhost/my_datawarehouse'
# app.config['SECRET_KEY'] = 'secretkey'
# app.secret_key = "datawarehouse"
# app.permanent_session_lifetime = timedelta(minutes=5)

# db = SQLAlchemy(app)
# #creat model
# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), nullable=False, unique=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

#     #creat a string
#     def __repr__(self):
#         return '<Name %r>' % self.name
# db_connection_string = "mysql+pymysql://wh1x4lqjob1xuh5upzsr:pscale_pw_5HhQMULzDzBZRI2LdRwWkIicybXkSjGUwk6v5eJtsNq@aws.connect.psdb.cloud/fararadatawarehouse?charset=utf8mb4"

# engine = create_engine(
#     db_connection_string,
#     connect_args={
#        "ssl": {
#            "ssl_cert": "/etc/ssl/cert.pem"                               
#         }
#     }
# )

def load_dim_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from test"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        footsteps = []
        for row in result.fetchall():
            footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries

        return footsteps
    
def get_table_names():
    inspector = inspect(engine)
    return inspector.get_table_names()



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
    footsteps = load_dim_from_db()
    table_names = get_table_names()
    return render_template('olap.html',
                           majors=MAJORS,
                           olap_commands=OLAP_COMMANDS,
                           footsteps=footsteps,
                           table_names=table_names)

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

# DIMENSIONS = [
#     {
#         'dim_id': 1,
#         'dim_name' : 'Dim College'
#     },
#     {
#         'dim_id': 2,
#         'dim_name' : 'Dim Degree'
#     },
#     {
#         'dim_id': 3,
#         'dim_name' : 'Dim College'
#     },
#     {
#         'dim_id': 4,
#         'dim_name' : 'Dim Year'
#     },
#     {
#         'dim_id': 5,
#         'dim_name' : 'Dim Semester'
#     },
#     {
#         'dim_id': 6,
#         'dim_name' : 'Dim Status'
#     },
#     {
#         'dim_id': 7,
#         'dim_name' : 'Dim GPARAnk'
#     },
# ]

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



if __name__ == '__main__':
    app.run(debug=True)