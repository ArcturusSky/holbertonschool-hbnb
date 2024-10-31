from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

# Define the namespace for place operations
place_api = Namespace('places', description='Place operations')

facade = HBnBFacade()

# Define the models for related entities
amenity_model = place_api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = place_api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = place_api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@place_api.route('/')
class PlaceList(Resource):
    @place_api.expect(place_model)
    @place_api.response(201, 'Place successfully created')
    @place_api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = place_api.payload

        # Validate required fields
        required_fields = ['title', 'price', 'latitude', 'longitude', 'owner_id']
        missing_fields = [field for field in required_fields if field not in place_data]
        if missing_fields:
            return {'error': f'Missing fields: {", ".join(missing_fields)}'}, 400

        # Validate owner existence
        owner = facade.get_user_by_id(place_data['owner_id'])
        if not owner:
            return {'error': 'Owner not found'}, 400

        # Validate each amenity ID
        invalid_amenities = [amenity_id for amenity_id in place_data['amenities'] 
                             if not facade.get_amenity_by_id(amenity_id)]
        if invalid_amenities:
            return {'error': f'Invalid amenities: {", ".join(invalid_amenities)}'}, 400

        # Create new place
        new_place = facade.create_place(place_data)

        return {
            'title': new_place.title,
            'place_id': new_place.id,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner': {
                'id': owner.id,
                'first_name': owner.first_name,
                'last_name': owner.last_name,
                'email': owner.email
            },
            'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in new_place.amenities]
        }, 201

@place_api.route('/all_places')
class ShowAllPlaces(Resource):
    @place_api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        all_places = facade.get_all_places()

        if not all_places:
            return {'error': 'No places found'}, 404

        places_data = [
            {
                'title': place.title,
                'place_id': place.id,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': {
                    'id': place.owner.id,
                    'first_name': place.owner.first_name,
                    'last_name': place.owner.last_name,
                    'email': place.owner.email
                },
                'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in place.amenities]
            }
            for place in all_places
        ]
        return places_data, 200

@place_api.route('/<place_id>')
class PlaceResource(Resource):
    @place_api.response(200, 'Place details retrieved successfully')
    @place_api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in place.amenities]
        }, 200

    @place_api.expect(place_model)
    @place_api.response(200, 'Place updated successfully')
    @place_api.response(404, 'Place not found')
    @place_api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Check if place exists
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        # Retrieve and validate payload data
        place_data = place_api.payload
        if 'owner_id' in place_data:
            owner = facade.get_user_by_id(place_data['owner_id'])
            if not owner:
                return {'error': 'Owner not found'}, 400

        if 'amenities' in place_data:
            invalid_amenities = [amenity_id for amenity_id in place_data['amenities'] 
                                 if not facade.get_amenity_by_id(amenity_id)]
            if invalid_amenities:
                return {'error': f'Invalid amenities: {", ".join(invalid_amenities)}'}, 400

        # Update place
        updated_place = facade.update_place(place_id, place_data)
        if not updated_place:
            return {'error': 'Update failed'}, 400

        return {
            'id': updated_place.id,
            'title': updated_place.title,
            'description': updated_place.description,
            'price': updated_place.price,
            'latitude': updated_place.latitude,
            'longitude': updated_place.longitude,
            'owner': {
                'id': updated_place.owner.id,
                'first_name': updated_place.owner.first_name,
                'last_name': updated_place.owner.last_name,
                'email': updated_place.owner.email
            },
            'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in updated_place.amenities]
        }, 200
