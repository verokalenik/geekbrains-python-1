sum = 0

while True:
    inp_str = input('Enter list of numbers divided by space ')
    lst = inp_str.split(' ')
    for item in lst:
        if item == 'end':
            print('Result is ', sum)
            exit()
        else:
            sum += int(item)


