from base_model import BaseModel
from validation_checks import email_validation, name_lenght_validation50, phone_validation, username_validation, password_validation
from Data import username_list, placename_list, review_list

class User(BaseModel):
    """
    Represents a user with attributes inherited from BaseModel and
    additional user-specific attributes like first name, last name, email,
    and admin privileges.
    """

    # Initialisation of the User class
    def __init__(self, first_name, last_name, username, password, email, localisation, phone_number, is_admin=False):
        """
        Create instance of User.
        """

        # Get attributs from super class (BaseModel)
        super().__init__()

        # Create valid strong passeword as private attribute
        if not password_validation(password):
            raise ValueError("Password must exceed 5 characters, have an Uppercase and a digit")
        else:
            self.__password__ = password

        # Check correct first and last name lenghts and localisation
        name_lenght_validation50(first_name)
        name_lenght_validation50(last_name)
        name_lenght_validation50(localisation)
        self.first_name = first_name
        self.last_name = last_name
        self.localisation = localisation

        # Check if usernam is valid
        name_lenght_validation50(username)
        username_validation(username)
        self.username = username

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
        self.myplaces = []  # Store all places belonging to User
        self.myreviews = [] # Store all reviews belonging to User

    # Adding data to pseudo-database
    def database_add_user(self, username):
        """ Add username to the "data"""
        username_list.append(username)

    # Relationships with others classes and adding datas
    def add_place(self, place):
        """Add a place to the user."""
        self.myplaces.append(place)
        placename_list.append(place)

    def add_review(self, review):
        """Add a review to the user."""
        self.myreviews.append(review)
        review_list.append(review)
