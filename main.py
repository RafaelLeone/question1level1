x = range(2000, 3201, 7)

for number in x:
    remainder = number % 5
    if (remainder != 0):
        print(number, end=', ')