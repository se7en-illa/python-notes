import random

name = "Sah"
question = "Am I cute?"
answer = ""
random_number = random.randint(1, 12)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Are you kidding me?"
elif random_number == 11:
    answer = "Unfortunately not."
elif random_number == 12:
    answer = "Hell yes!"
else:
    answer = "Error"

if name and question:
    print(name + " asks: " + question)
elif not name and question:
    print("Question: " + question)
elif not question:
    print("Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!")

print("Magic 8-Ball's answer: " + answer)
