n = int(input('Input the length of the list: '))
numbers = [int(input(f'Input {i} index number: ')) for i in range(n)]
print("Our manual entered list %s " % numbers)
print("The sum of numbers %d" % sum(numbers))
total = 1
for i in numbers:
    total *= i
print("The mult of numbers %d" % total)
