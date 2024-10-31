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
    adress_validation,
    place_validation,
    description_validation,
    price_validation,
    title_validation,
    rating_validation,
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

            self.user_repo = {}
            self.place_repo = {}
            self.review_repo = {}
            self.amenity_repo = {}

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
            """
            Create and add a new place to the place repository.
            Args:
                place_data (dict): A dictionary containing place attributes (placename, descriptions, price, etc.).
            Returns:
                place: The created place instance.
            """

            # Try all the validations from validations checks
            try:
                name_length_validation50(place_data['placename'])
                adress_validation(place_data['latitude'], place_data['longitude']) 
                place_validation(place_data['placename'], place_data['address'])
                description_validation(place_data['description'])
                price_validation(place_data['price'])
                
                # Check if owner exist by its ID
                if not self.user_repo.get(place_data['owner']):
                    raise ValueError("Owner does not exist.")
            except ValueError as e:
                return {"error": str(e)}, 400 

            place = Place(**place_data)
            self.place_repo.add(place)
            return place

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
            dict: A dictionary containing the place's updated details, or None if the user is not found.
        """
        # Retrieve the place by ID and update only given attributes
        updated_place = self.place_repo.update(place_id, place_data)
        if not updated_place:
            return None

        # Return explicit place data to avoid returning a boolean
        return {
            'id': updated_place.id,
            'title': updated_place.title,
            'text': updated_place.text,
        }

# /////     REVIEW PART     ///// #

    def create_review(self, review_data):
            """
            Create and add a new review to the review repository.
            Args:
                review_data (dict): A dictionary containing review attributes (title, text, rating, placename, owner.).
            Returns:
                review: The created review instance.
            """

            # Try all the validations from validations checks
            try:
                name_length_validation50(review_data['title'])
                description_validation(review_data['text'])
                rating_validation(review_data['rating'])

                # Check if place exist by its ID
                if not self.place_repo.get(review_data['place']):
                    raise ValueError("Place does not exist.")
                
                # Check if owner exist by its ID
                if not self.user_repo.get(review_data['owner']):
                    raise ValueError("Owner does not exist.")
            except ValueError as e:
                return {"error": str(e)}, 400 
            
            review = Review(**review_data)
            self.review_repo.add(review)
            return review
    
    def get_review_by_id(self, review_id):
        """
        Retrieve a review from the repository by their ID.
        Args:
            review_id (str): The ID of the review to retrieve.
        Returns:
            user: The Review instance corresponding to the provided ID, or None if not found.
        """
        return self.review_repo.get(review_id)

    def get_review_by_attribute(self, **kwargs):
        """
        Retrieve a review from the repository by their specified attribute.
        Args:
            **kwargs: Attributes to search for
        Returns:
            User: The Review instance corresponding to the provided attribute, or None if not found.
        """
        # Extract the attribute and its value
        attribute, value = next(iter(kwargs.items()))
        
        # Use the attribute and value to query the user repository
        return self.review_repo.get_by_attribute(attribute, value)
    
    def get_all_reviews(self):
        """
        Retrieve all reviews from the repository 

        Args:
            None.

        Returns:
            All reviews datas
        """
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        """
        Update review data by their ID.

        Args:
            review_id (str): The unique identifier of the review.
            review_data (dict): Updated data in dict format.

        Returns:
            dict: A dictionary containing the review's updated details, or None if the user is not found.
        """
        # Retrieve the review by ID and update only given attributes
        updated_review = self.review_repo.update(review_id, review_data)
        if not updated_review:
            return None

        # Return explicit review data to avoid returning a boolean
        return {
            'id': updated_review.id,
            'title': updated_review.title,
            'text': updated_review.text,
        }

# /////     AMENITY PART     ///// #

    def create_amenity(self, amenity_data):
            """
            Create and add a new amenity to the amenity repository.
            Args:
                amenity_data (dict): A dictionary containing amenity attribute (title).
            Returns:
                amenity: The created amenity instance.
            """

            # Try all the validations from validations checks
            try:
                title_validation(amenity_data['title'])
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

    def get_amenity_by_attribute(self, **kwargs):
        """
        Retrieve a amenity from the repository by their specified attribute.
        Args:
            **kwargs: Attributes to search for
        Returns:
            User: The Amenity instance corresponding to the provided attribute, or None if not found.
        """
        # Extract the attribute and its value
        attribute, value = next(iter(kwargs.items()))
        
        # Use the attribute and value to query the user repository
        return self.amenity_repo.get_by_attribute(attribute, value)
    
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
            'title': updated_amenity.title
        }