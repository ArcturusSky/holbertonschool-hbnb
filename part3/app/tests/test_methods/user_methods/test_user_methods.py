"""
Module to test all user-related functionalities in HBnBFacade.
This module includes tests for user creation, retrieval, update, and listing.
"""

import pytest
from app.services.facade import HBnBFacade
from app.models.user import User

@pytest.fixture(autouse=True)
def clear_facade():
    """Nettoie la façade avant chaque test."""
    facade = HBnBFacade()
    facade.clear()
    yield facade

@pytest.fixture
def sample_user(clear_facade):
    user_data = {
        "first_name": "Clara",
        "last_name": "Carmine",
        "username": "ClaraC",
        "password": "LittleMamaGirl02",
        "email": "Carmine.Cl@example.com",
        "localisation": "Hell",
        "phone_number": "0304050607",
        "is_admin": False
    }
    return clear_facade.create_user(user_data)

def test_create_user(clear_facade):
    """Test user creation"""
    user_data = {
        "first_name": "Clara",
        "last_name": "Carmine",
        "username": "ClaraC",
        "password": "LittleMamaGirl02",
        "email": "Carmine.Cl@example.com",
        "localisation": "Hell",
        "phone_number": "0304050607",
        "is_admin": False
    }
    created_user = clear_facade.create_user(user_data)

    assert isinstance(created_user, User)
    assert created_user.first_name == "Clara"
    assert created_user.last_name == "Carmine"
    assert created_user.username == "ClaraC"
    assert created_user.email == "Carmine.Cl@example.com"
    assert created_user.localisation == "Hell"
    assert created_user.phone_number == "0304050607"
    assert created_user.is_admin is False
    assert created_user.id is not None

    print("User creation test passed!")

def test_get_user(clear_facade, sample_user):
    """Test retrieving a user by ID"""
    retrieved_user = clear_facade.get_user_by_id(sample_user.id)

    assert retrieved_user is not None
    assert retrieved_user.id == sample_user.id
    assert retrieved_user.username == "ClaraC"
    assert retrieved_user.email == "Carmine.Cl@example.com"

    print("Get user test passed!")

def test_update_user(clear_facade, sample_user):
    """Test updating a user"""
    update_data = {
        "localisation": "Heaven",
        "phone_number": "9876543210"
    }
    updated_user = clear_facade.update_user(sample_user.id, update_data)

    assert updated_user is not None
    assert updated_user.id == sample_user.id
    assert updated_user.localisation == "Heaven"
    assert updated_user.phone_number == "9876543210"
    assert updated_user.username == "ClaraC"
    assert updated_user.email == "Carmine.Cl@example.com"

    print("Update user test passed!")

def test_get_all_users(clear_facade):
    """Test retrieving all users"""
    # Create two users for this test
    clear_facade.create_user({
        "first_name": "Clara",
        "last_name": "Carmine",
        "username": "ClaraC",
        "password": "LittleMamaGirl02",
        "email": "Carmine.Cl@example.com",
        "localisation": "Hell",
        "phone_number": "0304050607",
        "is_admin": False
    })
    clear_facade.create_user({
        "first_name": "John",
        "last_name": "Doe",
        "username": "JohnDoe",
        "password": "password123",
        "email": "john.doe@example.com",
        "localisation": "Earth",
        "phone_number": "1122334455",
        "is_admin": True
    })

    all_users = clear_facade.get_all_users()

    assert isinstance(all_users, list)
    assert len(all_users) >= 2
    assert any(user.username == "ClaraC" for user in all_users)
    assert any(user.username == "JohnDoe" for user in all_users)

    print("Get all users test passed!")

if __name__ == "__main__":
    pytest.main([__file__])