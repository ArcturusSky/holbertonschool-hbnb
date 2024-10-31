from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

# Define the namespace for amenities operations
amenity_api = Namespace('amenities', description='Amenity operations')

facade = HBnBFacade()

# Define the amenity model for input validation and documentation
amenity_model = amenity_api.model('Amenity', {
    'title': fields.String(required=True, title='Name of the amenity')
})

@amenity_api.route('/')
class AmenityList(Resource):
    @amenity_api.expect(amenity_model)
    @amenity_api.response(201, 'Amenity successfully created')
    @amenity_api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""

        amenity_data = amenity_api.payload

        # Validate required fields
        required_field = ['title']
        if any(field not in amenity_data for field in required_field):
            return {'error': f'Missing fields: {", ".join(required_field)}'}, 400

        # Create new amenity
        new_amenity = facade.create_amenity(amenity_data)

        return {
            'title': new_amenity.title,
            'amenity_id': new_amenity.id  # Correction de 'aminity_id' à 'amenity_id'
        }, 201


@amenity_api.route('/all_amenities')
class ShowAllAmenities(Resource):
    @amenity_api.response(200, 'List of amenities retrieved successfully')
    @amenity_api.response(404, 'Amenities not found')
    def get(self):
        """Retrieve a list of all amenities"""
        
        all_amenities = facade.get_all_amenities()
        
        if not all_amenities:
            return {'error': 'No amenity found'}, 404

        amenities_data = [
            {
                'id': amenity.id,
                'title': amenity.title,
            }
            for amenity in all_amenities
        ]
        return amenities_data, 200

@amenity_api.route('/<amenity_id>')
class AmenityResource(Resource):
    @amenity_api.response(200, 'Amenity details retrieved successfully')
    @amenity_api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            return {'error': 'amenity not found'}, 404

        return {
            'id': amenity.id,
            'title': amenity.title,
        }, 200

    @amenity_api.expect(amenity_model)
    @amenity_api.response(200, 'Amenity updated successfully')
    @amenity_api.response(404, 'Amenity not found')
    @amenity_api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        
        # check if amenity exist
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            return {'error': 'amenity not found'}, 404

        # Retrieve payload data
        amenity_data = amenity_api.payload
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)

        # Check if update failed
        if updated_amenity is None:
            return {'error': 'Update failed'}, 400
        
        return updated_amenity, 200    