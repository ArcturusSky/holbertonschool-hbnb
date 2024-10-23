import pytest
from app.models.user import User
from app.models.PseudoDataBase import username_list, users_id_list, email_list, phonenumber_list

# Clearing the data base before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """Clear pseudo-database before each test."""
    username_list.clear()
    users_id_list.clear()
    email_list.clear()
    phonenumber_list.clear()

def test_user_creation():
    user = User(
        first_name="John",
        last_name="Doe",
        username="Jojo",
        password="Jojo1234",
        email="john.doe@example.com",
        localisation="Paris",
        phone_number="0102030405"
        )
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.username == "Jojo"
    assert user.__password__ == "Jojo1234"
    assert user.email == "john.doe@example.com"
    assert user.localisation == "Paris"
    assert user.phone_number == "0102030405"
    assert user.is_admin is False  # Default value
    print("User creation test passed!")

test_user_creation()