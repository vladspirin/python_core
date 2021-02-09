def is_year_leap(year):
    return True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False


def main():
    year = int(input("Input year: "))
    print(is_year_leap(year))


if __name__ == '__main__':
    main()
