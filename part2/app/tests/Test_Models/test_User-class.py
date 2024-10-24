"""
Module to test the creation of a User.
This module verifies that a User instance can be created with the
required attributes and checks the integrity of the User's data.
"""

import pytest
from app.models.user import User
from app.models.PseudoDataBase import username_list, users_id_list, email_list, phonenumber_list

# Clearing the pseudo-database before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """
    Fixture to clear the pseudo-database before each test.
    
    This ensures that each test starts with a clean state, removing any
    leftover data in the pseudo-database. It clears all lists related
    to users, including usernames, user IDs, emails, and phone numbers.
    """
    username_list.clear()
    users_id_list.clear()
    email_list.clear()
    phonenumber_list.clear()

def test_user_creation():
    """
    Test the creation of a User instance.
    
    This test verifies that a User can be instantiated with the 
    required attributes (first_name, last_name, username, password, 
    email, localisation, and phone_number). It also checks if the 
    default value of is_admin is set correctly.

    Assertions:
    - The User's first name, last name, username, password, email, 
      localisation, and phone number are correctly set.
    - The default value of is_admin is False.
    """
    user = User(
        first_name="John",
        last_name="Doe",
        username="Jojo",
        password="Jojo1234",
        email="john.doe@example.com",
        localisation="Paris",
        phone_number="0102030405"
    )
    
    # Test if attributes correspond to the creation
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.username == "Jojo"
    assert user.__password__ == "Jojo1234"
    assert user.email == "john.doe@example.com"
    assert user.localisation == "Paris"
    assert user.phone_number == "0102030405"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")

# Running the test manually
test_user_creation()
