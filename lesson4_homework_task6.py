from itertools import count
from itertools import cycle

x = int(input('Enter any number: '))
for el in count(x):
    if el < x+10:
        print(el)
    else:
        break

sq = input('Enter any sequence')

cnt = 0
for el in cycle(sq):
    if cnt < len(sq) * 5:
        print(el)
    else:
        break
    cnt += 1


