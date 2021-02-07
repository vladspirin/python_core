def greatest_common_divisor(a, b):
    """Function to calculate the greatest common divisor"""
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a


def least_common_multiple(a, b):
    """Function to calculate the least common multiple"""
    return (a * b) / greatest_common_divisor(a, b)


def main():
    first = int(input('Input A '))
    second = int(input('Input B '))
    print("The greatest common divisor %d " % greatest_common_divisor(first, second))
    print("The least common multiple %d " % least_common_multiple(first, second))


if __name__ == '__main__':
    main()
