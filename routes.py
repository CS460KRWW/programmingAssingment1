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
@app.route("/show_business", methods = ['GET', 'POST'])
def show_business():
	if (request.method == "POST"):
	#form to add a new business
		newBusiness = Business(request.form['business_id'],request.form['active'],request.form['categories'],request.form['review_count'],request.form['business_name'],request.form['stars'])
	#db commands
		db.session.add(newBusiness)
		db.session.commit()
		return redirect(url_for('show_business'))
	allBusiness = Business.query.all()
	return render_template('business.html', allBusiness = allBusiness)

#delete business route
@app.route('/delete_business/<string:id>', methods=['POST'])
def delete_business(id):
	temp = Business.query.get(id)
	db.session.delete(temp)
	db.session.commit()
	flash('Data Deleted', 'success')
	return redirect(url_for('show_business'))






