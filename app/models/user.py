from base_model import BaseModel

from validation_checks import (
    email_validation,
    name_lenght_validation50,
    phone_validation, username_validation,
    password_validation
)

from PseudoDataBase import (
    username_list,
    placename_list,
    review_list,
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

        # Check correct first and last name lenghts and localisation
        name_lenght_validation50(first_name)
        name_lenght_validation50(last_name)
        name_lenght_validation50(localisation)
        self.first_name = first_name
        self.last_name = last_name
        self.localisation = localisation

        # Check if username is valid and add to data list
        name_lenght_validation50(username)
        username_validation(username)
        self.username = username

        # Check email format
        email_validation(email)
        self.email = email

        # Check phone number
        phone_validation(phone_number)
        self.phone_number = phone_number

        # Private attribute for admin can be changed only by admin
        self.__is_admin__ = is_admin

        # Initialize lists to store related objects belonging to users
        self.myplaces = []
        self.myreviews = []

    # Adding data to pseudo-database
    def database_add_user(self, username):
        """
        Add all users attributes to the PseudoDataBase
        for relationships with other class and validations
        """

        users_id_list.append(id)
        username_list.append(username)
        email_list.append(self.email)
        phonenumber_list.append(self.phone_number)

    # Relationships with others classes and adding datas to Database
    def add_place(self, place):
        """Add a place to the user."""

        self.myplaces.append(place)
        placename_list.append(place)

    def add_review(self, review):
        """Add a review to the user."""

        self.myreviews.append(review)
        review_list.append(review)
