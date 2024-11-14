from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

# Define the namespace for user operations
user_api = Namespace('users', description='User operations')

facade = HBnBFacade()

# Define the user model for input validation and documentation
user_model = user_api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'username': fields.String(required=True, description='Username of the user'),
    'password': fields.String(required=True, description='Password of the user'),  # Should be hashed
    'email': fields.String(required=True, description='Email of the user'),
    'localisation': fields.String(required=False, description='Location of the user'),
    'phone_number': fields.String(required=False, description='Phone number of the user'),
    'user_id': fields.String(required=False, description='Id of the User'),
    'is_admin': fields.Boolean(required=False, description='Admin status of the user', default=False)
})

@user_api.route('/')
class UserList(Resource):
    """Resource for handling operations related to creating and listing users"""

    @user_api.expect(user_model, validate=True)
    @user_api.response(201, 'User successfully created')
    @user_api.response(409, 'Username or email already registered')
    @user_api.response(400, 'Invalid input data')
    @user_api.marshal_list_with(user_model)
    def post(self):
        """Register a new user."""
        user_data = user_api.payload

        # Validate required fields
        required_fields = ['first_name', 'last_name', 'username', 'password', 'email']
        missing_fields = [field for field in required_fields if field not in user_data]

        if missing_fields:
            return {'error': f'Missing fields: {", ".join(missing_fields)}'}, 400

        # Check if username or email already in use
        if facade.get_user_by_email(email=user_data['email']):
            return {'error': 'Email already registered'}, 409
        
        if facade.get_user_by_attribute(username=user_data['username']):
            return {'error': 'Username already registered'}, 409

        # Create new user via the facade (password is already hashed in User class)
        try:
            new_user = facade.create_user(user_data)
        except Exception as e:
            return {'error': str(e)}, 400  # Handle any other error that may occur during user creation
        
        return {
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'username': new_user.username,
            'password': "You really thought I would display the password? Noob.",
            'email': new_user.email,
            'localisation': new_user.localisation,
            'phone_number': new_user.phone_number,
            'user_id': new_user.id,
            'is_admin': new_user.is_admin,
        }, 201


@user_api.route('/<user_id>')
class UserResource(Resource):
    """Resource for handling operations related to a specific user"""

    @user_api.response(200, 'User details retrieved successfully')
    @user_api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by user ID."""
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'password': "You really thought I would display the password? Noob.",
            'email': user.email,
            'localisation': user.localisation,
            'phone_number': user.phone_number,
            'is_admin': user.is_admin,
        }, 200
    
    @user_api.expect(user_model, partial=True)
    @user_api.response(200, 'User successfully updated')
    @user_api.response(404, 'User not found')
    @user_api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user details by user ID."""
        
        # check if user exist
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        # Retrieve payload data
        user_data = user_api.payload
        updated_user = facade.update_user(user_id, user_data)

        # Check if update failed
        if updated_user is None:
            return {'error': 'Update failed'}, 400
        
        return updated_user, 200

@user_api.route('/all')
class ShowAllUsers(Resource):
    """Resource for showing all users."""

    @user_api.response(200, 'User details retrieved successfully')
    @user_api.response(404, 'No users found')
    def get(self):
        """Retrieve all registered users."""
        all_users = facade.get_all_users()
        
        if not all_users:
            return {'error': 'No users found'}, 404

        users_data = [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'password': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                'email': user.email,
                'localisation': user.localisation,
                'phone_number': user.phone_number,
                'is_admin': user.is_admin,
            }
            for user in all_users
        ]
        
        return users_data, 200
