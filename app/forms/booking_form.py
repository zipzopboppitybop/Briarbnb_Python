from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateTimeField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from app.models import Booking

class BookingForm(FlaskForm):
    owner_id = IntegerField('owner_id')
    spot_id = IntegerField('spot_id')
    start_date = DateTimeField('start_date', validators=[DataRequired()])
    end_date = DateTimeField('end_date', validators=[DataRequired()])