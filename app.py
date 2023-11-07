from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
 
# https://hevodata.com/learn/flask-mysql/ 