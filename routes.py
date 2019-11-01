import os
from flask import render_template, url_for, flash, redirect, request, abort
#from __init__
from codebase import app, db
#import query calls
from codebase.query import *



@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	#can potentially query
	if (request.method == "POST"):
		return redirect(url_for('output', code=307))

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
		flash('Data Added', 'success')
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


#display data for checkin table
@app.route("/show_checkin", methods = ['GET', 'POST'])
def show_checkin():
	if (request.method == "POST"):
	#form to add a new business
		newCheckin = Checkin(request.form['business_id'],request.form['Friday'])
	#db commands
		db.session.add(newCheckin)
		db.session.commit()
		flash('Data Added', 'success')
		return redirect(url_for('show_checkin'))
	checkin = Checkin.query.all()
	return render_template('checkin.html', checkin = checkin)

#delete checkin route
@app.route('/delete_checkin/<string:id>', methods=['POST'])
def delete_checkin(id):
	temp = Checkin.query.get(id)
	db.session.delete(temp)
	db.session.commit()
	flash('Data Deleted', 'success')
	return redirect(url_for('show_checkin'))

#display data for review table
@app.route("/show_review", methods = ['GET', 'POST'])
def show_review():
	if (request.method == "POST"):
	#form to add a new business
		newReview = Review(request.form['review_id'],request.form['business_id'],request.form['user_id'],request.form['stars'],request.form['review_text'])
	#db commands
		db.session.add(newReview)
		db.session.commit()
		flash('Data Added', 'success')
		return redirect(url_for('show_review'))
	allReview = Review.query.all()
	return render_template('review.html', allReview = allReview)

#delete review route
@app.route('/delete_review/<string:id>', methods=['POST'])
def delete_review(id):
	temp = Review.query.get(id)
	db.session.delete(temp)
	db.session.commit()
	flash('Data Deleted', 'success')
	return redirect(url_for('show_review'))

#display data for user table
@app.route("/show_user", methods = ['GET', 'POST'])
def show_user():
	if (request.method == "POST"):
	#form to add a new business
		newUser = User(request.form['user_id'],request.form['name'],request.form['review_count'])
	#db commands
		db.session.add(newUser)
		db.session.commit()
		flash('Data Added', 'success')
		return redirect(url_for('show_user'))
	allUser = User.query.all()
	return render_template('user.html', allUser = allUser)

#delete user route
@app.route('/delete_user/<string:id>', methods=['POST'])
def delete_user(id):
	temp = User.query.get(id)
	db.session.delete(temp)
	db.session.commit()
	flash('Data Deleted', 'success')
	return redirect(url_for('show_user'))

@app.route('/output', methods=['GET', 'POST'])
def output():
	t = request.form.get('USERSQL')

	#making the sqlquery with sqlalchemy
	q = db.engine.execute(t)

	return render_template('output.html', sqlq = q)
