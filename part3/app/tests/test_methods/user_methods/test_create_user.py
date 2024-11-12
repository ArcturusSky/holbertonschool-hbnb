"""
Module to test the user creation functionality in HBnBFacade.
This module verifies that a user can be created with the specified attributes.
"""

import pytest
from app.services.facade import HBnBFacade
from app.models.user import User

def test_create_user():
    """
    Test the creation of a user through the HBnBFacade.
    
    This test verifies that a user can be created using the facade's
    create_user method and checks if the returned data is correct.

    Assertions:
    - The created user's attributes match the input data.
    - The user is assigned a unique ID.
    """
    facade = HBnBFacade()

    # Sample user data for creation
    user_data = {
        "first_name": "Carmilla",
        "last_name": "Carmine",
        "username": "BladeOverlord",
        "password": "AngelicSteel12",
        "email": "Carmine.C@example.com",
        "localisation": "Hell",
        "phone_number": "0102030405",
        "is_admin": False
    }

    # Create the user using the facade
    created_user = facade.create_user(user_data)

    # Verify that the created user's attributes are correct
    assert isinstance(created_user, User)
    assert created_user.first_name == "Carmilla"
    assert created_user.last_name == "Carmine"
    assert created_user.username == "BladeOverlord"
    assert created_user.email == "Carmine.C@example.com"
    assert created_user.localisation == "Hell"
    assert created_user.phone_number == "0102030405"
    assert created_user.is_admin is False
    assert created_user.id is not None  # Ensure that an ID was assigned

    print("User creation test passed!")

# Running the test manually
if __name__ == "__main__":
    pytest.main([__file__])