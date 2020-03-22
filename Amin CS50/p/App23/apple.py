# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:07:18 2020

@author: Amin
"""
import datetime

from flask import Flask, render_template

app=Flask(__name__)

app.static_folder = 'static'
time=datetime.date.today()

@app.route("/")
def index():
    var2="Salaaam"
    return render_template("index.html",var1=var2, var3="Amin")
@app.route("/david")
def david():
    return "Hello david"
@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return render_template("index.html",var1=name)
#