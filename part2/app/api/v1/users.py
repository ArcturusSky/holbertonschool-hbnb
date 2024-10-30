from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.models.PseudoDataBase import all_users
from flask import jsonify

# Define the namespace (aka the "box" holding all the routes of user here)
user_api = Namespace('users', description='User operations')

facade = HBnBFacade()
# Define the user model for input validation and documentation in the given namespace
user_model = user_api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'username': fields.String(required=True, description='Username of the user'),
    'password': fields.String(required=True, description='Password of the user'),  # Will have to be hashed at some point
    'email': fields.String(required=True, description='Email of the user'),
    'localisation': fields.String(required=False, description='Location of the user'),
    'phone_number': fields.String(required=True, description='Phone number of the user'),
    'user_id': fields.String(required=False, description='Id of the User'),
    'is_admin': fields.Boolean(required=False, description='Admin status of the user', default=False)
})

@user_api.route('/')
class UserList(Resource):
    """Resource for handling operations related to creating and listing users"""

    @user_api.expect(user_model, validate=True)
    @user_api.response(201, 'User successfully created')
    @user_api.response(400, 'Email already registered')
    @user_api.response(400, 'Username already registered')
    @user_api.response(400, 'Invalid input data')
    # `marshal` is used to serialize user_model into JSON format to return it at the end
    @user_api.marshal_list_with(user_model)
    def post(self):
        """
        Register a new user.
        
        This endpoint allows creating a new user. The request payload must contain
        'first_name', 'last_name', 'username', 'password', and 'email'. Optional fields include
        'localisation', 'phone_number', and 'is_admin'.
        
        Returns:
            JSON object containing the new user's details (without password).
        """
        user_data = user_api.payload

        # Check if email is already in use
        existing_user_email = facade.get_user_by_attribute(email=user_data['email'])
        if existing_user_email:
            return {'error': 'Email already taken'}, 400
        # Check if username is already in use
        existing_user_username = facade.get_user_by_attribute(username=user_data['username'])
        if existing_user_username:
            return {'error': 'Username already registered'}, 400

        # Create new user and add their data in users global dict
        new_user = facade.create_user(user_data)
        all_users.append(new_user)
        return {
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'username': new_user.username,
            'email': new_user.email,
            'localisation': new_user.localisation,
            'phone_number': new_user.phone_number,
            'user_id': new_user.id,
            'is_admin': new_user.is_admin,
        }, 200

@user_api.route('/<user_id>')
class UserResource(Resource):
    """Resource for handling operations related to a specific user"""

    @user_api.response(200, 'User details retrieved successfully')
    @user_api.response(400, 'error: Invalid input data')
    @user_api.response(404, 'User not found')
    def get(self, user_id):
        """
        Get user details by user ID.
        
        This method retrieves the details of a user identified by their unique ID and DISPLAY them in the HTML response.
        
        Args:
            user_id (str): The unique identifier of the user.
        
        Returns:
            JSON object containing the user's details if found, otherwise a 404 error.
        """
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'localisation': user.localisation,
            'phone_number': user.phone_number,
            'is_admin': user.is_admin,
        }, 200
    
    def put(self, user_id):
        """
        Update user details by user ID.
        
        This method allows updating the details of an existing user.
        
        Args:
            user_id (str): The unique identifier of the user.
        
        Returns:
            JSON object containing the updated user's details.
        """
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        user_data = user_api.payload
        updated_user = facade.update_user(user_id, user_data)

        if not updated_user:
            return 400
        return jsonify(updated_user), 200

    
@user_api.route('/all_users')
class ShowAllUsers(Resource):
    """
    Resource for showing all users.
    """
    @user_api.response(200, 'User details retrieved successfully')
    def get_all_users(self):
        """
        Function that returns the entire users dictionary as JSON.
        """
        return jsonify(all_users), 200
