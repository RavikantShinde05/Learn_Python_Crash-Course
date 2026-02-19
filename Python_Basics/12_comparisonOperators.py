# COMPARISON OPERATORS:

# problem statment: age should be less than 21 and 70 for approval of loan:

# Simple Way:
age = 25
if age >= 21 and age < 70:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


# Chaining Comparison Operators:
if 21 <= age < 70:
    print("Eligible")
else:
    print("Not Eligible")


# EXAMPLES:

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# output: c


print("bag" > "cat")  # False
print("bag" > "apple")  # True

# Because when we sorting alphabetically "cat comes later than bag and apple comes
# early before bag":
