str = input('Enter the string with a few variables separated by space: ')
words = str.split()

for word in words:
    print(word[:10])

