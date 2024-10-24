from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
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

    def create_user(self, user_data):
        """
        Create and add a new user to the user repository.

        Args:
            user_data (dict): A dictionary containing user attributes (first_name, last_name, username, email, etc.).

        Returns:
            user: The created User instance.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieve a user from the repository by their ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            user: The User instance corresponding to the provided ID, or None if not found.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieve a user from the repository by their email address.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            User: The User instance corresponding to the provided email, or None if not found.
        """
        return self.user_repo.get_by_attribute('email', email)
