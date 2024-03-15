from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateTimeField, DateField
from wtforms.validators import DataRequired, ValidationError, NumberRange
from app.models import Booking

class BookingForm(FlaskForm):
    owner_id = IntegerField('owner_id')
    spot_id = IntegerField('spot_id')
    start_date = DateField('start_date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('end_date', format='%Y-%m-%d', validators=[DataRequired()])