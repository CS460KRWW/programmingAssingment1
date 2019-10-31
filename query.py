from codebase import db


"""make the business table"""
class Business(db.Model):
	business_id = db.Column(db.String(120), primary_key=True, nullable=False)
	active = db.Column(db.String(32))
	categories = db.Column(db.String(32))
	review_count = db.Column(db.Integer)
	business_name = db.Column(db.String(120))
	stars = db.Column(db.REAL)

	def __init__(self, business_id, active, categories, review_count, business_name, stars):
		self.business_id = business_id
		self.active = active
		self.categories = categories
		self.review_count = review_count
		self.business_name = business_name
		self.stars = stars

	def __repr__(self):
		return "<Business %r>" % self.business_id

"""make the checkin table"""
class Checkin(db.Model):
	business_id = db.Column(db.String(120), primary_key=True, nullable=False)
	Friday = db.Column(db.Integer)

	def __init__(self, business_id, Friday):
		self.business_id = business_id
		self.Friday = Friday

	def __repr__(self):
		return "<checkin %r>" % self.business_id

"""make the review table"""
class Review(db.Model):
	review_id = db.Column(db.String(32), primary_key=True, nullable=False)
	business_id = db.Column(db.String(32))
	user_id = db.Column(db.String(32))
	stars = db.Column(db.Integer)
	review_text = db.Column(db.String(1270))

	def __init__(self, review_id, business_id, user_id, stars, review_text):
		self.review_id = review_id
		self.business_id = business_id
		self.user_id = user_id
		self.stars = stars
		self.review_text = review_text

	def __repr__(self):
		return "<Review %r>" % self.review_id

"""make the user table"""
class User(db.Model):
	user_id = db.Column(db.String(32), primary_key=True, nullable=False)
	name = db.Column(db.String(32))
	review_count = db.Column(db.Integer)

	def __init__(self, user_id, name, review_count):
		self.user_id = user_id
		self.name = name
		self.review_count = review_count

	def __repr__(self):
		return "<user %r>" % self.user_id





