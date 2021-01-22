# 1
min_value = int(input("Please enter your min value: "))
max_value = int(input("Please enter your max value: "))
step = int(input("Please enter step: "))
for i in range(min_value, max_value, step):
    print(i)
# 2
number = int(input("Please enter your number: "))
number = int(str(number)[::-1])
print(number)
