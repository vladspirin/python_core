month = {'January': None, 'February': None, 'March': None, 'April': None, 'May': None, 'June': None, 'July': None, 'August': None, 'September': None, 'October': None, 'November': None, 'December': None}
for key, value in month.items():
    month[key] = float(input(f"Please enter the {key} temperature: "))
for key, value in month.items():
    if month[key] == max(month.values()):
        print(f'The max temperature month is {key}')
