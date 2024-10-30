"""
Module to test the user retrieval functionality in HBnBFacade.
"""

import pytest
from app.services.facade import HBnBFacade

@pytest.fixture
def facade():
    return HBnBFacade()

@pytest.fixture
def sample_user(facade):
    user_data = {
        "first_name": "Carmilla",
        "last_name": "Carmine",
        "username": "BladeOverlord",
        "password": "AngelicSteel12",
        "email": "Carmine.C@example.com",
        "localisation": "Hell",
        "phone_number": "0102030405",
        "is_admin": False
    }
    return facade.create_user(user_data)

def test_get_user(facade, sample_user):
    """Test retrieving a user by ID"""
    retrieved_user = facade.get_user_by_id(sample_user.id)

    assert retrieved_user is not None
    assert retrieved_user.id == sample_user.id
    assert retrieved_user.username == "BladeOverlord"
    assert retrieved_user.email == "Carmine.C@example.com"

    print("Get user test passed!")

if __name__ == "__main__":
    pytest.main([__file__])