"""
This module will holds the methodes dedicated to getting by id from repo
"""

def get_user_by_id(self, user_id):
    """
    Retrieve a user from the repository by their ID.
    Args:
        user_id (str): The ID of the user to retrieve.
    Returns:
        user: The User instance corresponding to the provided ID, or None if not found.
    """
    return self.user_repo.get(user_id)

def get_place_by_id(self, place_id):
    """
    Retrieve a place from the repository by their ID.
    Args:
        place_id (str): The ID of the place to retrieve.
    Returns:
        user: The User instance corresponding to the provided ID, or None if not found.
    """
    return self.place_repo.get(place_id)

def get_review_by_id(self, review_id):
    """
    Retrieve a review from the repository by their ID.
    Args:
        review_id (str): The ID of the review to retrieve.
    Returns:
        user: The User instance corresponding to the provided ID, or None if not found.
    """
    return self.review_repo.get(review_id)

def get_amenity_by_id(self, amenity_id):
    """
    Retrieve a amenity from the repository by their ID.
    Args:
        amenity_id (str): The ID of the amenity to retrieve.
    Returns:
        user: The User instance corresponding to the provided ID, or None if not found.
    """
    return self.amenity_repo.get(amenity_id)