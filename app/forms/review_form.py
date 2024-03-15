from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from app.models import Review

class ReviewForm(FlaskForm):
    owner_id = IntegerField('owner_id')
    spot_id = IntegerField('spot_id')
    review = StringField('review', validators=[DataRequired()])
    stars = IntegerField('stars', validators=[DataRequired(), NumberRange(min=1, max=5, message="Stars must be between 1 and 5.")])