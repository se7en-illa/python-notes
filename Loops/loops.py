board_games = ["Settlers of Catan", "Carcassone",
               "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

promise = "I will finish the python loops module!"

for temp in range(5):
    print(promise)


# while loops
count = 0
while count <= 3:
    # Loop Body
    print(count)
    count += 1

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

# while loop lists

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

index = 0
length = len(python_topics)

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1


# using break
dog_breeds_available_for_adoption = [
    "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"


for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break


# using continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    else:
        print(age)


# nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
    print(location)
    for data in location:
        scoops_sold += data

print(scoops_sold)


# list comprehensions
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)


single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)
print(squares)

cubes = [num ** 3 for num in single_digits]
print(cubes)
