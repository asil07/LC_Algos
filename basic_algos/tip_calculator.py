# If the bill was $150.00, split between 5 people, with 12% tip.

# Write your code below this line 👇

print("Welcom to the tip calcualtor")
total_bill = float(input("How much is total bill? "))
percentage_tip = float(input("what percent r u gonna give? 10, 12, 15: "))
people = float(input("how many people to split the bill? "))

# Each person should pay (150.00 / 5) * 1.12 = 33.6
res = (percentage_tip / 100 * total_bill + total_bill) / people
print(f"Each person should pay {res}")




