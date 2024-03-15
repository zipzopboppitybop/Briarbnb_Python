from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Review, User, db, Spot
from app.forms import SpotForm, ReviewForm

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/<id>/edit', methods=['PUT'])
@login_required
def edit_review(id):
    """
    Edit a review and return it in a review dictionary
    """
    user = current_user.to_dict()
    form = ReviewForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review.query.get(id)

        if review is None:
            return {'errors': 'Review does not exist'}, 404
        
        if user['id'] != review.owner_id:
            return {'errors': 'You do not have permission to edit this review!'}, 403

        review.review = form.data['review']
        review.stars = form.data['stars']
        db.session.commit()
        return review.to_dict()

    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
    
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

