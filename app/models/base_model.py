import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class that defines common attributes and methods 
    for other models in the application.
    
    Attributes:
        id (str): Unique identifier for each instance, generated using uuid.
        created_at (datetime): Timestamp when the instance is created.
        updated_at (datetime): Timestamp when the instance was last modified.
    """

    def __init__(self):
        """Initialize a new instance of BaseModel with unique id and 
        timestamps for creation and updates.
        """
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the instance
        self.created_at = datetime.now()  # Set the creation time
        self.updated_at = datetime.now()  # Set the last update time

    def save(self):
        """Update the updated_at timestamp whenever the object is modified."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary.
        
        Args:
            data (dict): A dictionary of attributes and their new values 
                         to update the instance with.
        """
        for key, value in data.items():
            if hasattr(self, key):  # Check if the attribute exists in the object
                setattr(self, key, value)  # Update the attribute with the new value
        self.save()  # Update the updated_at timestamp after modifications
