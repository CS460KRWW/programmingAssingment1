import os
from flask import render_template, url_for, flash, redirect, request, abort
#from __init__
from codebase import app, db
#import query calls
from codebase.query import *



@app.route("/")
@app.route("/home")
def home():
	# return render_template('post_business.html')
	return render_template('home.html')


#display data for business table
@app.route("/show_business", methods = ['GET'])
def show_business():
	allBusiness = Business.query.all()
	return render_template('business.html', allBusiness = allBusiness)


#url for adding data to businesses 
# @app.route("/post_business", methods = ['GET', 'POST'])
# def post_business():
# 	newBusiness = Business(request.form.get('business_id'),
# 		request.form.get('active'),request.form.get('categories'),
# 		request.form.get('review_count'),request.form.get('business_name'),
# 		request.form.get('stars'))
# 	db.session.add(newBusiness)
# 	db.session.commit()
# 	return redirect(url_for('/'))







