# calculator :)
num_1 = int(input("Plaese enter the first number: "))
num_2 = int(input("Plaese enter the second number: "))
operation = input("Please enter math operation: ")
prog_exit = None
while prog_exit != 0:
    if operation == "+":
        print(f"Result = {num_1 + num_2}")
    elif operation == "-":
        print(f"Result = {num_1 - num_2}")
    elif operation == "*":
        print(f"Result = {num_1 * num_2}")
    elif operation == "/":
        print(f"Result = {num_1 / num_2}")
    else:
        prog_exit = int(input("If you want to exit please enter 0: "))
# in process....
