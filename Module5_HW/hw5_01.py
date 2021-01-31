import random


rnd = random.randint(0, 100)
print("You have 10 attempts. Please guess the number.")

for i in range(0, 10):
    number = int(input("Please enter your number: "))
    if rnd == number:
        print("You guessed the number.")
        break
    elif rnd < number:
        print("You entered a higher number.")
    elif rnd > number:
        print("You entered a lower number.")
else:
    print(f"You didn't guess the number. The number is {rnd}")
