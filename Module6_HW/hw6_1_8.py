from random import randint

n = int(input('Input N: '))
numbers = [randint(1, 100) for i in range(n)]
print(numbers)
maxEl = max(numbers)
print(f'Max elem = {maxEl}')
minEl = min(numbers)
print(f'Min elem = {minEl}')
tmp = numbers[numbers.index(minEl)]
numbers[numbers.index(minEl)] = numbers[numbers.index(maxEl)]
numbers[numbers.index(maxEl)] = tmp
print(numbers)
