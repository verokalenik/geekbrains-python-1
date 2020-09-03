n = int(input('Enter a number '))

max_number = 0
while n > 0:
    if n % 10 > max_number:
        max_number = n % 10
    n //= 10

print('Max digit:', max_number)
