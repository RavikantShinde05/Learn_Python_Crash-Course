# CONDITION AND STATEMENTS:

# the indentation should be carefully handled
students = 35
if students > 35:
    print("all present")
elif students < 35:
    print("class have < 50 percent of attendance")
else:
    print("the class attendance is 50 percent")
print("Done")

# EXAMPLES:
# simple if elif:

age = 21
if age >= 21:
    print("Eligible")
else:
    print("not Eligible")

# or make it smaller for clean code:

age = 22
if age >= 21:
    message = "Eligible"
else:
    message = "Not Eligible"

# Then Modify this code into a Single line of Code:
    # This is the way of writting "Ternary Operator"
message = "Eligible" if age >= 21 else "Not Eligible"
print(message)

