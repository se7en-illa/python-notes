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
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

# A 2d list with three lists in each of the indices.
tic_tac_toe = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"]
]

# Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]
print(noelles_height)

class_name_test = [["Jenny", 90], [
    "Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

# modifying 2d lists

class_name_hobbies = [["Jenny", "Breakdancing"], [
    "Alexus", "Photography"], ["Grace", "Soccer"]]
# The list of Jenny is at index 0. The hobby is at index 1.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

incoming_class = [["Kenny", "American", 9], [
    "Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]

incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken"
print(incoming_class)


# Python List Methods
# .count( - A list method to count the number of occurrences of an element in a list.
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)

# .insert() - A list method to insert an element into a specific index of a list.
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# •pop() - A list method to remove an element from a specific index or from the end of a list.
data_science_topics = ["Machine Learning", "SQL",
                       "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
data_science_topics.pop(-2)
print(data_science_topics)

# range() - A built-in Python function to create a sequence of integers.
number_list = range(0, 9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

# len() - A built-in Python function to get the length of a list.
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that",
             "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len)

big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length)

# slice
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# sort@/ sortedO-A method and a built- in function to sort a list
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place",
             "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]

print(addresses)
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)


games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)

print(games)
print(games_sorted)


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table",
             "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory = sorted(inventory)


# ZIPPPP

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
