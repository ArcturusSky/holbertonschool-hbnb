import pytest
from app.models.review import Review
from app.models.PseudoDataBase import (
    review_id_list,
    review_list,
    placename_list,
    username_list
)

# Clearing the data base before each test
@pytest.fixture(autouse=True)
def clear_pseudo_database():
    """Clear pseudo-database before each test."""
    username_list.clear()
    review_id_list.clear()
    placename_list.clear()
    review_list.clear()

    # Added in the list for testing purpose
    username_list.append("Olivier")
    placename_list.append("Holberton School Thonon")

def test_review_creation():
    review = Review(
        title="Good School",
        text="This is a school and this school is good",
        rating= 3.5,
        placename= "Holberton School Thonon",
        user= "Olivier"
        )
    assert review.title == "Good School"
    assert review.text == "This is a school and this school is good"
    assert review.rating == 3.5
    assert review.placename == "Holberton School Thonon"
    assert review.author == "Olivier"
    print("Review creation test passed!")

test_review_creation()