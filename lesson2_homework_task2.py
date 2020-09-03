items = list()

size = int(input('Enter size of list: '))

for ix in range(size):
    items.append(input('Enter item: '))

print(items)

ix = 0
while ix < size - 1:
    items[ix], items[ix+1] = items[ix+1], items[ix]
    ix += 2

print(items)



