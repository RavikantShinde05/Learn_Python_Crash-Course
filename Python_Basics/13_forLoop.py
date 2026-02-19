# FOR LOOP:

# Problem Statement:
# Print a message for "3" Times:

for number in range(3):
    # "5" is the number of iteration
    # "range" is an inbuilt function
    # "number" is an "int" type variable
    print("Message")


# Examples:

for number in range(2):
    print("Message", number)  # this iteration starts from "0"


for number in range(3):
    print("Message", number + 1)  # this iteration starts from "1"


for number in range(3):
    # this iteration starts from "1" with "*" symbol.
    print("Message", number + 1, (number + 1) * "*")


for number in range(3):
    # this iteration starts from "1" with "!" symbol.
    print("Message", number + 1, (number + 1) * "!")


# passing arguments:
for number in range(1, 4):
    # this iteration starts from "1" with "@" symbol.
    print("Message", number, number * "@")


# changing "number" variable:
for i in range(1, 4):
    # this iteration starts from "1" with "$" symbol.
    print("Message", i, i * "$")


# changing the range:
for i in range(2, 5):  # output: 3 times 5-2=3, i.e. 2,3,4.
    # this iteration starts from "1" with "$" symbol.
    print("Message", i, i * "$")


# adding arguments as steps:
for i in range(1, 12, 2):  # output: 1,3,5,7,9,11 with "$" sign.
    # this iteration starts from "1" with "$" symbol.
    print("Message", i, i * "$")


# make a right-angled triangel:
for i in range(1, 7):
    print(i * "*")
