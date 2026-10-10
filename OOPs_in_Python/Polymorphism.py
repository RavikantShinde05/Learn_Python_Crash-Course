# POLYMORPHISM: 
# "POLYMORPHISM" means "many forms" or same operation, different behavior.
# if allows a function or methods with the same name to work differently depending on the type
# of object they are acting upon.

# FOR EXAMPLE:
# - In an online payment system different payment methods such as "Credit Card, UPI, Wallet and NetBanking
#   all use the same processPayment() mehod.
# - The Method name remains the same, but each payment type performs its own specific payment process.


# Here we have different types of polymorphism, how can a single interface
# can exhibit multiple behaviors at "Compile" and "Run-time"

# Types of POLYMORPHISM:-
# 1. compile-time POLYMORPHISM:-
#       -Method Overloading.
# 2. Run-time POLYMORPHISM:-
#       - Method overloading.
#       - Duck Typing.
#       - Operator Overloading.

# Coding Example:
# 1. Compile-time Polymorphism allows multiple methods with the same name but different parameters.

class Calculator:
    def multiply(self, a=5, b=2, *args):
        result = a * b
        for num in args:
            result *= num
        return result


calc = Calculator()
print(calc.multiply())
print(calc.multiply(2))
print(calc.multiply(2, 4))
print(calc.multiply(2, 3, 4))


# OutPut:
# 10
# 4
# 8
# 24
