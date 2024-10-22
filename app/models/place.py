from base_model import BaseModel
# from validation_checks import (for later implementation)
from PseudoDataBase import places_id_list
class Place(BaseModel):
    """
    Represents a Place with attributes inherited from BaseModel.
    """

    # Initialisation of the Place class
    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Create instance of review.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Add the ID (from the BaseModel) to the place id list.
        places_id_list.append(id)

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)