# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# small = 15
# medium = 20
# large = 25
total_bill = 0
if size.lower() == "s":
    total_bill += 15
    if add_pepperoni.lower() == "y":
        total_bill += 2
elif size.lower() == "m":
    total_bill += 20
    if add_pepperoni.lower() == "y":
        total_bill += 3
elif size.lower() == "l":
    total_bill += 25
    if add_pepperoni.lower() == 'y':
        total_bill += 3
if extra_cheese.lower() == "y":
    total_bill += 1
print(f"Your total bill {total_bill}$")
