# In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.

heights = [61, 70, 67, 64]

# A list begins and ends with square brackets ([ and ]).
# Each item (i.e., 67 or 70) is separated by a comma (,)
# It’s considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.

# Lists can contain more than just numbers.
ints_and_strings = [1, 2, 3, "four", "five", "six"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]

# You can create an empty list
empty_list = []

# In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.
# For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).
# An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = ['This', 'is', 'an', 'example']
append_example.append('list')
print(append_example)

orders = ["daisies", "periwinkle"]
orders.append("tulips")
orders.append("roses")
print(orders)

# When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]
