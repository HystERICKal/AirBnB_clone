#!/usr/bin/python3
"""The basemodel class"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """The basemodel class"""
    def __init__(self, *args, **kwargs):
        """instance initialization"""
        if kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for i, j in kwargs.items():
                if "__class__" not in i:
                    self.__setattr__(i, j)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Representation of string"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """Representation of string"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """'updated_at' instance gets updated"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """dict representation is returned"""
        the_dict = self.__dict__.copy()
        the_dict['created_at'] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        the_dict['updated_at'] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        the_dict['__class__'] = self.__class__.__name__
        return the_dict
