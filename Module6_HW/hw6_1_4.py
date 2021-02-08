from random import randint

list_1 = []
list_2 = []
numbers = [randint(-5, 5) for i in range(-5, 5)]
for i in numbers:
    print(i)
    if i < 0:
        list_1.append(i)
    if i > 0:
        list_2.append(i)
print(list_1)
print(list_2)
