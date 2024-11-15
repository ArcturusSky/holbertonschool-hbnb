from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.validation_checks import (
    name_length_validation50,
    username_validation,
    email_validation,
    phone_validation,
    password_validation,
    title_validation,
)

class HBnBFacade(InMemoryRepository):
    """
    Facade class to interact with repositories for users, places, reviews, and amenities.
    """

    def __init__(self):
        """
        Initialize the HBnBFacade with in-memory repositories for different entities.

        Repositories initialized:
        - user_repo: Manages user data
        - place_repo: Manages place data
        - review_repo: Manages review data
        - amenity_repo: Manages amenity data
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

# /////     TOOL    ///// #

    def clear(self):
            """
            Clean all data in repo for testing purpose
            """

            self.user_repo._storage = {}
            self.place_repo._storage = {}
            self.review_repo._storage = {}
            self.amenity_repo._storage = {}

# /////     USER PART     ///// #

    def create_user(self, user_data):
        """
        Create and add a new user to the user repository.
        Args:
            user_data (dict): A dictionary containing user attributes (first_name, last_name, username, email, etc.).
        Returns:
            user: The created User instance.
        """

        # Try all the validations from validations checks
        try:
            name_length_validation50(user_data['first_name'])
            name_length_validation50(user_data['last_name'])
            username_validation(user_data['username'])
            email_validation(user_data['email'])
            phone_validation(user_data['phone_number'])
            password_validation(user_data['password'])
        except ValueError as e:
            return {"error": str(e)}, 400 
        
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user_by_id(self, user_id):
        """
        Retrieve a user from the repository by their ID.
        Args:
            user_id (str): The ID of the user to retrieve.
        Returns:
            user: The User instance corresponding to the provided ID, or None if not found.
        """
        return self.user_repo.get(user_id)
    
    def get_user_by_attribute(self, **kwargs):
        """
        Retrieve a user from the repository by their specified attribute.
        Args:
            **kwargs: Attributes to search for, e.g., email or username.
        Returns:
            User: The User instance corresponding to the provided attribute, or None if not found.
        """
        # Extract the attribute and its value
        attribute, value = next(iter(kwargs.items()))
        
        # Use the attribute and value to query the user repository
        return self.user_repo.get_by_attribute(attribute, value)

    def get_all_users(self):
        """
        Retrieve a user from the repository 

        Args:
            None.

        Returns:
            All users datas
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """
        Update user data by their ID.

        Args:
            user_id (str): The unique identifier of the user.
            user_data (dict): Updated data in dict format.

        Returns:
            dict: A dictionary containing the user's updated details, or None if the user is not found.
        """
        # Retrieve the user by ID and update only given attributes
        updated_user = self.user_repo.update(user_id, user_data)
        if not updated_user:
            return None

        # Return explicit user data to avoid returning a boolean
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'username': updated_user.username,
            'email': updated_user.email,
            'localisation': updated_user.localisation,
            'phone_number': updated_user.phone_number,
        }

# /////     PLACE PART     ///// #

    def create_place(self, place_data):
        """Create a new place with the given data"""
        # Check if owner exist
        owner = self.get_user_by_id(place_data['owner_id'])
        if not owner:
            return None

        # Create new instance of place associating the owner
        new_place = Place(
            placename = place_data['placename'],
            description = place_data.get('description', ''),
            price = place_data['price'],
            latitude = place_data['latitude'],
            longitude = place_data['longitude'],
            owner = owner  # Associate the owner found in the previous check
        )

        # Manage amenities if provided
        if 'amenities' in place_data:
            for amenity_name in place_data['amenities']:
                amenity = self.get_amenity_by_name(amenity_name)
                if not amenity:
                    amenity = self.create_amenity({'amenity_name': amenity_name})
                new_place.add_amenity(amenity)

        self.place_repo.add(new_place)

        return new_place



    def get_place_by_id(self, place_id):
            """
            Retrieve a place from the repository by their ID.
            Args:
                place_id (str): The ID of the place to retrieve.
            Returns:
                user: The User instance corresponding to the provided ID, or None if not found.
            """
            return self.place_repo.get(place_id)

    def get_place_by_attribute(self, **kwargs):
        """
        Retrieve a place from the repository by their specified attribute.
        Args:
            **kwargs: Attributes to search for
        Returns:
            User: The Place instance corresponding to the provided attribute, or None if not found.
        """
        # Extract the attribute and its value
        attribute, value = next(iter(kwargs.items()))
        
        # Use the attribute and value to query the user repository
        return self.place_repo.get_by_attribute(attribute, value)

    def get_all_place(self):
        """
        Retrieve all place from the repository 

        Args:
            None.

        Returns:
            all places data
        """
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """
        Update place data by their ID.

        Args:
            place_id (str): The unique identifier of the place.
            place_data (dict): Updated data in dict format.

        Returns:
            Place: The updated Place object, or None if the place is not found.
        """
        # Retrieve the place by ID
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Update basic attributes
        for key, value in place_data.items():
            if key not in ['owner_id', 'amenities']:
                setattr(place, key, value)

        # Update owner if provided
        if 'owner_id' in place_data:
            new_owner = self.get_user_by_id(place_data['owner_id'])
            if new_owner:
                place.owner = new_owner

        # Update amenities if provided
        if 'amenities' in place_data:
            # Clear existing amenities
            place.amenities = []
            for amenity_name in place_data['amenities']:
                amenity = self.get_amenity_by_name(amenity_name)
                if not amenity:
                    amenity = self.create_amenity({'amenity_name': amenity_name})
                place.add_amenity(amenity)

        # Prepare updated data dictionary
        updated_data = {
            'placename': place.placename,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': place.owner,
            'amenities': place.amenities
        }

        # Save the updated place
        updated_place = self.place_repo.update(place_id, updated_data)

        return updated_place

