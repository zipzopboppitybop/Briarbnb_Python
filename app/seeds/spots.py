from app.models import db, Spot, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_spots():
    spot1 = Spot(
        name='Dollar General', 
        owner_id=1, 
        address='406 University Dr TX 77445', 
        city='Prairie View', 
        state='Texas', 
        country='United States', 
        lat=30.0915,
        lng=-95.9863, 
        description='Dollar General is proud to be America’s neighborhood general store. We strive to make shopping hassle-free and affordable with more than 15,000 convenient, easy-to-shop stores.', 
        price=1.00)
    spot2 = Spot(
        name='Lakefront Luxury Villa', 
        owner_id=2, 
        address='1470 Willows End', 
        city='Alexander City', 
        state='Alabama', 
        country='United States', 
        lat=32.794300,
        lng=-85.990580, 
        description='Grand and sophisticated villa on peninsula at Lake Martin. Winding staircase, limestone and marble floors, two story windows, stylish details at every turn. Gourmet kitchen, two bar areas. Formal dining room. Make memories in the billiard area, swim and sun on the expansive pool deck. Three docks and a beach. Forget your worries in this spacious and serene space. Sleeps 18.', 
        price=1570.00)
    spot3 = Spot(
        name='French Quarter Inn - Views - Spa tub Sleeps 27', 
        owner_id=3, 
        address='123 Main Street', 
        city='Mentone,', 
        state='Alabama', 
        country='United States', 
        lat=30.0915,
        lng=-95.9863, 
        description='The French Quarter Inn is refinement, beauty and total luxury! New Orleans charm and style atop the mountain offers long range mountain views, stunning sunsets and a sunken mini pool. 6 bedrooms and 4.5 baths sleeps up to 27 guests. The spacious and open family area has a gourmet kitchen, plenty of dining and lounging areas. Outdoor spaces include an oversize screen porch with a fireplace and swing bed, outside fireplace courtyard. Optional fee of $45 per night to heat the mini pool, inquire', 
        price=581.00)

    db.session.add(spot1)
    db.session.add(spot2)
    db.session.add(spot3)
    db.session.commit()

def undo_spots():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.spots RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM spots"))
        
    db.session.commit()