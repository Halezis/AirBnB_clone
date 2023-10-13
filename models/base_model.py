import uuid
from datetime import datetime

class BaseModel:
    """
	This is a base class that takes care of initiaiztion, serialization
	and deserialization of our instances
    """

    def __init__ (self, id, created_at, updated_at):
        """
        Constructor to initialize public instance attributes

        id: a unique identifier for each instance
        created_at: the datetime when an instance is created
        updated_at: the datetime each time an object is changed
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        A method in the class that prints in the desired format
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """
        A public instance method that updates 'updated_at' with the
        current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A p.i.m that returns a dictionary containing all keys/values of
        '__dict__' of the instance

        return: as stated
        """

        #converting the datetimes to ISO format
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        #creating a dictionary
        obj_dict = {
        "__class__": self.__class__.__name__,
        "created_at": created_at_iso,
        "updated_at": updated_at_iso,
        **self.__dict__
        }

        return obj_dict
