from random import randint

col = int(input('Please enter the number of columns: '))
row = int(input('Please enter the number of rows: '))
numbers = [[0] * col for row in range(row)]
numbers_new = [[0] * col for row in range(row)]
for i in range(row):
    for j in range(col):
        numbers[i][j] = randint(1, 100)
        print("%4d" % numbers[i][j], end="")
    print()

temp_list = []
for j in range(col):
    temp_list.append(numbers[0][j])

sorted_temp_list = sorted(temp_list)

print(sorted_temp_list)

index_list = []
for item in sorted_temp_list:
    index_list.append(temp_list.index(item))

print(index_list)

for j in range(5):
    for i in range(5):
        numbers_new[i][j] = numbers[i][index_list[j]]

for i in range(5):
    for j in range(5):
        print('%4d' % numbers_new[i][j], end='')
    print()
