# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 06:50:58 2019

@author: cfitz662
"""
from flask import Flask, render_template

class_roster=[("Claude","C","Sophmore"),
        ("Dimitri","B","Senior"),
        ("Dorothea","C","Freshman"),
        ("Hilda","D","Junior"),
        ("Hubert","A","Senior"),
        ("Caspar","C","Sophomore"),
        ("Chris","B","Junior")]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student>")
def welcome(student):
    return render_template("welcome.html", student=student)


@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", grade_view=grade_view, class_roster=class_roster)