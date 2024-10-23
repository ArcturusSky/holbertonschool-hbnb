import pytest
from app.models.place import Place
from app.models.user import User
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

# Clearing the data base before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """Clear pseudo-database before each test."""
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

def test_place_w_relationships_creation():
    owner = User(
        first_name="Alice",
        last_name="Smith",
        username= "Lili02",
        password= "Test01",
        email="alice.smith@example.com",
        localisation="Paris",
        phone_number="0203040506")
    place = Place(
        placename="Cozy Apartment",
        description="A nice place to stay",
        price=100,
        latitude=37.7749,
        longitude=-122.4194,
        owner=owner)

    # Adding a review
    review = Review(
        title = "Great stay!",
        text = "The place was cool and clean, great job!",
        rating = 5,
        placename = place.placename,
        owner = owner)

    place.add_review(review)

    assert place.placename == "Cozy Apartment"
    assert place.price == 100
    assert len(place.myreviews) == 1
    assert place.myreviews[0].title == "Great stay!"
    assert place.myreviews[0].text == "The place was cool and clean, great job!"
    print("Place creation and relationship test passed!")

test_place_w_relationships_creation()