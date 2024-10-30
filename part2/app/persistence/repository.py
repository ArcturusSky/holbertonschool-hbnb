from abc import ABC, abstractmethod

class Repository(ABC):
    """
    Abstract base class for a repository.
    
    A repository is responsible for storing, retrieving, updating, and deleting objects.
    Subclasses must implement all methods defined in this interface.
    """
    
    @abstractmethod
    def add(self, obj):
        """
        Add an object to the repository.

        Args:
            obj: The object to add.
        """
        pass

    @abstractmethod
    def get(self, obj_id):
        """
        Retrieve an object from the repository by its ID.

        Args:
            obj_id: The ID of the object to retrieve.

        Returns:
            The object with the given ID or None if not found.
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Retrieve all objects stored in the repository.

        Returns:
            A list of all objects in the repository.
        """
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """
        Update an existing object in the repository by its ID.

        Args:
            obj_id: The ID of the object to update.
            data: A dictionary with the data to update the object with.
        """
        pass

    @abstractmethod
    def delete(self, obj_id):
        """
        Delete an object from the repository by its ID.

        Args:
            obj_id: The ID of the object to delete.
        """
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object from the repository by a specific attribute and its value.

        Args:
            attr_name: The attribute name to filter by.
            attr_value: The value of the attribute to match.

        Returns:
            The object that matches the attribute or None if not found.
        """
        pass


class InMemoryRepository(Repository):
    """
    Concrete implementation of the Repository that stores objects in memory.

    This repository uses a dictionary to store objects, where the key is the object's ID.
    """
    
    def __init__(self):
        """
        Initialize an empty storage dictionary for the repository.
        """
        self._storage = {}

    def add(self, obj):
        """
        Add an object to the in-memory storage.

        Args:
            obj: The object to add. The object must have an 'id' attribute.
        """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """
        Retrieve an object from the in-memory storage by its ID.

        Args:
            obj_id: The ID of the object to retrieve.

        Returns:
            The object with the given ID or None if not found.
        """
        return self._storage.get(obj_id)

    def get_all(self):
        """
        Retrieve all objects stored in the in-memory storage.

        Returns:
            A list of all objects stored in memory.
        """
        return list(self._storage.values())

    def update(self, obj_id, data):
        """
        Update an existing object in the in-memory storage by its ID.

        Args:
            obj_id: The ID of the object to update.
            data: A dictionary of updated data for the object.

        Returns:
            The updated object or None if the object does not exist.
        """
        obj = self.get(obj_id)  # Retrieve the object by it's ID
        if obj:
            # Udpate object with new values
            for key, value in data.items():
                setattr(obj, key, value)  # Update each attribute
            return obj
        return None

    def delete(self, obj_id):
        """
        Delete an object from the in-memory storage by its ID.

        Args:
            obj_id: The ID of the object to delete.
        """
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieve an object from in-memory storage by a specific attribute and its value.

        Args:
            attr_name: The attribute name to filter by.
            attr_value: The value of the attribute to match.

        Returns:
            The first object that matches the attribute or None if not found.
        """
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
