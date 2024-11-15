from .base_model import BaseModel
from .validation_checks import title_validation
from .PseudoDataBase import amenity_id_list, amenity_list

class Amenity(BaseModel):
    """
    Represents a amenity with attributes inherited from BaseModel.
    """

    # Initialisation of the Amenity class
    def __init__(self, amenity_name):
        """
        Create instance of amenity.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Check if amenity_name valid
        title_validation(amenity_name)
        self.amenity_name = amenity_name

        # Add the ID (from the BaseModel) to the amenity id list.
        amenity_id_list.append(id)
        amenity_list.append(amenity_name)
