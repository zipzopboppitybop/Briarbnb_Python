from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Spot

spot_routes = Blueprint('spots', __name__)


@spot_routes.route('/')
def spots():
    """
    Query for all spots and returns them in a list of spot dictionaries
    """
    spots = Spot.query.all()
    return {'spots': [spot.to_dict() for spot in spots]}

@spot_routes.route('/<id>')
@login_required
def spot(id):
    """
    Query for one spot and return it in a spot dictionary
    """
    spot = Spot.query.get(id)
    return spot.to_dict()

