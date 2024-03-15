from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import Review, User, db, Spot
from app.forms import SpotForm

review_routes = Blueprint('reviews', __name__)