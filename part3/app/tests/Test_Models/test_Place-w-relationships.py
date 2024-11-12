"""
Module to test the creation of a Place with relationships.
This module verifies that relationships between Place, Review, and Amenity 
are correctly handled, ensuring that Reviews and Amenities can be 
associated with a Place instance.
"""

import pytest
from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review

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
    
    This ensures that each test starts with a clean state, with no leftover
    data in the pseudo-database. It clears all lists related to users, places,
    reviews, and amenities before running a test.
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

# Test case for creating a place with reviews and amenities
def test_place_w_relationships_creation():
    """
    Test the creation of a Place and the addition of Reviews and Amenities.
    
    This test ensures that a Place instance is correctly created with the
    required attributes (placename, description, price, latitude, longitude, 
    and owner). It then verifies the following:
    
    - Adding a Review to the Place works correctly and the review's attributes 
      (title, text, rating, and placename) match the expected values.
    - Adding an Amenity to the Place works, and the amenity's title is 
      correctly set and associated with the Place.
    
    Assertions:
    - The Place's placename, price, and reviews are correctly initialized.
    - The Review is correctly associated with the Place and can be retrieved.
    - The Amenity is successfully associated with the Place.
    """
    owner = User(
        first_name="Alice",
        last_name="Smith",
        username="Lili02",
        password="Lili01020304050607080910",
        email="alice.smith@example.com",
        localisation="Paris",
        phone_number="0203040506"
    )
    
    place = Place(
        placename="Cozy Apartment",
        description="A nice place to stay",
        price=100,
        latitude=37.7749,
        longitude=-122.4194,
        owner=owner
    )

    # Adding a review to the place
    review = Review(
        title="Great stay!",
        text="The place was cool and clean, great job!",
        rating=5,
        placename=place.placename,
        owner=owner
    )
    place.add_review(review)

    # Test if attributes correspond to the creation of the place and review
    assert place.placename == "Cozy Apartment"
    assert place.price == 100
    assert len(place.myreviews) == 1
    assert place.myreviews[0].title == "Great stay!"
    assert place.myreviews[0].text == "The place was cool and clean, great job!"
    print("Place creation and review association test passed!")

    # Adding a new amenity to the place
    pool = Amenity(title="Pool")
    place.add_amenity(pool)

    # Test if the amenity was correctly added to the place
    assert place.myamenities[0].title == "Pool"
    print("Amenity addition test passed!")

# Running the test manually
test_place_w_relationships_creation()