# /////     REVIEW PART     ///// #

    def create_review(self, review_data):
        """
        Creates a review with the provided data, validating required associations.

        Args:
            review_data (dict): Contains 'text', 'rating', 'user_id', 'place_id'.
        
        Returns:
            Review: The created review instance.
        
        Raises:
            ValueError: If any required field is missing or invalid.
        """
        # Validate required fields
        required_fields = ['text', 'rating', 'user_id', 'place_id']
        for field in required_fields:
            if field not in review_data:
                raise ValueError(f"{field} is required.")

        # Validate user and place existence
        user = self.user_repo.get(review_data['user_id'])
        place = self.place_repo.get(review_data['place_id'])

        if not user:
            raise ValueError("User not found.")
        if not place:
            raise ValueError("Place not found.")
        
        # Create the review instance
        review = Review(
            title=review_data['title'],
            text=review_data['text'],
            rating=review_data['rating'],
            place_id=review_data['place_id'],
            owner=user
        )

        # Add the review to the repository
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.
        
        Args:
            review_id (str): The review's identifier.
        
        Returns:
            Review: The corresponding review or None if not found.
        """
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """
        Retrieve all reviews.
        
        Returns:
            list[dict]: List of all reviews as dictionaries.
        """
        reviews = self.review_repo.get_all()
        return [{'id': review.id,
                'title': review.title,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.owner.id,
                'place_id': review.place_id}
                for review in reviews]

    def get_reviews_by_place(self, place_id):
        """
        Retrieve all reviews associated with a specific place.
        
        Args:
            place_id (str): The identifier of the place.
        
        Returns:
            list[Review]: List of reviews for the specified place.
        """
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        """
        Update a review with the provided data.
        
        Args:
            review_id (str): The review's identifier.
            review_data (dict): New review data.
        
        Returns:
            Review: The updated review instance.
        
        Raises:
            ValueError: If the review does not exist.
        """
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found.")
        
        # Update attributes
        for key, value in review_data.items():
            setattr(review, key, value)

        self.review_repo.update(review_id, review)
        return review

    def delete_review(self, review_id):
        """
        Delete a review by its ID.
        
        Args:
            review_id (str): The identifier of the review to delete.
        
        Returns:
            bool: True if the review was deleted, False otherwise.
        """
        return self.review_repo.delete(review_id)

# /////     AMENITY PART     ///// #

    def create_amenity(self, amenity_data):
            """
            Create and add a new amenity to the amenity repository.
            Args:
                amenity_data (dict): A dictionary containing amenity attribute (amenity_name).
            Returns:
                amenity: The created amenity instance.
            """

            # Try all the validations from validations checks
            try:
                title_validation(amenity_data['amenity_name'])
            except ValueError as e:
                return {"error": str(e)}, 400 
            
            amenity = Amenity(**amenity_data)

            self.amenity_repo.add(amenity)
            return amenity

    def get_amenity_by_id(self, amenity_id):
        """
        Retrieve a amenity from the repository by their ID.
        Args:
            amenity_id (str): The ID of the amenity to retrieve.
        Returns:
            user: The Amenity instance corresponding to the provided ID, or None if not found.
        """
        return self.amenity_repo.get(amenity_id)
    
    def get_amenity_by_name(self, amenity_name):
        """
        Retrieve a amenity from the repository by their ID.
        Args:
            amenity_id (str): The ID of the amenity to retrieve.
        Returns:
            user: The Amenity instance corresponding to the provided ID, or None if not found.
        """
        return self.amenity_repo.get(amenity_name)

    def get_all_amenities(self):
        """
        Retrieve all amenities from the repository 

        Args:
            None.

        Returns:
            All amenities datas
        """
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """
        Update amenity data by their ID.

        Args:
            amenity_id (str): The unique identifier of the amenity.
            amenity_data (dict): Updated data in dict format.

        Returns:
            dict: A dictionary containing the amenity's updated details, or None if the user is not found.
        """
        # Retrieve the amenity by ID and update only given attributes
        updated_amenity = self.amenity_repo.update(amenity_id, amenity_data)
        if not updated_amenity:
            return None

        # Return explicit amenity data to avoid returning a boolean
        return {
            'id': updated_amenity.id,
            'amenity_name': updated_amenity.amenity_name
        }