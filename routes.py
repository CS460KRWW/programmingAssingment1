import os
from flask import render_template, url_for, flash, redirect, request, abort
#from __init__
from codebase import app, db
#import query calls
from codebase.query import *



@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')







