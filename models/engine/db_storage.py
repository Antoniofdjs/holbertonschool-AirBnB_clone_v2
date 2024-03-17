#!/usr/bin/python3
"""Engine for db"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage():
    """
        New Storage with SQL
    """
    __engine = None
    __session = None

    def __init__(self):
        db = os.getenv("HBNB_MYSQL_DB")
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        env_name = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}',
            pool_pre_ping=True
            )
        if env_name == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return dictionary of a class from the db
        """
        from models.base_model import BaseModel, Base
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
              }
        dictionary = {}

        if cls == None:
            for class_name in classes:
                result = self.__session.query(classes[class_name]).all()
                dictionary[class_name] = result
        else:
            result = self.__session.query(cls).all()
            dictionary[cls] = result

        return dictionary

    def new(self, obj):
        """
            add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
            commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session
        """

        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """
            Create all tables in the database
        """

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()