#!/usr/bin/python3
"""DBSstorage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from os import getenv

class DBStorage():
    """Class for dbs storage, MISSING ALL"""
    __engine = None
    __session = None

    def __init__(self):

        usr = getenv('HBNB_MYSQL_USER')
        pswd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_DEV')

        engine = create_engine(f"mysql+mysqldb://{usr}:{pswd}@{host}/{db}",
                               pool_pre_ping=True)

        self.__engine = engine

        if env == "test":
            Base.metadata.dropall(self.__engine)
      
    def new(self, obj):
        """add new object to the current database db"""
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def all(self, cls=None):
        """Returns dict of current database"""  
        db_dict = {}
        classes = {
               'State': State, 'City': City
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

        all_objects = []
        for cls in classes.values():  # Get classes from dict to query all
            all_objects.extend(self.__session.query(cls).all())
        for obj in all_objects:
            id = obj.id
            obj_key = '{}.{}'.format(obj.__class__, id)
            db_dict.update({obj_key: obj})
        return db_dict

    def save(self):
        """Commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj"""
        if obj is not None:
            results = self.__session.query(State, City).all()
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
