from math import sqrt


def square(side):
    return tuple([4 * side, side ** 2, sqrt(2) * side])


def main():
    side = int(input("Input side: "))
    print(square(side))


if __name__ == '__main__':
    main()
