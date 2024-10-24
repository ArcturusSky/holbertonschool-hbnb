"""
Module to test creating a Place.
This module verifies that a Place instance can be created with the
required attributes and checks the integrity of the Place's data.
"""

import pytest
from app.models.place import Place
from app.models.user import User
from app.models.PseudoDataBase import (
    users_id_list,
    places_id_list,
    review_id_list,
    amenity_id_list,
    username_list,
    phonenumber_list,
    email_list,
    placename_list,
    places_adress_list,
    review_list,
    amenity_list
)

# Clearing the pseudo-database before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """
    Fixture to clear the pseudo-database before each test.
    
    This ensures that each test starts with a clean state, removing any
    leftover data in the pseudo-database. It clears all lists related
    to users, places, reviews, amenities, and contact information.
    """
    users_id_list.clear()
    places_id_list.clear()
    review_id_list.clear()
    amenity_id_list.clear()
    username_list.clear()
    phonenumber_list.clear()
    email_list.clear()
    placename_list.clear()
    places_adress_list.clear()
    review_list.clear()
    amenity_list.clear()

def test_place_creation():
    """
    Test the creation of a Place instance.
    
    This test verifies that a Place can be instantiated with the
    required attributes (placename, description, price, latitude,
    longitude, and owner). It checks that these attributes are set
    correctly upon creation.

    Assertions:
    - The Place's placename is correctly set.
    - The Place's description is correctly set.
    - The Place's price is correctly set.
    - The Place's address (latitude and longitude) is correctly set.
    - The owner of the Place is correctly set.
    """
    owner = User(
        first_name="Olivier",
        last_name="Jesaispas",
        username="Oli",
        password="Test02",
        email="Olivier@example.com",
        localisation="Thonon",
        phone_number="0102030405"
    )
    
    place = Place(
        placename="Holberton School Thonon",
        description="This is a school",
        price=15.5,
        latitude=46.37016323447714,
        longitude=6.479164831619981,
        owner=owner
    )

    # Test if attributes correspond to the creation 
    assert place.placename == "Holberton School Thonon"
    assert place.description == "This is a school"
    assert place.price == 15.5
    assert place.adress == (46.37016323447714, 6.479164831619981)
    assert place.owner.username == "Oli"
    print("Place creation test passed!")

# Running the test manually
test_place_creation()
