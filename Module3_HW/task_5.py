result = int(input("Please enter your result: "))
if 0 <= result <= 35:
    print("Fx")
elif 36 <= result <= 49:
    print("F")
elif 50 <= result <= 59:
    print("E")
elif 60 <= result <= 69:
    print("D")
elif 70 <= result <= 79:
    print("C")
elif 80 <= result <= 89:
    print("B")
elif 90 <= result <= 100:
    print("A")
else:
    print("Please enter correct result")
