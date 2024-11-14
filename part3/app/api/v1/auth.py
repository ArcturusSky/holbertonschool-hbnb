from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.api.v1.instance_facade import facade

login_api = Namespace('login', description='Authentication operations')

# Model for input validation
login_model = login_api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@login_api.route('/')
class Login(Resource):
    @login_api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = login_api.payload  # Get the email and password from the request payload
        password = credentials["password"]

        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_attribute(email=credentials["email"])
        
        # Step 2: Check if the user exists and the password is correct
        # Étape de vérification du mot de passe
        if not user or not user.verify_password(password):
            return {'error': 'Invalid credentials'}, 401


        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200
    
@login_api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """
        Protected endpoint requiring valid JWT token
        """
        current_user = get_jwt_identity() # Fetch identity of user
        return {'message': f'Hello, user {current_user["id"]}'}, 200