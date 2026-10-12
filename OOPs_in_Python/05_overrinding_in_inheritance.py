# OVERRIDING IN INHERITANCE:
# Method overriding allows a child class to provide its own implementation
# of a method that already exists in the parent class.
# This enables customized behavior while still maintaining the inheritance relationship.


class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


d = Dog()
d.sound()
