from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Review, User, db, Spot
from app.forms import SpotForm

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/<id>/delete', methods=['DELETE'])
@login_required
def delete_review(id):
    """
    Delete a Review
    """
    user = current_user.to_dict()
    review = Review.query.get(id)

    if review is None:
        return {'errors': 'Review does not exist'}, 404

    if user['id'] != review.owner_id:
        return {'errors': 'You do not have permission to delete this Review!'}, 403

    db.session.delete(review)
    db.session.commit()
    return {'message': 'Review deleted successfully'}