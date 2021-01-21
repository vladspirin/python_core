# 1
number = int(input("Please enter natural number: "))
if number % 2 == 0:
    print("This is even number")
elif number % 4 == 0:
    print("This number is multiple of 4")

# 2
number1 = int(input("Please enter natural number: "))
if number1 % 2 != 0:
    print("This is odd number")
elif number1 % 5 == 0:
    print("This number is multiple of 5")

# 3
number2 = int(input("Please enter real number: "))
if number2 > 0:
    print("This is a positive number")
elif number2 < 0:
    print("This is a negative number")
elif number2 == 0:
    print("Your number is equal 0")

# 4
seat_number = int(input("Plaese enter your seat number: "))
if seat_number % 2 == 0 and seat_number < 37:
    print("You got the bottom seat in the coupe")
elif seat_number % 2 == 0 and 37 < seat_number <= 54:
    print("You have a bottom side seat")
elif seat_number % 2 != 0 and seat_number < 37:
    print("You got the top seat in the coupe")
elif seat_number % 2 != 0 and 37 <= seat_number < 54:
    print("You have a top side seat")
