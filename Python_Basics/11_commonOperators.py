# COMMON OPERATORS ARE:
# AND
# OR
# NOT

owned_property = False
employed = True

# AND operator:

if owned_property and employed:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


# OR operator:

if owned_property or employed:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


# NOT operator:

if not employed:
    print("Eligible")
else:
    print("Not Eligible")


# For increasing Complexity:

citizen = True

if (employed or owned_property) and not citizen:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


# Short circuit condition:

# if any of the agument or variable is false the interpretre stops
# no matter what the other condition is.
if (employed and owned_property) and not citizen:  # all arguments must be True.
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
