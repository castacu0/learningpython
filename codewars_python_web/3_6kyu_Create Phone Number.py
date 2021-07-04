
"""
Write a function that accepts an array of 10 integers
(between 0 and 9), that returns a string of those numbers
in the form of a phone number.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
# => returns "(123) 456-7890"


The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""

# def create_phone_number(n):
#     lol = "".join(map(str, n[0:5]))
#     parentheses = "".join(map(str, n[0:3]) )
#     three = "".join(map(str, n[3:6]) )
#     four = "".join(map(str, n[6:10]) )
#     return "("+ parentheses +") "+ three +"-"+ four + "   NEW: " + lol


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))