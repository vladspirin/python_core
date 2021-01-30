from random import randint

numbers = [randint(-5, 4) for i in range(20)]
print(f'Our random list: {numbers}')
negative = 0
zero = 0
positive = 0
for i in numbers:
    if i < 0:
        negative += 1
    elif i == 0:
        zero += 1
    else:
        positive += 1
neg_list = [i for i in numbers if i < 0]
zero_list = [i for i in numbers if i == 0]
pos_list = [i for i in numbers if i > 0]
print("%d: " % negative, end="")
for item in neg_list:
    print("%d, " % item, end="")
print()
print("%d: " % zero, end="")
for item in zero_list:
    print("%d, " % item, end="")
print()
print("%d: " % positive, end="")
for item in pos_list:
    print("%d, " % item, end="")
print()
