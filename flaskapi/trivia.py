#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template 

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start(): 
    return render_template("postmaker.html")

@app.route("/login", methods =[POST", "GET"]):
    if request.method =="POST":
    #the request method by teh client is a post 



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
