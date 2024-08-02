#!/bin/python3

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return render_template("index.html", name=name)
