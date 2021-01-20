# 1
a = 2
b = 4
c = 9
d = 7
# 2
print('#2')
foo1 = a < b or b <= c and c > d or c >= d and a != d
print(foo1) # True
foo2 = (b == d)
print(foo2) # False
foo1 = foo2
print(foo1) # False
# 3
print('#3')
x = 10
print(x != 5)
print(x > 0 and x < 10)
print(x < 6 or x > 4)
print(x != 5 and x < 7)
