from base_model import BaseModel
# from validation_checks import (for later implementation)
from PseudoDataBase import amenity_id_list

class Amenity(BaseModel):
    """
    Represents a amenity with attributes inherited from BaseModel.
    """

    # Initialisation of the Amenity class
    def __init__(self, title, rank):
        """
        Create instance of amenity.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Add the ID (from the BaseModel) to the amenity id list.
        amenity_id_list.append(id)