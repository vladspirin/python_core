from math import pi


figure = input("Please enter your figure: ")
if figure == "circle":
    radius = int(input("Please enter radius: "))
    print(f"The area of the circle = {pi * radius ** 2}")
elif figure == "triangle":
    a = int(input("Please enter side A: "))
    b = int(input("Please enter side B: "))
    c = int(input("Please enter side C: "))
    p = 0.5 * (a + b + c)
    print(f"The area of the triangle = {p * (p - a) * (p - b) * (p - c)}")
elif figure == "rectangle":
    side1 = int(input("Please enter side A: "))
    side2 = int(input("Please enter side B: "))
    print(f"The area of the rectangle = {side1 * side2}")
