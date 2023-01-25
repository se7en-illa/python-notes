# Comments are declared with a hashtag.

# Variables do not need to be declared in Python like they do in JavasScript.
# Simply start with the name.

my_name = "Sah"

# Instead of console.log(), use print()
print("Hello and welcome " + my_name + "!")

# Like JS, in Python strings can use either single or double quotes
print("sah")
print('sah')

# Variables can be re-declared like JS
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = 'Turkey sandwich'

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "Spaghetti with meatballs"
# Printing out dinner
print("Dinner:")
print(meal)


# Common Python errors include SyntaxError and NameError
# SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.
# print('This message has mismatched quote marks!")
#   File "script.py", line 1
#     print('This message has mismatched quote marks!")
#                                                     ^
# SyntaxError: EOL while scanning string literal

# A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError.
# print(Abracadabra)
# Traceback (most recent call last):
#   File "script.py", line 2, in <module>
#     print(Abracadabra)
# NameError: name 'Abracadabra' is not defined


# NUMBERS
# int = whole number
# float = decimal number
# Define the release and runtime integer variables below:
release_year = 2019
runtime = 160
# Define the rating_out_of_10 float variable below:
rating_out_of_10 = 6.5

print(25 * 68 + 13 / 28)


# Variables that have numeric values can be treated as numbers
quilt_width = 8
quilt_length = 8
print(quilt_width * quilt_length)

# Python can also perform exponentiation
# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 3 * 6)

# Modulo operator works the same as JS
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)


# The + operator also concatenates text
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

# += works the same as JS, except it can also be used for string concatenation
# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14


# Multi-line strings use triple quotes """
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""

# we can assign info to a variable using input()
# >> > favorite_fruit = input("What is your favorite fruit? ")
# What is your favorite fruit? mango

# >> > print("Oh cool! I like " + favorite_fruit + " too, but I think my favorite fruit is apple.")
# Oh cool! I like mango too, but I think my favorite fruit is apple.
