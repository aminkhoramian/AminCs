# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:07:18 2020

@author: Amin
"""

from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
     return "Hello, world!"