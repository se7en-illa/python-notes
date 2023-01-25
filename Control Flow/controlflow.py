# Booleans are same as JS
# Equals: ==
# Not equals: !=
1 == 1     # True
2 != 4     # True
3 == 5     # False
'7' == 7   # False
statement_one = (5 * 2) - 1 == 8 + 1
statement_two = 13 - 6 != (3 * 2) + 1
statement_three = 3 * (2 - 1) == 4 - 1

# check types using type()
my_baby_bool = "true"
print(type(my_baby_bool))  # <class 'str'>

my_baby_bool_two = True
print(type(my_baby_bool_two))  # <class 'bool'>


# if statements
user_name = "Dave"

if user_name == "Dave":
    print("Get off my computer Dave!")

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
    print("I know it is you, Dave! Go away!")


# relational operators
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
x = 20
y = 20
# Write the first if statement here:
if x == y:
    print("These numbers are the same")

credits = 120
# Write the second if statement here:
if credits >= 120:
    print("You have enough credits to graduate!")


# boolean operator "and"
# and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise
(1 + 1 == 2) and (2 + 2 == 4)   # True
(1 > 9) and (5 != 6)            # False
(1 + 1 == 2) and (2 < 1)        # False
(0 == 10) and (1 + 1 == 1)      # False

# boolean operator "or"
# The boolean operator or combines two expressions into a larger expression that is True if either component is True.
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

credits = 118
gpa = 2.0
if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements."
          )

# boolean operator "not"
# This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.
not True == False
not False == True

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")


# else statements
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")


# else if statements
grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

    # REVIEW

# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.
# We can create boolean expressions using relational operators:
# ==: Equals
# !=: Not equals
# >: Greater than
# >=: Greater than or equal to
# <: Less than
# <=: Less than or equal to
# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements


# bugs
# SyntaxError: Error caused by not following the proper structure (syntax) of the language.
# NameError: Errors reported when the interpreter detects a variable that is unknown.
# TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.
