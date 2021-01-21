account = int(input("Please enter the amount of money: "))

if 0 < account >= 200:
    print(f"200 hrn = {account // 200} banknotes")
if 0 < account >= 100:
    print(f"100 hrn = {account // 100} banknotes")
if 0 < account >= 10:
    print(f"100 hrn = {account // 10} banknotes")
if 0 < account >= 1:
    print(f"1 hrn = {account // 1} monets")
