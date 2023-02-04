import calendar
print('Welcome to my calendar\n')
year = int(input('Please enter a year: '))
month = int(input('Enter a number for any month: '))
print(calendar.month(year, month))
print('Bye!')