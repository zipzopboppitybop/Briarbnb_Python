from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Spot, User, db
from app.forms import SpotForm

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