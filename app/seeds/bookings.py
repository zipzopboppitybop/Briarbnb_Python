from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
import datetime


# Adds a demo user, you can add other users here if you want
def seed_bookings():
    booking1 = Booking(
        owner_id=1, 
        spot_id=3,
        start_date=datetime.datetime(2020, 5, 17),
        end_date=datetime.datetime(2020, 5, 18)
    )
    booking2 = Booking(
        owner_id=2, 
        spot_id=1,
        start_date=datetime.datetime(2020, 5, 17),
        end_date=datetime.datetime(2020, 5, 18)
    )
    booking3 = Booking(
        owner_id=3, 
        spot_id=2,
        start_date=datetime.datetime(2020, 5, 17),
        end_date=datetime.datetime(2020, 5, 18)
    )
    
    db.session.add(booking1)
    db.session.add(booking2)
    db.session.add(booking3)
    db.session.commit()

def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))
        
    db.session.commit()