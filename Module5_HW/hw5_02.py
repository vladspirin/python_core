count = 0
for i in range(10):
    n = int(input('Input the number: '))
    if n > 2:
        if n % 5 == 0:
            count += 1
print(count)
