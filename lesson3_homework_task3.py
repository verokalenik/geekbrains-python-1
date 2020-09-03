def my_func(*args):
    lst = sorted(args)
    return lst[1] + lst[2]


print(my_func(10, 2, 15))


