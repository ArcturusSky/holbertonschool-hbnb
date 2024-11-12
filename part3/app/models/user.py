from .base_model import BaseModel

from .validation_checks import (
    email_validation,
    name_length_validation50,
    phone_validation, username_validation,
    password_validation
)

from .PseudoDataBase import (
    username_list,
    users_id_list,
    email_list,
    phonenumber_list,
)


class User(BaseModel):
    """
    Represents a user with attributes inherited from BaseModel and
    additional user-specific attributes like first name, last name, email,
    and admin privileges.
    """

    # Initialisation of the User class
    def __init__(
            self, first_name, last_name, username,
            password, email, localisation, phone_number, is_admin=False):
        """
        Create instance of User.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Create valid strong password as private attribute
        password_validation(password)
        self.__password__ = password

        # Check correct first and last name lengths and localisation
        name_length_validation50(first_name)
        name_length_validation50(last_name)
        name_length_validation50(localisation)
        self.first_name = first_name
        self.last_name = last_name
        self.localisation = localisation

        # Check if username is valid and add to data list
        name_length_validation50(username)
        username_validation(username)
        self.username = username

        # Check email format
        email_validation(email)
        self.email = email

        # Check phone number
        phone_validation(phone_number)
        self.phone_number = phone_number

        # Private attribute for admin can be changed only by admin
        self.__is_admin__ = False

        # Initialize lists to store related objects belonging to users
        self.myplaces = []
        self.myreviews = []

        # Adding User's data into the pseudo-database
        users_id_list.append(self.id)
        username_list.append(self.username)
        email_list.append(self.email)
        phonenumber_list.append(self.phone_number)

    # Getter for is_admin
    @property
    def is_admin(self):
        """Return is user is admin."""
        return self.__is_admin__

    # Setter for is_admin
    @is_admin.setter
    def is_admin(self, user_requesting):
        """Allows granting admin privileges only if the requesting user is an admin."""
        if user_requesting.is_admin:
            self.__is_admin__ = True
        else:
            raise PermissionError("Only administrator can grand admin rank.")

    # Relationships with others classes
    def add_place(self, place):
        """Add a place to the user."""
        self.myplaces.append(place)


    def add_review(self, review):
        """Add a review to the user."""

        self.myreviews.append(review)
