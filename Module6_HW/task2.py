from random import randint

# 1
print('# 1')
first_list = []
n = int(input("Please input N: "))
for i in range(n):
    first_list.append(randint(1, 100))
    print("%d, " % first_list[i], end="")
print()
position = int(input("The quantity of position: "))
direction = input("Left or right? L/R ")
if direction.upper() == 'L':
    new_list = first_list[position:] + first_list[:position]
else:
    new_list = [0] * position + first_list
print("Our new list: ")
for item in new_list:
    print("%d, " % item, end="")
print()
# 2
print('# 2')
second_list = [randint(1, 100) for i in range(10)]
print(second_list)
print(f'The max element = {max(second_list)}, Index of the max element = {second_list.index(max(second_list))}')
