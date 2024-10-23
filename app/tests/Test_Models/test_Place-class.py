import pytest
from app.models.place import Place
from app.models.PseudoDataBase import (
    places_id_list,
    placename_list,
    places_adress_list,
    username_list
)

# Clearing the data base before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """Clear pseudo-database before each test."""
    places_id_list.clear()
    placename_list.clear()
    places_adress_list.clear()

# Added in the list for testing purpose
username_list.append("Olivier")

def test_place_creation():
    place = Place(
        placename="Holberton School Thonon",
        description="This is a school",
        price= 15.5,
        latitude= 46.37016323447714,
        longitude= 6.479164831619981,
        owner= "Olivier"
        )
    assert place.placename == "Holberton School Thonon"
    assert place.description == "This is a school"
    assert place.price == 15.5
    assert place.adress == (46.37016323447714, 6.479164831619981)
    assert place.owner == "Olivier"
    print("Place creation test passed!")

test_place_creation()