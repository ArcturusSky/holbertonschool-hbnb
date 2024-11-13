from flask import Blueprint
from flask_restx import Api

# Create a Blueprint for the API with a specific URL prefix
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Initialize the API object, defining version and basic metadata
api = Api(api_bp, version='1.0', title="HBnB API", description="API for HBnB project")

# Import namespace for handling operations
from .v1.users import user_api as user_namespace
from .v1.auth import login_api as login_namespace
from .v1.places import place_api as place_namespace
from .v1.reviews import review_api as review_namespace
from .v1.amenities import amenity_api as amenity_namespace

# Add namespace to the API, defining its URL path
api.add_namespace(user_namespace, path='/users')
api.add_namespace(place_namespace, path='/places')
api.add_namespace(review_namespace, path='/reviews')
api.add_namespace(amenity_namespace, path='/amenities')
api.add_namespace(login_namespace, path='/login')
