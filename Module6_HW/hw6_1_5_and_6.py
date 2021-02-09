# 5
from random import randint

n = int(input("Input N: "))
my_list = [randint(-n, n) for i in range(n)]
print(my_list)

list1 = [i for i in my_list if i >= 0]
print(list1)

# 6
list2 = [list1.index(i) for i in list1 if i % 2 == 0]
print(list2)
