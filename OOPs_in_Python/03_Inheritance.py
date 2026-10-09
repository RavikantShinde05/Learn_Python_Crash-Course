# INHERITANCE:
# Inheritance allows the class (child class) to acquire properties and
# methods of another class(Parent class). it supports hierarchical classification and helps in
# reuseability of code (promotes reuse of code)

# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name", self.name)


class Dog(Animal):
    def sound(self):
        print(self.name, "Barks")


d = Dog("Buddy")
# inheritance method:
d.info()
d.sound()

# output:
# Animal name Buddy
# Buddy Barks

# Here the class "Animal" is defined as a Parent class and "info()" function  method prints
# the name of the animal and class "Dog(Animal)", Where Dog is child class an (Animal) means
# inheriting properties or methods from "Animal" parent class. Now call the methods like;
# d.info() and d.sound()

# Benefits Of Inheritance
# Promotes code reusability by sharing attributes and methods across different classes.
# Models real-world hierarchies like Animal -> Dog or Person -> Employee.
# Simplifies maintenance through centralized updates in parent classes.
# Enables method overriding for customized subclass behavior.
# Supports scalable, extensible design using polymorphism.
