# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:07:18 2020

@author: Amin
"""
import datetime

from flask import Flask, render_template, request

app=Flask(__name__)

app.static_folder = 'static'
time=datetime.datetime.now()
month=time.month
year=time.year
day=time.day
new_year= day==1 and month==1
names={"Amin", "Reza", "Amir"}
var2="Salaaam"
@app.route("/")
def index():
    return render_template("index.html",var1=var2, var3=year, var4=month, var5=day, new_year=new_year, names=names)
@app.route("/more")
def more():
    return render_template("more.html",var1=var2, var3=year, var4=month, var5=day, new_year=new_year, names=names)
@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return render_template("index.html",var1=name)
@app.route("/chakh", methods=["GET"])
def chakh():
    name=request.args.get("name")
#    name=name.capitalize()
    return render_template("index.html",name=name)

