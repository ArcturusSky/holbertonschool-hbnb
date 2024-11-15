from .base_model import BaseModel
from .validation_checks import (
    title_validation,
    description_validation,
    rating_validation,
    given_owner_validation
)
from .PseudoDataBase import review_id_list, review_list

class Review(BaseModel):
    """
    Represents a review with attributes inherited from BaseModel.
    """

    def __init__(self, title, text, rating, place_id, owner):
        """
        Create instance of review.
        """

        super().__init__()

        # Add the ID (from the BaseModel) to the review id list.
        review_id_list.append(self.id)

        # Validate attributes
        title_validation(title)
        self.title = title

        description_validation(text)
        self.text = text

        rating_validation(rating)
        self.rating = rating

        given_owner_validation(owner)
        self.owner = owner

        self.place_id = place_id

        # Add data to the PseudoDatabase
        review_list.append(self)