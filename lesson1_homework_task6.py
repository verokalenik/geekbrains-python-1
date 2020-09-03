a = int(input('Enter first result '))
b = int(input('Enter expected result '))

day_number = 1
while a < b:
   a *= 1.1
   day_number += 1

print('Day number', day_number)
