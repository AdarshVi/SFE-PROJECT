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
def index():
    return render_template('index.html')


@app.route('/ScrapRate')
def scraprate():
    return render_template('ScrapRate.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')
@app.route('/')
def home():
    if'User_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')
    





if __name__ == "__main__":
    app.run(debug = True)