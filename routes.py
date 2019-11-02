import os
from flask import render_template, url_for, flash, redirect, request, abort
#from __init__
from . import app, db
#import query calls
from .query import *



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
	if ((request.method == "POST") and (request.form['Friday'] == 'Friday')):
		#form to add a new checkin
		business = request.form['business_id']

		# if existing business, update it
		if (db.session.query(Checkin.business_id).filter_by(business_id = business).scalar() is not None):
			Checkin.query.filter_by(business_id=business).update({Checkin.Friday: Checkin.Friday+1})

		# else new business in Checkin
		else:
			newCheckin = Checkin(request.form['business_id'],1)
			db.session.add(newCheckin)
		#db commands
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

	lookup = {t : "Customized Query",
	"select u.name from User u where u.review_count > 0;": "Display all users that have at least 1 review.",
	"select u.name from User u where u.review_count <= 2;" : "Display the name of the users that have made 2 reviews or less.",
	"select b.business_name from Business b where b.active = 'FALSE';" : "Display all inactive businesses.",
	"select b.business_name from Business b where b.business_name like '%pizza%';": "Display the names of all pizza restaurants that have a rating of 4 stars or above.",
	"select count(*) from Checkin c, Business b where b.business_id = c.business_id and c.Friday > 0;":"Display the number of stores that had at least one check-in on Friday.",
	"select r.review_text from Business b, Review r where b.business_id = r.business_id and b.business_name like 'Arcadia Tavern';" : "Display the text of all reviews made for the Arcadia Tavern.",
	"select distinct b.business_name from Business b, Review r where b.business_id = r.business_id and r.stars < 3;" : "Display the names of the restaurants that have taken at least one 1-star or 2-star review.",
	"select avg(b.stars), sum(b.review_count) from Business b where b.business_name like 'KFC';":"Display the average rating and total number of reviews of all KFC stores.",
	"select b.business_id from Business b order by b.review_count desc limit 10;":"Display a list of the ids of the top 10 stores in terms of the number of reviews they have received.",
	"select u.name from User u order by u.review_count desc limit 1;": "Display the name of the user that has made the most reviews."}

	#making the sqlquery with sqlalchemy
	q = db.engine.execute(t)

	return render_template('output.html', sqlq = q, name = lookup[t])








