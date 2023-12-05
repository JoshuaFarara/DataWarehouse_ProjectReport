from dotenv import load_dotenv
import os
import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from database import load_dim_from_db, load_dim_degree_from_db, load_dim_gparanks_from_db, get_table_names
from sqlalchemy import text
from sqlalchemy import MetaData

# import mysql.connector
from sqlalchemy import create_engine, inspect


app = Flask(__name__)


# Pages
@app.route("/dashboard", methods=['POST'])
@app.route("/")
def dashboard():
    if request.method == 'POST':
    
        rollUp = request.form.get('rollUp')
        rollUpDimension = request.form.get('rollUpDimension')
        dimFootsteps1 = request.form.get('dimFootsteps1')
        dimFootsteps2 = request.form.get('dimFootsteps2')

        rollDown = request.form.get('rollDown')
        rollDownDimension = request.form.get('rollDownDimension')
        dimSteps1 = request.form.get('dimSteps1')
        dimSteps2 = request.form.get('dimSteps2')

    
    
        roll_up_data = None
        roll_down_data = None

        responses = []
        
        if rollUp:
            roll_up_data =  {
                'selectedOLAP': rollUp,
                'selected_dimension': rollUpDimension, 
                'selected_footsteps': [dimFootsteps1, dimFootsteps2]
            }
            responses.append(roll_up_data)

        if rollDown:  # Check if the Roll Down section is submitted
            roll_down_data = {
                'selectedOLAP': rollDown,
                'selected_dimension': rollDownDimension,
                'selected_footsteps': [dimSteps1, dimSteps2]
            }
            responses.append(roll_down_data)

        return jsonify(responses)
    else:
        return render_template('dashboard.html')
    # return render_template('dashboard.html')

@app.route("/oldhome")
def home():
    return render_template('oldhome.html', 
                            majors=MAJORS)


@app.route("/api/dimensions")
def list_dimensions():
    footsteps = load_dim_from_db()
    return jsonify(footsteps)

@app.route("/olap")
def olap():
    footsteps = load_dim_from_db()
    degree_footsteps = load_dim_degree_from_db()
    gparanks_footsteps = load_dim_gparanks_from_db()
    table_names = get_table_names()
    return render_template('olap.html',
                           footsteps=footsteps,
                           table_names=table_names,
                           degree_footsteps=degree_footsteps,
                           gparanks_footsteps=gparanks_footsteps)

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