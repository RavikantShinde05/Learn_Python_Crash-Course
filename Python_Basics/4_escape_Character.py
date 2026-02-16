# ESCAPE_CHARACTERS:

person_name1 = "Harry Potter"  # this is a simple string.

# now the case where the there are 3 double Quotes
# the characters after 2nd Quotes will be useless in Python.
# to solve this in Python "Escape Characters" are introduce like "\".

# person_name2 = "Harry "Potter"
person_name3 = "Harry \" Potter"

print(person_name1)  # output: Harry Potter
# print(person_name2) # output: error at 3rd Quote.
print(person_name3)  # output: Harry " Potter  " '\"'  is escape sequence"

# ESCAPE CHARACTERS:

# esc Char  ||  output
# \"        -    "
# \'        -    '
# \\        -   \
# \n        -     add newline
