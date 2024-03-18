
#!/usr/bin/python3
""" BACKUP VERSIONN"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
<<<<<<< HEAD
    
=======

>>>>>>> master
    id = Column(
        String(60),
        primary_key=True,
        nullable=False
<<<<<<< HEAD
        )
=======
    )
>>>>>>> master

    created_at = Column(
        DateTime,
        nullable=False,
<<<<<<< HEAD
        default=datetime.utcnow()
        )
=======
        default=datetime.utcnow
    )
>>>>>>> master

    updated_at = Column(
        DateTime,
        nullable=False,
<<<<<<< HEAD
        default=datetime.utcnow()
        )


    
=======
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

>>>>>>> master
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
<<<<<<< HEAD
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
=======
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
>>>>>>> master
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                          '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                          '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = type(self).__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
<<<<<<< HEAD
        self.updated_at = datetime.now()
=======
        self.updated_at = datetime.utcnow()
>>>>>>> master
        storage.new(self)
        storage.save()

    def delete(self):
<<<<<<< HEAD
        """Delete instance from  __objects from storage"""
=======
        """Delete instance from __objects from storage"""
>>>>>>> master
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
=======
        dictionary.pop('_sa_instance_state', None)
>>>>>>> master
        return dictionary
