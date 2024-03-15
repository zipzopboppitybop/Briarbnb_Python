from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Spot, User, Review, Booking, db
from app.forms import SpotForm, ReviewForm, BookingForm

spot_routes = Blueprint('spots', __name__)


@spot_routes.route('/')
def spots():
    """
    Query for all spots and returns them in a list of spot dictionaries
    """
    spots = Spot.query.all()
    return {'spots': [spot.to_dict() for spot in spots]}

@spot_routes.route('/<id>')
def spot(id):
    """
    Query for one spot and return it in a spot dictionary
    """
    spot = Spot.query.get(id)

    if spot is None:
        return {'errors': 'Spot does not exist'}, 404

    return spot.to_dict()


@spot_routes.route('/create', methods=['POST'])
@login_required
def create_spot():
    """
    Create a spot and return it in a spot dictionary
    """
    user = current_user.to_dict()
    form = SpotForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        spot = Spot(
            name=form.data['name'],
            owner_id=user['id'],
            address=form.data['address'],
            city=form.data['city'],
            state=form.data['state'],
            country=form.data['country'],
            lat=form.data['lat'],
            lng=form.data['lng'],
            description=form.data['description'],
            price=form.data['price']
        )
        db.session.add(spot)
        db.session.commit()
        return spot.to_dict()

    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
    

@spot_routes.route('/<id>/review/create', methods=['POST'])
@login_required
def create_review_on_spot(id):
    """
    Create a review on a spot and return it in a review dictionary
    """
    user = current_user.to_dict()
    spot = Spot.query.get(id)
    form = ReviewForm()

    if spot is None:
        return {'errors': 'Spot does not exist'}, 404
    
    if spot.owner_id == user['id']:
        return {'errors': 'You cannot review your own spot!'}, 403

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            owner_id=user['id'],
            spot_id=spot.id,
            review=form.data['review'],
            stars=form.data['stars']
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()

    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
    

@spot_routes.route('/<id>/booking/create', methods=['POST'])
@login_required
def create_booking_on_spot(id):
    """
    Create a booking on a spot and return it in a booking dictionary
    """
    user = current_user.to_dict()
    spot = Spot.query.get(id)
    form = BookingForm()

    if spot is None:
        return {'errors': 'Spot does not exist'}, 404
    
    if spot.owner_id == user['id']:
        return {'errors': 'You cannot book your own spot!'}, 403

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        booking = Booking(
            owner_id=user['id'],
            spot_id=spot.id,
            start_date=form.data['start_date'],
            end_date=form.data['end_date']
        )
        db.session.add(booking)
        db.session.commit()
        return booking.to_dict()

    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
    

@spot_routes.route('/<id>/edit', methods=['PUT'])
@login_required
def edit_spot(id):
    """
    Edit a spot and return it in a spot dictionary
    """
    user = current_user.to_dict()
    form = SpotForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        spot = Spot.query.get(id)

        if spot is None:
            return {'errors': 'Spot does not exist'}, 404
        
        if user['id'] != spot.owner_id:
            return {'errors': 'You do not have permission to edit this spot!'}, 403

        spot.name = form.data['name']
        spot.address = form.data['address']
        spot.city = form.data['city']
        spot.state = form.data['state']
        spot.country = form.data['country']
        spot.lat = form.data['lat']
        spot.lng = form.data['lng']
        spot.description = form.data['description']
        spot.price = form.data['price']
        db.session.commit()
        return spot.to_dict()

    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
    
@spot_routes.route('/<id>/delete', methods=['DELETE'])
@login_required
def delete_spot(id):
    """
    Delete a Spot 
    """
    user = current_user.to_dict()
    spot = Spot.query.get(id)

    if spot is None:
        return {'errors': 'Spot does not exist'}, 404

    if user['id'] != spot.owner_id:
        return {'errors': 'You do not have permission to delete this spot!'}, 403

    db.session.delete(spot)
    db.session.commit()
    return {'message': 'Spot deleted successfully'}