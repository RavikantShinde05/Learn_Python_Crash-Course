# FUNCTIONS FOR STRING'S OPERATIONS:

# Speacial functions which are available on strings in python whareas these refer to as methods in OOPS
# these functions can be access by "." notation
person_name = "Harry Potter"

# These are the few methods for strings
print(person_name.upper())  # output: HARRY POTTER
# output: Harry potter  /first character capital and rest is lowercase.
print(person_name.capitalize())  # Harry potter  /first character capital.
print(person_name.lower())  # output> harry potter
print(person_name.title())  # output> Harry potter
print(person_name.strip)  # output>harry potter
print(person_name.lstrip())  # output>harry potter
print(person_name.rstrip())  # output> harry potter
# output> help to find index of character "P".
print(person_name.find("Potter"))
print(person_name.replace("Harry", "Python"))  # output> Python potter

# an experession to also find the character existence in string
# this funcition will give you a boolean value:
print("ter" in person_name)  # output> True
print("Tiger" not in person_name)  # output> True
