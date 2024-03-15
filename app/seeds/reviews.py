from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
import datetime


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    review1 = Review(
        owner_id=1, 
        spot_id=2,
        startDate=datetime.datetime(2021, 6 ,1),
        endDate=datetime.datetime(2021, 6 ,2),
        review='Great place to park and restock on supplies.',
        stars=5
    )
    review2 = Review(
        owner_id=3, 
        spot_id=2,
        startDate=datetime.datetime(2021, 6 ,1),
        endDate=datetime.datetime(2021, 6 ,2),
        review='Great place to park and restock on supplies.',
        stars=5
    )
    review3 = Review(
        owner_id=2, 
        spot_id=1,
        startDate=datetime.datetime(2021, 6 ,1),
        endDate=datetime.datetime(2021, 6 ,2),
        review='Great place to park and restock on supplies.',
        stars=5
    )
    
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()