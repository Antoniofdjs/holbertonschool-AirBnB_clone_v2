#!/usr/bin/python3
<<<<<<< HEAD
# models/engine/db_storage.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
=======
"""Engine for db"""


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage():
>>>>>>> master
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        classes = [State, City]
        if cls:
            classes = [cls]
        for class_ in classes:
            objects = self.__session.query(class_).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
=======

        user = getenv("HBNB_MYSQL_USER")
        psswd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        environ = getenv("HBNB_ENV")

        engine = create_engine(f"mysql+mysqldb://{user}:{psswd}@{host}/{db}")
        self.__engine = engine

        if environ == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """Returns dict of current database"""
        db_dict = {}
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        if cls:
            for key in classes.keys():
                if cls.__name__ == key:
                    objects = (self.__session.query(classes[key]).all())
                    obj_class = key
                    break
            for obj in objects:
                id = obj.id
                obj_key = '{}.{}'.format(obj_class, id)
                db_dict[obj_key] = obj
            return db_dict
        all_objects = (self.__session.query
                            (City, State, User, Place, Review, Amenity)
                            .filter(City.state_id == State.id,
                                    Place.user_id == User.id,
                                    Place.city_id == City.id,
                                    Review.place_id == Place.id,
                                    Review.user_id == User.id).all())
        for objs in all_objects:
            for obj in range(0, len(objs)):
                id = objs[obj].id
                obj_key = '{}.{}'.format(objs[obj].__class__, id)
                db_dict.update({obj_key: objs[obj]})
        return db_dict

    def new(self, obj):
        """Add new obj"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Save and commit session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj"""
        if obj is not None:
            results = self.__session.query(State, City, Place, User).all()
            for row in results:
                if obj == row:
                    self.__session.delete(row)
                    break
            self.save()

    def reload(self):
        """Reload, create all tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = (sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
>>>>>>> master
