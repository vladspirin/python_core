number = input("Please enter your number: ")
string_length = len(number)

if int(number) >= 0:
    print(f"This is positive {string_length} digit number")
elif int(number) < 0:
    print(f"This is negative {string_length} digit number")
