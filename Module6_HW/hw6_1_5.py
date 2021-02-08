from random import randint

n = int(input("Input N: "))
my_list = [randint(-n, n) for i in range(n)]
print(my_list)

my_list = [i for i in my_list if i >= 0]
print(my_list)
