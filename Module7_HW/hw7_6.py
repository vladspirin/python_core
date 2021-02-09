def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main():
    n = int(input("Input the number from 0 to 1000: "))
    print(is_prime(n))


if __name__ == '__main__':
    main()
