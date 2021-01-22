import random


rnd = random.randint(0, 100)
print(rnd)
number = int(input("Please enter your number: "))
for i in range(0, 10):
    if i < number:
        print("")
