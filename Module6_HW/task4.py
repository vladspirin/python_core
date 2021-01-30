from random import randint

# 1
col = int(input('Please enter the number of columns: '))
row = int(input('Please enter the number of rows: '))
temp = [randint(1, 20) for i in range(col)]
print(temp)
my_list = []
for i in range(row):
    for j in range(col):
        ro = [randint(1, 20) for i in range(col)]
        my_list.append(ro)
        print("%4d" % my_list[i][j], end="")
    print()
# 2
# min row3 element and max column2
print(my_list)
for r in my_list:
    for c in r:
        if r == 2:
            print(min(r))
        # print(c, end=' ')
# 3

# 4

# table = [[0] * row for і in range(column)]
