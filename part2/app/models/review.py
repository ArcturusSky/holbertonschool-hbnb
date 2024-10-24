from .base_model import BaseModel
from .validation_checks import (
    title_validation,
    description_validation,
    rating_validation,
    existing_place_validation,
    owner_validation
)
from .PseudoDataBase import review_id_list, review_list

class Review(BaseModel):
    """
    Represents a review with attributes inherited from BaseModel.
    """

    # Initialisation of the Review class
    def __init__(self, title, text, rating, placename, owner):
        """
        Create instance of review.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Add the ID (from the BaseModel) to the review id list.
        review_id_list.append(id)

        # Check if title is valid
        title_validation(title)
        self.title = title

        # Check if text is valid
        description_validation(text)
        self.text = text

        # Check if rating is valid
        rating_validation(rating)
        self.rating = rating

        # Check if place exist
        existing_place_validation(placename)
        self.placename = placename

        # Check if user exist
        owner_validation(owner)
        self.owner = owner

        # Add data to the PseudoDatabase
        review_list.append(self.title)
