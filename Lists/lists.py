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

# accessing index
# When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
print(employees[4])

# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
# If we select the -1 index, we get the final element, "love".
print(pancake_recipe[-1])

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element)
print(index5_element)

# To change a value in a list, reassign the value using the specific index.
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden)

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
garden_waitlist[-1] = "Alex"
print(garden_waitlist)


# We can remove elements in a list using the .remove() Python method.
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
# We could remove "Chris" by using the .remove() method:

shopping_line.remove("Chris")
print(shopping_line)


# 2d lists