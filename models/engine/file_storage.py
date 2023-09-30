#!/usr/bin/python3
"""FIle storage manager"""
import json


class FileStorage:
    """ File storage manager """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns object Dictionary """
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        dictionary = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                dictionary[key] = self.__objects[key]
        return dictionary

    def new(self, obj):
        """Adds new object to the dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """Saves dictionary to file"""
        with open(self.__file_path, 'w') as f:
            cont = {}
            cont.update(self.__objects)
            for key, val in cont.items():
                cont[key] = val.to_dict()
            json.dump(cont, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                cont = json.load(f)
                for key, value in cont.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' deletes the objects '''
        if obj is None:
            return
        object_key = obj.to_dict()['__class__'] + '.' + obj.id
        if object_key in self.__objects.keys():
            del self.__objects[object_key]

    def close(self):
        """Calls the reload function"""
        self.reload()

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
