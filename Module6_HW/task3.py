from random import randint

# 1
print('# 1')
my_list = ['apple', 'banana', 'pineapple', 'orange', 'apple', 34, 'python', 'python']
for i in my_list:
    if my_list.count(i) == 1:
        print(i)
# 2
print('# 2')
my_list2 = [randint(1, 20) for i in range(10)]
print(my_list2)
max_elem = max(my_list2)
print(f'The max element = {max_elem}')
min_elem = min(my_list2)
print(f'The min element = {min_elem}')
max_ind = my_list2.index(max(my_list2))
min_ind = my_list2.index(min(my_list2))
my_list2[max_ind], my_list2[min_ind] = my_list2[min_ind], my_list2[max_ind]
print(my_list2)

# 3
# print('# 3')
# my_list3 = [3, 12, 27, 3, 14, 5, 8, 5, 12, 3, 84, 2]
# print(my_list3)
# for i in my_list3:
#     print(my_list3.count(i))

