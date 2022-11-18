#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import json

app = Flask(__name__)

## landing page
@app.route("/") # users can land at '/' 
def homepage():
    return render_template('homepage.html')

@app.route("/colon") # or user can land at "/start"
def colon():
    return render_template("colon.html") # look for templates/colon.html
# This is where colon.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/lung") 
def lung():
    return render_template("lung.html") # look for templates/lung.html
# This is where lung.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/bone") # or user can land at "/start"
def bone():
    return render_template("bone.html") # look for templates/bone.html
# This is where bone.html POSTs data to
# A user could also browser (GET) to this location


@app.route("/diagnosis", methods = ["POST", "GET"])
def diagnosis( data = {"dx": None, "stage": None, "age_cat": None, "priorMed": None}):
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        data = request.form
        return render_template('diagnosis.html', newDxInfo=data)
    return json.dumps(data)

@app.route("/newDiagnosis")
def newdiagnosis():
        return render_template('newDiagnosis.html')

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application




