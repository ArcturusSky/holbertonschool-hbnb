from flask import Blueprint
from flask_restx import Api

# Create a Blueprint for the API with a specific URL prefix
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Initialize the API object, defining version and basic metadata
api = Api(api_bp, version='1.0', title="HBnB API", description="API for HBnB project")

# Import the user namespace for handling user-related operations
from .v1.users import user_api as user_namespace

    # ////////// Import other namespaces as needed for different resources //////////
# from .v1.places import place_api as place_namespace
# from .v1.reviews import review_api as review_namespace
# from .v1.amenities import amenity_api as amenity_namespace

# Add the user namespace to the API, defining its URL path
api.add_namespace(user_namespace, path='/users')

    # ////////// Add other namespaces to the API for different resource paths //////////
# api.add_namespace(places_namespace, path='/places')
# api.add_namespace(reviews_namespace, path='/reviews')
# api.add_namespace(amenities_namespace, path='/amenities')
