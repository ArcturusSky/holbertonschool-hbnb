from base_model import BaseModel
from validation_checks import email_validation, name_lenght_validation50, phone_validation

class User(BaseModel):
    """
    Represents a user with attributes inherited from BaseModel and
    additional user-specific attributes like first name, last name, email,
    and admin privileges.
    """

    # Initialisation of the User class
    def __init__(self, first_name, last_name, email, localisation, phone_number, is_admin=False):
        """
        Create instance of User.
        """

        # Get attributs from super class (BaseModel)
        super().__init__()

        # Check correct first and last name lenghts and localisation
        name_lenght_validation50(first_name)
        name_lenght_validation50(last_name)
        name_lenght_validation50(localisation)
        self.first_name = first_name
        self.last_name = last_name
        self.localisation = localisation

        # Check email format
        if not email_validation(email):
            raise ValueError("Invalid email format.")
        else:
            self.email = email

        # Check phone number
        if not phone_validation(phone_number):
            raise ValueError("Invalid phone number")

        # Private attribut for admin can be changed only by admin
        self.__is_admin__ = is_admin

        # Initialize lists to store related objects
        self.places = []  # Store all places belonging to User
        self.reviews = [] # Store all reviews belonging to User

    # Relationships with others classes
    def add_place(self, place):
        """Add a place to the user."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user."""
        self.reviews.append(review)
