import random

print("Hello! The goal for this app is to try and guess your age!")

name = input("What's your name? ")

ages = list(range(15, 31))
random.shuffle(ages)
    
for age in ages:
    answer = input(f"Are you {age} years old? (y/n): ").lower()
    if answer == "y":
        print(f"Yes! {name} is {age} years old.")
        break
    else:
        print("Rats.")
