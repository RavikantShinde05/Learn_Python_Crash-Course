from typing import Final
name = "Alice"
age = 22

print(name, age)
print("hello my name is", name)  # output: hello my name is Alice


# DATA TYPES:

number: int = 10  # integer value
decimal: float = 5.2
text: str = "Harry Potter"
active: bool = 10
names: list = ['alice', 'bob', 'david']  # list or queue of names
coordinates: tuple = (3.14, 9.81)  # values cannot be change
# values cannot be duplicated hence unique used in database to store id's.
unique: {1, 2, 5, 8, 9}
# use to store data in a key-value pair.
data: dict = {'name': 'alice', 'age': 20}


# TYPE ANNOTATIONS: it is just like defining the type of variable manually.

name = 'Alice'  # normal way
name: str = "Alice"  # annotations of variable type

age = 25
age: int = 26  # the age must be an integer as intended to be.


# We need to import Final from Typing:

# To define constant variables use "UpperCase"
VERSION: Final[str] = '22.18.04'

# Here you will get the warning about "version" is constant cannot be changed.
VERSION = '22.18.05'

# constant
PI: Final[float] = 3.14
