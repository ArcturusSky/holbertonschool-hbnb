from base_model import BaseModel
# from validation_checks import (for later implementation)
from PseudoDataBase import review_id_list

class Review(BaseModel):
    """
    Represents a review with attributes inherited from BaseModel.
    """

    # Initialisation of the Review class
    def __init__(self, title, rank):
        """
        Create instance of review.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Add the ID (from the BaseModel) to the review id list.
        review_id_list.append(id)
        review_list.append(review)
