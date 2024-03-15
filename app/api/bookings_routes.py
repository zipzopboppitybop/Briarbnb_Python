from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import User, db, Spot, Booking
from app.forms import SpotForm, BookingForm

booking_routes = Blueprint('bookings', __name__)

@booking_routes.route('/<id>/delete', methods=['DELETE'])
@login_required
def delete_booking(id):
    """
    Delete a Booking
    """
    user = current_user.to_dict()
    booking = Booking.query.get(id)

    if booking is None:
        return {'errors': 'Booking does not exist'}, 404

    if user['id'] != booking.owner_id:
        return {'errors': 'You do not have permission to delete this Booking!'}, 403

    db.session.delete(booking)
    db.session.commit()
    return {'message': 'Booking deleted successfully'}
