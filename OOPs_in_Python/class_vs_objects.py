# WHAT IS CLASS?
# => Class is Blueprint of an object, this means it defines an object can have, what kind of behaviour or Data. This is the consistantly used defination for class,
#    class for example: Painting of a car on a paper, its just a painting you can see it but
#    you can;t seat or Drive.
# - Class it defines set of attributes and methods that the created objects can have.

# WHEREAS:

# WHAT IS OBJECT?
# => Object is an real Instance of a Class and created from Class. This means from the obove example where you have seen
#    a painting of a car that you can only see. Here "OBJECT" is the Actual car exactly same  as "PAINTING". But in this you can
#    seat or Drive also.
# - It represents speacific implementation of the Class and hold their own data.

# Class: its the structure of object
# Object: its real instance created using same class

# Example of Class: Creating a Class.

class Dog:
    species = "Canine"  # class attribute

    def _init_(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


# Example of object: Creating an object.

class Dog:
    species = "Canine"  # class attribute

    def _init_(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute


# creating an object of a Dog.
Dog1 = Dog("Tommy", 3)


print(Dog1.name, Dog1.age, Dog1.species)

# OUTPUT:
# Student1:
