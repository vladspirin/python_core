counter = 0
positive_num = 0
negative_num = 0

while True:
    numbers = int(input("Input your number or type 0 to exit: "))
    if numbers == 0:
        break
    if numbers > 0:
        positive_num += 1
        counter += 1
    if numbers < 0:
        negative_num += 1
        counter += 1
print("All numbers %d " % counter)
print("Positive numbers %d" % (positive_num * 100 / counter), "%")
print("Negative numbers %d" % (negative_num * 100 / counter), "%")
