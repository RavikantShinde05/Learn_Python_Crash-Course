# SUPER() FUNCTION:
# Super() function is used to call methods from a superclass.
# Python's "Method Resolution Order"(MRO). it is commonly used in the child class's
# __init__() method to initialize attributes.

# Explanation:

# - super() function is used inside __init__() method of Dog to call the constructor of Animal and initialize inherited attribute (name).
# - This ensures that parent class functionality is reused without needing to rewrite the code in the child class.

# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name: ", self.name)


# Child class Dog:
class Dog(Animal):
    def _init__(self, name, bread):
        # class constructor based on MRO
        super().__init__(name)
        self.bread = bread

    def details(self):
        print(self.name, "is a ", self.bread)


d = Dog("Tommy", "Golden Retriever")
d.info()  # Parent Method
d.details()  # Child Method


# OUTPUT:
# Animal name: Buddy
# Buddy is a Golder Retriever
