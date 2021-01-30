from random import randint

# 1
print('# 1')
col = int(input('Please enter the number of columns: '))
row = int(input('Please enter the number of rows: '))
numbers = [[0] * col for row in range(row)]
for i in range(row):
    for j in range(col):
        numbers[i][j] = randint(1, 100)
        print("%4d" % numbers[i][j], end="")
    print()

# 2
print('# 2')
print(numbers)
# min row3 element and max column2
temp = []
for j in range(col):
    temp.append(numbers[2][j])
print('The min element in the 3rd row: %4d' % min(temp))
print(temp)
temp = []
for i in range(row):
    temp.append(numbers[i][1])
print('The max element in the 2nd column: %4d' % max(temp))
print(temp)

# 3
print('# 3')
print('Initial list: ')
for i in range(row):
    for j in range(col):
        print("%4d" % numbers[i][j], end="")
    print()

for i in range(row):
    tmp = numbers[i][3]
    numbers[i][3] = numbers[i][1]
    numbers[i][1] = tmp

print('Changed list: ')
for i in range(row):
    for j in range(col):
        print("%4d" % numbers[i][j], end="")
    print()

# 4
print('# 4')
sum_of_diagonal = sum([numbers[i][j] for i in range(row) for j in range(col) if i == j])
print("The sum of diagonal is %4d" % sum_of_diagonal, end="")
