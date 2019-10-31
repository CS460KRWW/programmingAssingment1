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