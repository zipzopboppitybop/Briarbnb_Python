from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Spot, User, Review, db
from app.forms import SpotForm

review_routes = Blueprint('reviews', __name__)


@review_routes.route('/')
def reviews():
    """
    Query for all reviews and returns them in a list of review dictionaries
    """
    reviews = Review.query.all()
    return {'reviews': [review.to_dict() for review in reviews]}

@review_routes.route('/<id>')
def review(id):
    """
    Query for one review and returns them in a review dictionary
    """
    review = Review.query.get(id)
    return review.to_dict()
