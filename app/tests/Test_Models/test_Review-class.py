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

    # Adding data to database for test
    placename_list.append("Holberton School Thonon")

def test_review_creation():
    owner = User(
        first_name="Jane",
        last_name="Doe",
        username= "JaneDoe01",
        password= "Test03",
        email="Jane@example.com",
        localisation="New-York",
        phone_number="0304050607")
    review = Review(
        title="Good School",
        text="This is a school and this school is good",
        rating= 3.5,
        placename= "Holberton School Thonon",
        owner= owner
        )
    assert review.title == "Good School"
    assert review.text == "This is a school and this school is good"
    assert review.rating == 3.5
    assert review.placename == "Holberton School Thonon"
    assert review.owner.username == "JaneDoe01"
    print("Review creation test passed!")

test_review_creation()