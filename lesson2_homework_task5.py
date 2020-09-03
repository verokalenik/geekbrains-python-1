rating = [7, 5, 3, 3, 2]

while True:
    num = int(input('Enter new number: '))
    index = 0
    while index < len(rating):
        if rating[index] < num:
            break
        index += 1
    rating.insert(index, num)
    print(rating)
