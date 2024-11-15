from .base_model import BaseModel
# from validation_checks import (for later implementation)
from .PseudoDataBase import places_id_list, placename_list, places_adress_list
from .validation_checks import (
    place_validation,
    description_validation,
    adress_validation,
    price_validation,
    given_owner_validation
)


class Place(BaseModel):
    """
    Represents a Place with attributes inherited from BaseModel.
    """

    # Initialisation of the Place class
    def __init__(self, placename, description, price, latitude, longitude, owner):
        """
        Create instance of place1.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Add the ID (from the BaseModel) to the place id list
        places_id_list.append(id)

        # Check if coordinates are valid and create tuple of theses
        self.latitude = latitude
        self.longitude = longitude
        self.adress = adress_validation(latitude, longitude)

        # Check if place doesn't already exist
        place_validation(placename, self.adress)
        self.placename = placename

        # Check if description is valid
        description_validation(description)
        self.description = description

        # Check if price is valid
        price_validation(price)
        self.price = price

        # Check if owner exist is in the FACADE
        given_owner_validation(owner)
        self.owner = owner

        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

        # Add the place info into the PseudoDataBase
        placename_list.append(self.placename)
        places_adress_list.append(self.adress)


    # Relationships with others classes and adding datas
    def add_review(self, review):
        """Add a review to the place."""
        self.myreviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)