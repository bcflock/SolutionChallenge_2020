from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/user")
def user():
    #test for authentication
    return

@app.route("/about")
def about():
    return render_template('about.html')    

@app.route("/contact")
def contact():
    return render_template('contact.html')