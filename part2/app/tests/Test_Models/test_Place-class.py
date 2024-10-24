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

def test_place_creation():
    owner = User(
        first_name="Olivier",
        last_name="Jesaispas",
        username= "Oli",
        password= "Test02",
        email="Olivier@example.com",
        localisation="Thonon",
        phone_number="0102030405")
    place = Place(
        placename="Holberton School Thonon",
        description="This is a school",
        price= 15.5,
        latitude= 46.37016323447714,
        longitude= 6.479164831619981,
        owner= owner
        )
    assert place.placename == "Holberton School Thonon"
    assert place.description == "This is a school"
    assert place.price == 15.5
    assert place.adress == (46.37016323447714, 6.479164831619981)
    assert place.owner.username == "Oli"
    print("Place creation test passed!")

test_place_creation()