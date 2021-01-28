from random import randint

# 1
first_list = [34, 69, 574, 22, 47, 90, 5, 18]
for i in range(0, len(first_list), 3):
    first_list.insert(0, 0)
    print(first_list)
# 2
second_list = [randint(50, 500) for i in range(10)]
print(second_list)
print(f'The max element = {max(second_list)}, Index of the max element = {second_list.index(max(second_list))}')
