year = int(input("Please enter year: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'This is leap year. {year // 100 + 1}th century.')
else:
    print(f'This is normal year. {year // 100 + 1}th century.')
