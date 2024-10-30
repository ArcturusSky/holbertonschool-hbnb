"""
Module to test the retrieval of all users functionality in HBnBFacade.
"""

import pytest
from app.services.facade import HBnBFacade

@pytest.fixture
def facade():
    return HBnBFacade()

@pytest.fixture
def sample_users(facade):
    user1 = facade.create_user({
        "first_name": "Carmilla",
        "last_name": "Carmine",
        "username": "BladeOverlord",
        "password": "AngelicSteel12",
        "email": "Carmine.C@example.com",
        "localisation": "Hell",
        "phone_number": "0102030405",
        "is_admin": False
    })
    user2 = facade.create_user({
        "first_name": "John",
        "last_name": "Doe",
        "username": "JohnDoe",
        "password": "password123",
        "email": "john.doe@example.com",
        "localisation": "Earth",
        "phone_number": "1122334455",
        "is_admin": True
    })
    return [user1, user2]

def test_get_all_users(facade, sample_users):
    """Test retrieving all users"""
    all_users = facade.get_all_users()

    assert isinstance(all_users, list)
    assert len(all_users) >= 2
    assert any(user.username == "BladeOverlord" for user in all_users)
    assert any(user.username == "JohnDoe" for user in all_users)

    print("Get all users test passed!")

if __name__ == "__main__":
    pytest.main([__file__])