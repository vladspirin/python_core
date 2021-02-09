from math import floor


def bank(n, years):
    total = n * 1.1
    for year in range(years - 1):
        total *= 1.1
    return floor(total)


def main():
    n = float(input("Input the deposit: "))
    years = int(input("Input the duration of deposit in years: "))
    print(bank(n, years))


if __name__ == '__main__':
    main()
