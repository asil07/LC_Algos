print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


both_names = name1 + name2
print(both_names)
T = both_names.lower().count("t")
R = both_names.lower().count("r")
U = both_names.lower().count("u")
E = both_names.lower().count("e")

true = T + R + U + E
L = both_names.lower().count("l")
O = both_names.lower().count("o")
V = both_names.lower().count("v")
E = both_names.lower().count("e")

love = L + V + O + E

score = int(str(true) + str(love))

if 10 > score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f'Your score is {score}, you are alright together.')

else:
    print(f"Your score is {score}")



