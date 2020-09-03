lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [lst[index] for index in range(1, len(lst) - 1) if lst[index] > lst[index - 1]]

print(res)
