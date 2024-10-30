"""
Module to test the user update functionality in HBnBFacade.
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

def test_update_user(facade, sample_user):
    """Test updating a user"""
    update_data = {
        "localisation": "Heaven",
        "phone_number": "9876543210"
    }
    updated_user = facade.update_user(sample_user.id, update_data)

    assert updated_user is not None
    assert updated_user.id == sample_user.id
    assert updated_user.localisation == "Heaven"
    assert updated_user.phone_number == "9876543210"
    assert updated_user.username == "BladeOverlord"
    assert updated_user.email == "Carmine.C@example.com"

    print("Update user test passed!")

if __name__ == "__main__":
    pytest.main([__file__])