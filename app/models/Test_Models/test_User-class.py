from app.models.user import User

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