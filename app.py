from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
# from database import engine
from sqlalchemy import text
import mysql.connector
from sqlalchemy import create_engine, text


app = Flask(__name__)

app.secret_key = "datawarehouse"
app.permanent_session_lifetime = timedelta(minutes=5)

try:
    mydb = mysql.connector.connect(
        host="aws.connect.psdb.cloud",
        user="i8eui9t5t23dkw5va23d",
        password="pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55"
    )
    print("Connection established")
    cursor = mydb.cursor()
    cursor.execute("create database if not exists fararadatawarehouse")
    mydb.commit()
    print("Database created successfully")
    cursor.execute("use fararadatawarehouse")
    print("using fararadatawarehouse")

except mysql.connector.Error as err:
    print("An error occurred:", err)

# database = 'fararadatawarehouse'
# hostname = 'aws.connect.psdb.cloud'
# username = 'i8eui9t5t23dkw5va23d'
# password = 'pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55'

# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))
# engine = create_engine("mysql+mysqldb://root:pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55@aws.connect.psdb.cloud/fararadatawarehouse")
db_connection_string = "mysql+pymysql://i8eui9t5t23dkw5va23d:pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55@aws.connect.psdb.cloud/fararadatawarehouse?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
       "ssl": {
           "ssl_cert": "/etc/ssl/cert.pem"                               
        }
    }
)

# with engine.connect() as conn:
#         result = conn.execute(text("select * from test"))
#         print(result.all())
    #     result_dicts = []
    #     for row in result.all():
    #         result_dicts.append(dict(row._mapping))

    # print(result_dicts)


def load_dimensions_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from test"))
        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(row._mapping))

    print(result_dicts)



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