
#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER, DATETIME
from os import getenv


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    # Columns for sql tables, hold same values as the __init__
    id = Column(INTEGER, primary_key=True, nullable=False)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage

            self.id = str(uuid.uuid4())
            # Times for db
            if getenv("HBNB_TYPE_STORAGE") == "db":
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()
            # Times for file storage (json)
            else:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']

            # Assign values to columns for db when kwargs
            self.id = kwargs['id']
            self.created_at = kwargs['created_at']
            self.updated_at = kwargs['updated_at'] 
            kwargs.pop('_sa_instance_state', None)   

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.updated_at = datetime.utcnow()
        else:
            self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Delete current instance from storage"""
        from models import storage
        storage.delete(self)
