from random import randint

# 1
print('# 1')
my_list = ['apple', 'banana', 'pineapple', 'orange', 'apple', 34, 'python', 'python']
for i in my_list:
    if my_list.count(i) == 1:
        print(i)

# 2
print('# 2')
n = int(input("Please input the list length: "))
numbers = [randint(1, 100) for i in range(n)]
print(f'Our list: {numbers}')
max_elem = max(numbers)
print(f'Max elem = {max_elem}')
min_elem = min(numbers)
print(f'Min elem = {min_elem}')
temp = numbers[numbers.index(min_elem)]
numbers[numbers.index(min_elem)] = numbers[numbers.index(max_elem)]
numbers[numbers.index(max_elem)] = temp
print(f'Our new list: {numbers}')

# 3
print('# 3')
length = int(input("Please input the list length: "))
num = [randint(1, 10) for i in range(length)]
print(num)
counts = []
for item in num:
    counts.append(num.count(item))
print(f'The most common number is {num[counts.index(max(counts))]}')
