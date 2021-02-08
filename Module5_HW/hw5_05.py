P = int(input("Input P: "))
H = int(input("Input H: "))
print("If you want to exit input number = P or number = H")
sum_num = 0
mul_num = 1
counter = 0
while True:
    numbers = int(input("Input numbers: "))
    if numbers == P or numbers == H:
        break
    if numbers < P:
        sum_num += numbers
    if numbers > H:
        mul_num *= numbers
    if P < numbers < H:
        counter += 1
print("Sum of num < P = %d " % sum_num)
print("Mult of num > H = %d " % mul_num)
print("Amount of numbers between P and H %d " % counter)
