![AirBnB](./web_static/images/logo.png)

# Table of contents

> ![AirBnB](./assets/Screenshot%20from%202023-07-10%2014-59-47.png)

TASK NUMBER | LINK TO TASK CODE | TASK DESCRIPTION-
----- | ------ | ---------- 
[0x00] | [README](./README.md) | Project Documentation
[0x00] | [Authors](./AUTHORS) | Project Authors 
[0x01] | [Be pycodestyle compliant!](./) | Beautifully written code that passes the pycodestyle checks 
[0x02] | [Unittests](./tests) | All files, classes, functions have been tested with unit tests, also in Non-interactive mode
[0x03] | [BaseModel](./models/base_model.py) | Defines all common attributes/methods for other classes  i.e ID, creation, update dates and a method to generate a dictionary representation of an instance 
[0x04] | [Create BaseModel from dictionary](./models/base_model.py) | Re-creates an instance with the dictionary representation created in the previous task 
[0x05] | [Store first object](./models/base_model.py) | Re-creates a BaseModel from another one by using a dictionary representation created in task 3, converted the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.
[0x06] | [Console 0.0.1](./console.py) | Contains the entry point of the command interpreter using the Cmd class from the cmd module, defines the class HBNBCommand and sets the initial methods like quit, EOF and updates the prompt:
[0x07] | [Console 0.1](./console.py) | Added more methods to the console like updating details, showing details, destroing instances and more
[0x08] | [First User](./models/user.py) | Created the sub class User that inherits from the BAseModel with unique attribues like email, password, first and last names.
[0x09] | [More classes!](./models/) | Created the rest of the classes inheriting from BaseModel i.e Amenity, Place, City, State, etc 
[0x10] | [Console 1.0](./models/engine/file_storage.py) | Updated file storage to manage correctly serialization and deserialization of all our new classes
[0x11] | [All instances by class name](./console.py) | Updated the console to retrieve all instances of a class by using: <class name>.all().
[0x12] | [Count instances](./console.py) | Updated the console to retrieve all instances of a class by using: <class name>.count().
[0x13] | [Show](./console.py) | Updated the console to retrieve all instances of a class on its ID: <class name>.show(<id>).

> 
> 


>>> # Practising Objectives
Through this project, you will be able to explain to anyone, without the help of Google:

> # General

>> What is Unit testing and how to implement it in a large project

>> What is *args and how to use it

>> What is **kwargs and how to use it

>> How to handle named arguments in a function

>> How to create a MySQL database

>> How to create a MySQL user and grant it privileges

>> What ORM 

>> How to map a Python Class to a MySQL table

>> How to handle 2 different storage engines with the same codebase
>> How to use environment variables

# Table of contents

> ![AirBnB](./assets/Screenshot%20from%202023-08-22%2003-01-03.png)

TASK NUMBER | LINK TO TASK CODE | TASK DESCRIPTION-
----- | ------ | ---------- 
[0x03] | [MySQL setup development](./setup_mysql_dev.sql) | Script that prepares a MySQL server for the project by creating the Database "hbnb_dev_db" and User "hbnb_dev", grants this user all privileges on created database and SELECT rights on "performance_schema.*"
[0x04] | [MySQL setup development](./setup_mysql_test.sql) | Script that prepares a MySQL server for the project by creating the Database "hbnb_test_db" and User "hbnb_test", grants this user all privileges on created database and SELECT rights on "performance_schema.*"
[0x05] | [Delete object](./models/engine/file_storage.py) | Added a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method does nothing. Updated the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. R    