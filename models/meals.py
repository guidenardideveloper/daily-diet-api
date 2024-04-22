from database import db

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_meal = db.Column(db.String(50), nullable=False, unique=True)
    description_meal = db.Column(db.Text(), nullable=True)
    date = db.Column(db.Date(), nullable=False)
    hour = db.Column(db.Time(), nullable=False)
    in_the_diet = db.Column(db.String(3), default='Yes')