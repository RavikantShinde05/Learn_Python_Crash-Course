# UNIQUE: This is an important concept where we can get a unique value from a list. 
# # This is an essential method used and emplemented in DATABASE. This helps to remove Duplicate
#  items from list their are multiple ways to extract duplicate values from a list. 

# 1. for Example:

a = [1, 1, 2, 2, 3, 4, 5, 5, 7, 7, 9]
res = list(dict.fromkeys(a))
print(res)

# OUTPUT: [1, 2, 3, 4, 5, 7, 9]

# here dict.fromkeys create a dictionary with unique elements as Keys and removes duplicate
# values and create a list again at the output.

# 2. USING collections.OrderedDict:

from collections import OrderedDict

a = [1, 2, 4, 5, 7, 5, 8, 2, 9]
res = list(OrderedDict.fromkeys(a))
print(res)

# OUTPUT: it removes duplicate elements and create a list but it preserves the order
# or sequence of the LIst 
# [1, 2, 4, 5, 7, 8, 9]

# UNIQUE SET CONVERSION:

a = [1, 2, 4, 5, 2, 1, 0]
res = list(set(a))
print(res)

# OUTPUT: it create a set and removes duplicate values from list and give a 
# list back at the output but the original order is not preserved.

# USING FOR LOOP:

a = [1, 2, 3, 4, 6, 5, 2, 1, 0]
res = []

for item in a:
    if item not in res:
        res.append(item)
print(res)

# OUTPUT: this will iterate through all the elements from the list and
# adds elements or items to res only if they have'nt added already
#  [1, 2, 3, 4, 6, 5, 0]