# CONSTRUCTOR:
# when an object is Created, the _init_() is the method that runs itself automatically.

# SELF:
# self refers to the recent or current object created.


class Car:
    def _init_(self, color, speed):
        self.color = color
        self.speed = speed


c1 = Car("Black", 190)

print("Color: ", c1.color)
print("speed: ", c1.speed)

# OUTPUT:
# Color: Black
# speed: 190
