from .base_model import BaseModel
from .validation_checks import title_validation
from .PseudoDataBase import amenity_id_list, amenity_list

class Amenity(BaseModel):
    """
    Represents a amenity with attributes inherited from BaseModel.
    """

    # Initialisation of the Amenity class
    def __init__(self, title):
        """
        Create instance of amenity.
        """

        # Get attributes from super class (BaseModel)
        super().__init__()

        # Check if title valid
        title_validation(title)
        self.title = title

        # Add the ID (from the BaseModel) to the amenity id list.
        amenity_id_list.append(id)
        amenity_list.append(title)
