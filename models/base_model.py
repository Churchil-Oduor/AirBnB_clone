#!/usr/bin/env python3
from datetime import datetime, timedelta
from uuid import uuid4
import time
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

        else:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dateTimeObj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dateTimeObj)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """returns strig representation"""
        message = "[{}] ({}) {}"
        return message.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves the current date and time when updated"""
        time.sleep(1)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """"creates and return a dictionary containing all
        key_value pairs
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value

        return my_dict
