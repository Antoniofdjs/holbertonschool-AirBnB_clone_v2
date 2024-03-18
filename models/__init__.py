#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""

from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
=======
"""BACKUP VERSIOON"""


from models.engine.file_storage import FileStorage
import os

storage = os.getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
>>>>>>> master
    storage = FileStorage()

storage.reload()
