# calculator :)
sign = '+'
while sign != '0':
    num_1 = int(input("Plaese enter the first number: "))
    num_2 = int(input("Plaese enter the second number: "))
    sign = input("Please enter math operation: ")
    if (sign not in '+-/*'):
        print("Input correct operation")
        continue
    else:
        if sign == "+":
            print(f"Result = {num_1 + num_2}")
        if sign == "-":
            print(f"Result = {num_1 - num_2}")
        if sign == "*":
            print(f"Result = {num_1 * num_2}")
        if sign == "/":
            if num_2 != 0:
                print(f"Result = {num_1 / num_2}")
                continue
            else:
                print("Devision by zero")

