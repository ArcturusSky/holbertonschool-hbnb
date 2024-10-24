"""
Module to test the creation of a Review in the HBnB application.
This module contains unit tests for creating a `Review` instance, 
ensuring that the attributes are correctly set, and that the 
pseudo-database is properly cleared and initialized before each test.
"""

import pytest
from app.models.review import Review
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
    
    This ensures that each test starts with an empty or clean database,
    avoiding issues caused by leftover data from previous tests. After 
    clearing, a default place name is added to the `placename_list` for
    testing.
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

    # Adding test data to the database
    placename_list.append("Holberton School Thonon")

# Test case for creating a review
def test_review_creation():
    """
    Test the creation of a Review instance and validate its attributes.
    
    This test verifies that when a `Review` is created, its attributes 
    (title, text, rating, placename, and owner) are correctly set. 
    It also ensures that the `owner` (a `User` instance) has the expected 
    username associated with the review.
    
    Assertions:
    - The review's title, text, rating, and placename match the expected values.
    - The review's owner is correctly associated with the review.
    """
    owner = User(
        first_name="Jane",
        last_name="Doe",
        username="JaneDoe01",
        password="Test03",
        email="Jane@example.com",
        localisation="New-York",
        phone_number="0304050607"
    )
    review = Review(
        title="Good School",
        text="This is a school and this school is good",
        rating=3.5,
        placename="Holberton School Thonon",
        owner=owner
    )

    # Test if attributes correspond to the creation 
    assert review.title == "Good School"
    assert review.text == "This is a school and this school is good"
    assert review.rating == 3.5
    assert review.placename == "Holberton School Thonon"
    assert review.owner.username == "JaneDoe01"

    print("Review creation test passed!")

# Running the test manually
test_review_creation()
