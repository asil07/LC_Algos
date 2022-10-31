import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


rand_num = random.randint(0, len(names) - 1)
name = names[rand_num]

print(f"{name} is going to buy the meal today!")
