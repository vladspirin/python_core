from random import randint

# 1
n = int(input('Input the length of the list: '))
numbers = [randint(1, 100) for i in range(n)]
print(f'Our random list: {numbers}')

# 2
n1 = int(input('Input the length of the list: '))
numbers2 = [int(input(f'Input {j} index number: ')) for j in range(n1)]
print(f'Our manual entered list: {numbers2}')

# 3
numbers3 = [sum(numbers), sum(numbers2)]
print(f'Our new list with sum of numbers: {numbers3}')