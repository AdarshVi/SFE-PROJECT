from flask import Flask, render_template, request, redirect, session
import mysql.connector  # type: ignore
import sys
import os


app = Flask(__name__)
app.secret_key=os.urandom(24) 

try:
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database= "Sfe_project")

    curser = conn.cursor()
except:
    print("Error")
    sys.exit()
else:
    print("Connected")

# get/post
# post:- the data reciverd by the html formate in the form of post by using url
# get:- the 

@app.route('/')
def login():
    return render_template('index.html')


@app.route('/ScrapRate')
def register():
    return render_template('ScrapRate.html')