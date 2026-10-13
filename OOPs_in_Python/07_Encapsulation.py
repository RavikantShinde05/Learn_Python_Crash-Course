# ENCAPSULATION = Encapsulation means keeping Data(attributes) & Methods(functions) Binded within a class. 
# Restricting access to some components to control interactions.
# A Class is an example of encapsulation as it groups together member functions, variables and other related data in a single unit.

# EXAMPLE:

# Class = Methods + Variables.

# "Data" and the "Methods" that operate on that "Data" together. 
# While controlling the direct access to the internal state.



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp = Employee("David", 500)
print(emp.name)
print(emp.salary)
