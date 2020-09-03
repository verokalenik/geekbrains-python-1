v1 = int(input('Enter the first number '))
v2 = int(input('Enter the second number '))


def function_divide(v1, v2):
    try:
        return v1 / v2
    except ZeroDivisionError:
        print('Zero division error')


print(function_divide(v1, v2))

