height = int(input('Input the side A: '))
length = int(input('Input the side B: '))
for i in range(length):
    if i == 0 or i == length - 1:
        for j in range(height):
            print('#', end='')
    else:
        print('#', end='')
        for j in range(1, height - 1):
            print('*', end='')
        print('#', end='')
    print()
