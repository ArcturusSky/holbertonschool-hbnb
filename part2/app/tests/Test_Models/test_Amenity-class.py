"""
Module to test the creation of an Amenity.
This module verifies that an Amenity instance can be created with
the required attributes and checks the integrity of the Amenity's data.
"""

import pytest
from app.models.amenity import Amenity
from app.models.PseudoDataBase import (
    amenity_id_list,
    amenity_list,
)

# Clearing the pseudo-database before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """
    Fixture to clear the pseudo-database before each test.
    
    This ensures that each test starts with a clean state, removing any
    leftover data in the pseudo-database. It clears all lists related
    to amenities, including amenity IDs and amenity instances.
    """
    amenity_id_list.clear()
    amenity_list.clear()

def test_amenity_creation():
    """
    Test the creation of an Amenity instance.
    
    This test verifies that an Amenity can be instantiated with the
    required attribute (title). It checks that the title is set correctly
    upon creation.

    Assertions:
    - The Amenity's title is correctly set to the expected value.
    """
    amenity = Amenity(
        title="Wi-Fi",
    )
    
    # Test if attributes correspond to the creation 
    assert amenity.title == "Wi-Fi"
    print("Amenity creation test passed!")

# Running the test manually
test_amenity_creation()
