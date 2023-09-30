#!/usr/bin/python3
'''Database engine '''

from sqlalchemy import create_engine
from os import getenv as gv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """ MySQL Database class """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiates the databae engine """
        self.__engine = create_engine(f"mysql+mysqldb:// \
        {gv('HBNB_MYSQL_USER')}:{gv('HBNB_MYSQL_PWD')}@ \
        {gv('HBNB_MYSQL_HOST')}/{gv('HBNB_MYSQL_DB')}", pool_pre_ping=True)

        if gv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries current Database of all objects or just one """
        dict = {}
        if cls is None:
            for clas in classes.values():
                objects = self.__session.query(clas).all()
                for obj in objects:
                    dic_key = {obj.__class__.__name__} + '.' + {obj.id}
                    dict[dic_key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                dic_key = {obj.__class__.__name__} + '.' + {obj.id}
                dict[dic_key] = obj

    def new(self, obj):
        """ Adds an object to the current database """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception:
                self.__session.rollback()
                raise Exception

    def save(self):
        """ Saves/commits new added object to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes parameter from current Database """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """ Reloads the database """
        Base.metadata.create_all(self.__engine)
        session_reload = sessionmaker(
            bind=self.__self.engine, expire_on_commit=False)

    def get(self, cls, id):
        """ method to retrieve one object """
        if cls is not None:
            match = list(
                    filter(
                        lamba x: type(x) is cls and x.id == id,
                        self.__objects.values()
                        )
                    )
            if match:
                return match[0]
        return None

    def count(self, cls=None):
        """ counts the number of objects in storage """
        return len(self.all(cls))
