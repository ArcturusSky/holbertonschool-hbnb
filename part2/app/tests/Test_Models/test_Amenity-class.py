import pytest
from app.models.amenity import Amenity
from app.models.PseudoDataBase import (
    amenity_id_list,
    amenity_list,
)

# Clearing the data base before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """Clear pseudo-database before each test."""
    amenity_id_list.clear()
    amenity_list.clear()

def test_amenity_creation():
    amenity = Amenity(
        title="Wi-Fi",
        )
    assert amenity.title == "Wi-Fi"
    print("Amenity creation test passed!")

test_amenity_creation()