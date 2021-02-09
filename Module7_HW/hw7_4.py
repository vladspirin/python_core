def season(month_num):
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    result = ""
    if month_num == 12 or month_num == 1 or month_num == 2:
        result = seasons[0]
    if month_num == 3 or month_num == 4 or month_num == 5:
        result = seasons[1]
    if month_num == 6 or month_num == 7 or month_num == 8:
        result = seasons[2]
    if month_num == 9 or month_num == 10 or month_num == 11:
        result = seasons[3]
    return result


def main():
    month_num = int(input("Input the number of month: "))
    print(season(month_num))


if __name__ == '__main__':
    main()
