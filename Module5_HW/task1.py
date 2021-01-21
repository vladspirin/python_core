a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
count = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        count += i
print(count)