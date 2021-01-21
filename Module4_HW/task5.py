# 1
stringFirst = 'I like programming. And I like Python.'
# 2
print(stringFirst.upper())
# 3
print(stringFirst.lower())
# 4
listSpace = stringFirst.split(" ")
print(listSpace)
# 5
listDot = stringFirst.split(".")
print(listDot)
# 6
stringSecond = '-'.join(listSpace)
print(stringSecond)
# 7
print(stringFirst.find('Python'))
# 8
stringThird = stringSecond.replace('like', 'know')
print(stringThird)
