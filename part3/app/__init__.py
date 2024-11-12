from flask import Flask
from flask_restx import Api

# Routes/namespaces for each entity
from app.api.v1.users import user_api as user_namespace
from app.api.v1.amenities import amenity_api as amenity_namespace
from app.api.v1.places import place_api as place_namespace
from app.api.v1.reviews import review_api as review_namespace

def create_app(config_class="config.DevelopmentConfig"):
    """
    Fonction that create the app
    
    Args:
        config_class (str): Path to the configuration class to use
                           by default: "config.DevelopmentConfig" since we are in dev currently
    
    Returns:
        Flask: Flask instance configured as wanted
    """

    # Create an instance of Flask
    app = Flask(__name__)

    # Apply config (by default DevelopmentConfig)
    app.config.from_object(config_class)

    # Initialization of the API and its documentation
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(user_namespace, path='/api/v1/users')
    api.add_namespace(amenity_namespace, path='/api/v1/amenities')
    api.add_namespace(place_namespace, path='/api/v1/places')
    api.add_namespace(review_namespace, path='/api/v1/reviews')
    return app