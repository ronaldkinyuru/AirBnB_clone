#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
import uuid
from datetime import datetime

class BaseModel:

    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pair attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str (uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


